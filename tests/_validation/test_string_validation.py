import apysc as ap
from apysc._testing import testing_helper
from apysc._testing.testing_helper import apply_test_settings, assert_raises
from apysc._validation import string_validation


@apply_test_settings()
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


@apply_test_settings()
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


@apply_test_settings()
def test_validate_builtin_string_type() -> None:
    string_validation.validate_builtin_string_type(string="Hello!")
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=string_validation.validate_builtin_string_type,
        match="\nTest error!",
        string=ap.String("Hello!"),
        additional_err_msg="Test error!",
    )


@apply_test_settings()
def test_validate_apysc_string_type() -> None:
    string: ap.String = ap.String("Test")
    result_string: ap.String = string_validation.validate_apysc_string_type(
        string=string
    )
    assert result_string == string
    assert result_string.variable_name == string.variable_name

    assert_raises(
        expected_error_class=TypeError,
        callable_=string_validation.validate_apysc_string_type,
        string="Test",
    )
