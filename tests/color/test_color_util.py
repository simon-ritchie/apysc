import pytest

from apyscript.color import color_util
from tests import testing_helper


def test__validate_hex_color_code_format() -> None:
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=color_util._validate_hex_color_code_format,
        kwargs={'hex_color_code': 10})

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=color_util._validate_hex_color_code_format,
        kwargs={'hex_color_code': '33'}
    )

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=color_util._validate_hex_color_code_format,
        kwargs={'hex_color_code': 'gggggg'})
