from apyscript.validation import digit_validation
from tests import testing_helper


def test_validate_digit() -> None:
    digit_validation.validate_digit(digits=100)
    digit_validation.validate_digit(digits=100.5)
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=digit_validation.validate_digit,
        kwargs={'digits': 'Hello!'})


def test_validate_integer() -> None:
    digit_validation.validate_integer(integer=10)
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=digit_validation.validate_integer,
        kwargs={'integer': 10.5})
