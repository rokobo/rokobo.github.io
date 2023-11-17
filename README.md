# Personal portfolio using Github Pages and Dash

[![Github Pages](https://github.com/rokobo/rokobo.github.io/actions/workflows/deploy.yml/badge.svg)](https://github.com/rokobo/rokobo.github.io/actions/workflows/deploy.yml)
[![Tests](https://github.com/rokobo/rokobo.github.io/actions/workflows/test.yml/badge.svg)](https://github.com/rokobo/rokobo.github.io/actions/workflows/test.yml)
[![License: MPL 2.0](https://img.shields.io/badge/License-MPL_2.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0)

## Deployment of a Dash app

This project was my first experience with Github Actions, which proved to be a valuable learning experience. This project’s workflow is comprised of the following:

+ `test.yml` workflow: Runs all Pytest tests.

+ `deploy.yml` workflow: Runs the Dash app, builds the static website via `wget` (using a Makefile), uploads artifacts and deploys to Github Pages.

## Multi-page support without using server-side callbacks

Typically, Dash apps can quickly support multi-page setups. However, the native pages system depends on one server-side callback. To get around this, I loaded each page’s layout into a tab of the `dbc.Tabs` component, then used a client-side callback to change the active tab of this component using the current URL.

## Projects section

This project was also my first experience with repository secrets. For making the project cards, I need to have my repository URLs and thumbnails. However, doing it without a Github token was severely limited, so I setup an environment variable for retrieving both of them.
