
from apyscript.color import color_util


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
