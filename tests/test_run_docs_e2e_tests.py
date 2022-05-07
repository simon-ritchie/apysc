from random import randint
from typing import List, Optional

from retrying import retry

from scripts import run_docs_e2e_tests


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_file_names() -> None:
    file_names: List[str] = run_docs_e2e_tests._get_file_names()
    expected_file_names: List[str] = [
        'index',
        'sprite',
        'jp_index',
        'jp_sprite',
    ]
    for expected_file_name in expected_file_names:
        assert expected_file_name in file_names


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_expected_assertion_failed_msgs() -> None:
    expected_assertion_failed_msgs: Optional[List[str]] = run_docs_e2e_tests.\
        _get_expected_assertion_failed_msgs(
            file_name='jp_assert_equal_and_not_equal')
    assert expected_assertion_failed_msgs == [
        'Values are equal!', 'Values are not equal!']

    expected_assertion_failed_msgs = run_docs_e2e_tests.\
        _get_expected_assertion_failed_msgs(
            file_name='sprite')
    assert expected_assertion_failed_msgs is None
