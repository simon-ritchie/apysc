"""This module is for the documents' E2E testing.

Command example:
$ python ./scripts/run_docs_e2e_tests.py
"""

import os
import sys
from typing import Dict
from typing import List
from typing import Optional

sys.path.append('./')

from apysc._lint_and_doc.docs_lang import Lang
from apysc._testing import e2e_testing_helper

_EXPECTED_ASSERTION_FAILED_MSGS: Dict[str, List[str]] = {
    'assertion_basic_behavior':
    ['', 'Values are not equal!'],
    'assert_equal_and_not_equal':
    ['Values are equal!', 'Values are not equal!'],
    'assert_true_and_false':
    ['Boolean value is not True!', 'Value is not Boolean(True)!'],
    'assert_arrays_equal_and_arrays_not_equal':
    ['Values are not equal!'],
    'assert_dicts_equal_and_dicts_not_equal':
    ['Values are not equal!'],
    'assert_defined_and_undefined':
    ['Value is not defined!'],
}


def _main() -> None:
    """Entry point of this script.
    """
    file_names: List[str] = _get_file_names()
    for file_name in file_names:
        file_path: str = e2e_testing_helper.get_docs_local_file_path(
            lang=Lang.EN, file_name=file_name)
        expected_assertion_failed_msgs: Optional[List[str]] = \
            _get_expected_assertion_failed_msgs(file_name=file_name)
        e2e_testing_helper.assert_local_file_not_raises_error(
            file_path=file_path,
            expected_assertion_failed_msgs=expected_assertion_failed_msgs)


def _get_expected_assertion_failed_msgs(
        *,
        file_name: str) -> Optional[List[str]]:
    """
    Get expected assertion failure messages if exist.

    Parameters
    ----------
    file_name : str
        A target document file name.

    Returns
    -------
    expected_assertion_failed_msgs : Optional[List[str]]
        Expected assertion failure messages. If there is no
        definition, this interface returns None.
    """
    for lang in Lang:
        if file_name.startswith(f'{lang.value}_'):
            file_name = file_name.replace(f'{lang.value}_', '', 1)
            break
    expected_assertion_failed_msgs: Optional[List[str]] = \
        _EXPECTED_ASSERTION_FAILED_MSGS.get(file_name)
    return expected_assertion_failed_msgs


def _get_file_names() -> List[str]:
    """
    Get target document's file names.

    Returns
    -------
    file_names : List[str]
        Target document's file names.'
    """
    file_names: List[str] = []
    for lang in Lang:
        dir_path: str = f'./docs/{lang.value}/'
        file_names_: List[str] = os.listdir(dir_path)
        file_name: str
        for file_name in file_names_:
            if not file_name.endswith('.html'):
                continue
            file_name = file_name.rsplit(sep='.', maxsplit=1)[0]
            file_names.append(file_name)
    return file_names



if __name__ == '__main__':
    _main()
