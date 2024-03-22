"""Functions for helping other scripts."""
# pylint: disable=broad-exception-caught
from os import listdir
from os.path import join, abspath, dirname
import time
import json
import requests
from decouple import config
from pdf2image import convert_from_path

HOME = dirname(dirname(abspath(__file__)))
REPO_DIR = join(HOME, "assets/repos")
STOCK_DIR = join(HOME, "assets/certificates_stock")
CERTIFICATES_DIR = join(HOME, "assets/certificates")


def get_repos():
    """Saves all repo URLs and descriptions into the repos.json file."""
    base_url = "https://api.github.com/users/rokobo/repos"
    session = requests.Session()
    session.headers.update(
        {'Authorization': f'token {config("GH_TOKEN_SECRET")}'})
    data = []
    page = 1

    while True:
        try:
            response = session.get(base_url, params={'page': page})
            response.raise_for_status()
            repos = response.json()
            if not repos:
                break

            for repo in repos:
                response = session.get(repo['languages_url'])
                response.raise_for_status()
                languages = response.json()
                data.append(
                    [-1, repo['html_url'], repo['description'], languages]
                )
            page += 1

        except requests.RequestException as error:
            print(f"Error occurred: {error}")
            time.sleep(5)
            continue

        except Exception as error:
            print(f"Unexpected error: {error}")
            time.sleep(5)
            continue

    # Order, save and get images
    repos = order_repos(data)
    with open(join(REPO_DIR, "repos.json"), "w", encoding="utf-8") as file:
        json.dump(repos, file, indent=4)
    get_repo_images(data)


def order_repos(repos: list[list]) -> list[list]:
    """
    Used by get_repos to set an order variable to the repos using the
        order.json file.

    Args:
        repos (list[list]): List of repos.

    Returns:
        list[list]: List of repos with correct indexes.
    """
    with open(join(REPO_DIR, "order.json"), "r", encoding="utf-8") as file:
        order = json.load(file)

    for order_index, name in enumerate(order):
        for repo_index, data in enumerate(repos):
            if data[1] == name:
                repos[repo_index][0] = order_index
    repos = sorted(repos, key=lambda x: x[0])
    return repos


def get_repo_images(repos: list[list]):
    """
    Used by get_repos to save repo thumbnails in the /repos directory.

    Args:
        repos (list[list]): List of repos.
    """
    for data in repos:
        url = data[1]
        thumbnail_url = f"{url}/raw/main/thumbnail.png"
        response = requests.get(thumbnail_url, timeout=10)

        if response.status_code == 200:
            file_path = join(REPO_DIR, f"{url.split('/')[-1]}.png")
            with open(file_path, 'wb') as file:
                file.write(response.content)


def short_display_num(num: int) -> str:
    """
    Makes numbers be represented in a small string.

    Args:
        num (int): Integer value.

    Returns:
        str: String representation.
    """
    unit = iter(["", "k", "m", "b"])

    while True:
        string = str(num)
        if len(string) > 3:
            num = int(num / 1000)
            next(unit)
        else:
            break
    return string + next(unit)


def convert_certificates() -> None:
    """Converts certificates from .pdf to .png"""
    certificate_pdf = [
        f for f in listdir(STOCK_DIR) if f.endswith((".pdf"))]
    certificate_pdf.sort()
    certificate_png = [
        f for f in listdir(CERTIFICATES_DIR) if f.endswith(".png")]
    certificate_png.sort()

    pdfs = set([f[:-4] for f in certificate_pdf])
    pngs = set([f[:-4] for f in certificate_png])

    if pdfs == pngs:
        return

    for file in certificate_pdf:
        cv_pdf = join(STOCK_DIR, file)
        cv_png = f"assets/certificates/{file.replace('pdf', 'png')}"
        convert_from_path(cv_pdf)[0].save(cv_png, 'PNG')
