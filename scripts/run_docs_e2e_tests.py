"""This module is for the documents' E2E testing.

Command example:
$ python ./scripts/run_docs_e2e_tests.py
"""

import os

from playwright.sync_api import sync_playwright


def _main() -> None:
    """Entry point of this script.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        os.path.abspath('./')
        file_path: str = os.path.join(
            f'file://{os.path.abspath("./")}/',
            'docs/en/index.html'
        )
        page.goto(url=file_path)
        print('Page title:', page.title())


if __name__ == '__main__':
    _main()
