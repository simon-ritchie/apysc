from random import randint

from retrying import retry

import apysc as ap
from apysc._testing import testing_helper
from apysc._validation import color_validation
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test_validate_hex_color_code_format() -> None:
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=color_validation.validate_hex_color_code_format,
        match="\nTest error!",
        hex_color_code=10,
        additional_err_msg="Test error!",
    )

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=color_validation.validate_hex_color_code_format,
        hex_color_code="33",
    )

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=color_validation.validate_hex_color_code_format,
        hex_color_code="gggggg",
    )

    color_validation.validate_hex_color_code_format(hex_color_code="")
    color_validation.validate_hex_color_code_format(hex_color_code="0")
    color_validation.validate_hex_color_code_format(hex_color_code="333")
    color_validation.validate_hex_color_code_format(hex_color_code=ap.String("333"))
    color_validation.validate_hex_color_code_format(hex_color_code=ap.String("0af"))
    color_validation.validate_hex_color_code_format(hex_color_code=ap.String("00aaff"))
