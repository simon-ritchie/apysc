"""This module is for the documents' E2E testing.

Command example:
$ python ./scripts/run_docs_e2e_tests.py
"""

import os
from typing import List

from playwright.sync_api import sync_playwright
from playwright.sync_api import Playwright, Page, ConsoleMessage, Error



def _main() -> None:
    """Entry point of this script.
    """
    p: Playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        file_paths: List[str] = _get_file_paths()
        for file_path in file_paths:
            page: Page = browser.new_page()
            page.on(event='console', f=_on_console)
            page.on(event='pageerror', f=_on_pageerror)
            page.goto(url=file_path)
            print('Page title:', page.title())
            print('Page url:', page.url)


def _get_file_paths() -> List[str]:
    file_path_suffix: str = f'file://{os.path.abspath("./")}/docs/'
    file_paths: List[str] = [
        f'{file_path_suffix}en/assert_equal_and_not_equal.html',
        # f'{file_path_suffix}en/static/assert_equal_basic_usage/index.html',
    ]
    return file_paths


def _on_pageerror(err: Error) -> None:
    print('Error msg:', err.message)


def _on_console(message: ConsoleMessage) -> None:
    print('console msg:', message.text)
    print('message type:', message.type)


if __name__ == '__main__':
    _main()
