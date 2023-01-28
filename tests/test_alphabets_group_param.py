from random import randint
from typing import List

from retrying import retry

from apysc._testing.testing_helper import assert_raises
from scripts import alphabets_group_param
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test__split_alphabets_group_str() -> None:
    assert_raises(
        expected_error_class=ValueError,
        callable_=alphabets_group_param.split_alphabets_group_str,
        match="An `--alphabets_group` argument' value cannot be blank.",
        alphabets_group_str="",
    )

    assert_raises(
        expected_error_class=ValueError,
        callable_=alphabets_group_param.split_alphabets_group_str,
        match="There is a non-alphabet character",
        alphabets_group_str="a3c",
    )

    assert_raises(
        expected_error_class=ValueError,
        callable_=alphabets_group_param.split_alphabets_group_str,
        match="There are duplicated alphabets",
        alphabets_group_str="aba",
    )

    alphabets_group: List[str] = alphabets_group_param.split_alphabets_group_str(
        alphabets_group_str="abc"
    )
    assert alphabets_group == ["a", "b", "c"]
