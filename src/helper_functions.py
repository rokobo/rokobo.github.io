"""Functions for helping other scripts."""
# pylint: disable=broad-exception-caught
from os.path import join, abspath, dirname
import time
import json
import requests
from decouple import config

REPO_DIR = join(dirname(dirname(abspath(__file__))), "assets/repos")


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

    repos = order_repos(data)
    with open(join(REPO_DIR, "repos.json"), "w", encoding="utf-8") as file:
        json.dump(repos, file, indent=4)


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


def get_repo_images():
    """Saves repo thumbnails in the /repos directory."""
    with open(join(REPO_DIR, "repos.json"), "r", encoding="utf-8") as file:
        repos = json.load(file)

    for url in repos.keys():
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
