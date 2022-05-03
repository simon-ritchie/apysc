"""This module is for the documents' E2E testing.

Command example:
$ python ./scripts/run_docs_e2e_tests.py
"""

from playwright.sync_api import sync_playwright


def _main() -> None:
    """Entry point of this script.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url='https://simon-ritchie.github.io/apysc/en/index.html')
        print('page:', page.title())


if __name__ == '__main__':
    _main()
