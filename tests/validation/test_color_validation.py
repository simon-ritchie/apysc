from tests import testing_helper
from apyscript.validation import color_validation


def test_validate_hex_color_code_format() -> None:
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=color_validation.validate_hex_color_code_format,
        kwargs={'hex_color_code': 10})

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=color_validation.validate_hex_color_code_format,
        kwargs={'hex_color_code': '33'}
    )

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=color_validation.validate_hex_color_code_format,
        kwargs={'hex_color_code': 'gggggg'})