from random import randint

from retrying import retry

import apysc as ap
from apysc._testing import testing_helper
from apysc._validation import string_validation


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_string_type() -> None:
    string_validation.validate_string_type(string="Hello!")
    string_validation.validate_string_type(string=ap.String("Hello!"))
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=string_validation.validate_string_type,
        match="\nTest error!",
        string=100,
        additional_err_msg="Test error!",
    )


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_not_empty_string() -> None:
    string_validation.validate_not_empty_string(string="Hello!")
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=string_validation.validate_not_empty_string,
        string="",
        additional_err_msg="Test error!",
        match="\nTest error!",
    )

    string_validation.validate_not_empty_string(string=ap.String("Hello!"))
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=string_validation.validate_not_empty_string,
        string=ap.String(""),
    )


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_builtin_string_type() -> None:
    string_validation.validate_builtin_string_type(string="Hello!")
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=string_validation.validate_builtin_string_type,
        match="\nTest error!",
        string=ap.String("Hello!"),
        additional_err_msg="Test error!",
    )
