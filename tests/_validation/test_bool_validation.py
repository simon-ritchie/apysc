from apysc._testing import testing_helper
from apysc._validation import bool_validation


def test_validate_bool() -> None:
    bool_validation.validate_bool(value=True)
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=bool_validation.validate_bool,
        kwargs={'value': 1})
