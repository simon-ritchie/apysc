"""This module is for the documents' E2E testing.

Command example:
$ python ./scripts/run_docs_e2e_tests.py
"""

import os
from typing import Dict, List, Optional
import sys

from playwright.sync_api import sync_playwright
from playwright.sync_api import Playwright, Page, ConsoleMessage, Error

sys.path.append('./')

from apysc._tests import e2e_testing_helper
from apysc._lint_and_doc.docs_lang import Lang

_EXPECTED_ASSERTION_FAILED_MSGS: Dict[str, List[str]] = {
    'assert_equal_and_not_equal':
    ['Values are equal!', 'Values are not equal!'],
}


def _main() -> None:
    """Entry point of this script.
    """
    file_names: List[str] = [
        'index',
        'assert_equal_and_not_equal',
    ]
    for file_name in file_names:
        file_path: str = e2e_testing_helper.get_docs_local_file_path(
            lang=Lang.EN, file_name=file_name)
        expected_assertion_failed_msgs: Optional[List[str]] = \
            _EXPECTED_ASSERTION_FAILED_MSGS.get(file_name)
        e2e_testing_helper.assert_local_file_not_raises_error(
            file_path=file_path,
            expected_assertion_failed_msgs=expected_assertion_failed_msgs)


if __name__ == '__main__':
    _main()
