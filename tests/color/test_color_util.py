
from apyscript.color import color_util
from apyscript.type import String


def test__fill_one_digit_hex_color_code() -> None:
    filled_color_code: str = color_util._fill_one_digit_hex_color_code(
        hex_color_code='a')
    assert filled_color_code == '00000a'


def test__fill_three_digit_hex_color_code() -> None:
    filled_color_code: str = color_util._fill_three_digit_hex_color_code(
        hex_color_code='a03')
    assert filled_color_code == 'aa0033'


def test_complement_hex_color() -> None:
    hex_color_code_1: str = color_util.complement_hex_color(
        hex_color_code='0')
    assert hex_color_code_1 == '#000000'
    assert isinstance(hex_color_code_1, str)

    hex_color_code_2: str = color_util.complement_hex_color(
        hex_color_code='#03f')
    assert hex_color_code_2 == '#0033ff'
    assert isinstance(hex_color_code_2, str)

    hex_color_code_3: str = color_util.complement_hex_color(
        hex_color_code='FFCC00')
    assert hex_color_code_3 == '#ffcc00'
    assert isinstance(hex_color_code_3, str)

    hex_color_code_4: String = String('#222')
    assert hex_color_code_4 == '#222222'
    assert isinstance(hex_color_code_4, String)
