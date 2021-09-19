from random import randint

from retrying import retry

import apysc as ap
from apysc._validation import string_validation
from tests import testing_helper


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_string_type() -> None:
    string_validation.validate_string_type(string='Hello!')
    string_validation.validate_string_type(string=ap.String('Hello!'))
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=string_validation.validate_string_type,
        kwargs={'string': 100})


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_not_empty_string() -> None:
    string_validation.validate_not_empty_string(string='Hello!')
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=string_validation.validate_not_empty_string,
        kwargs={'string': ''})
