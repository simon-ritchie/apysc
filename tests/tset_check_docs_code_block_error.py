from random import randint
from typing import List

from retrying import retry

from scripts import check_docs_code_block_error
from apysc._testing.testing_helper import assert_raises


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__split_alphabets_group_str() -> None:
    assert_raises(
        expected_error_class=ValueError,
        func_or_method=check_docs_code_block_error._split_alphabets_group_str,
        kwargs={'alphabets_group_str': ''},
        match='An `--alphabets_group` argument\' value cannot be blank.')

    assert_raises(
        expected_error_class=ValueError,
        func_or_method=check_docs_code_block_error._split_alphabets_group_str,
        kwargs={'alphabets_group_str': 'a3c'},
        match='There is a non-alphabet character')

    assert_raises(
        expected_error_class=ValueError,
        func_or_method=check_docs_code_block_error._split_alphabets_group_str,
        kwargs={'alphabets_group_str': 'aba'},
        match='There are duplicated alphabets')

    alphabets_group: List[str] = check_docs_code_block_error.\
        _split_alphabets_group_str(alphabets_group_str='abc')
    assert alphabets_group == ['a', 'b', 'c']
