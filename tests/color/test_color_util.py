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


def test__fill_one_digit_hex_color_code() -> None:
    filled_color_code: str = color_util._fill_one_digit_hex_color_code(
        hex_color_code='a')
    assert filled_color_code == '00000a'


def test__fill_three_digit_hex_color_code() -> None:
    filled_color_code: str = color_util._fill_three_digit_hex_color_code(
        hex_color_code='a03')
    assert filled_color_code == 'aa0033'


def test_complement_hex_color() -> None:
    hex_color_code: str = color_util.complement_hex_color(
        hex_color_code='0')
    assert hex_color_code == '#000000'

    hex_color_code = color_util.complement_hex_color(hex_color_code='#03f')
    assert hex_color_code == '#0033ff'

    hex_color_code = color_util.complement_hex_color(hex_color_code='FFCC00')
    assert hex_color_code == '#ffcc00'
