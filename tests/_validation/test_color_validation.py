from random import randint

from retrying import retry

import apysc as ap
from apysc._testing import testing_helper
from apysc._validation import color_validation


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_hex_color_code_format() -> None:
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=color_validation.validate_hex_color_code_format,
        match='\nTest error!',
        hex_color_code=10,
        additional_err_msg='Test error!')

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=color_validation.validate_hex_color_code_format,
        hex_color_code='33',
    )

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=color_validation.validate_hex_color_code_format,
        hex_color_code='gggggg')

    color_validation.validate_hex_color_code_format(hex_color_code='333')
    color_validation.validate_hex_color_code_format(
        hex_color_code=ap.String('333'))
