from random import randint

from retrying import retry

import apysc as ap
from apysc._testing import testing_helper
from apysc._validation import bool_validation
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test_validate_bool() -> None:
    bool_validation.validate_bool(value=True)
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=bool_validation.validate_bool,
        match="\nTest error!",
        value=1,
        additional_err_msg="Test error!",
    )


@apply_test_settings()
def test_validate_builtin_bool() -> None:
    bool_validation.validate_builtin_bool(value=True)
    bool_validation.validate_builtin_bool(value=False)
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=bool_validation.validate_builtin_bool,
        match="\nTest error!",
        value=ap.Boolean(True),
        additional_err_msg="Test error!",
    )
