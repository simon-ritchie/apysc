import re
from random import randint
from typing import List
from typing import Match
from typing import Optional

from retrying import retry

from apysc._color import color_util


def test__fill_one_digit_hex_color_code() -> None:
    filled_color_code: str = color_util._fill_one_digit_hex_color_code(
        hex_color_code='a')
    assert filled_color_code == '00000a'


def test__fill_three_digit_hex_color_code() -> None:
    filled_color_code: str = color_util._fill_three_digit_hex_color_code(
        hex_color_code='a03')
    assert filled_color_code == 'aa0033'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_complement_hex_color() -> None:
    import apysc as ap
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

    hex_color_code_4: ap.String = ap.String('#222')
    hex_color_code_5: ap.String = color_util.complement_hex_color(
        hex_color_code=hex_color_code_4)
    assert hex_color_code_5 == '#222222'
    assert isinstance(hex_color_code_4, ap.String)
    assert hex_color_code_4.variable_name != hex_color_code_5.variable_name


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__append_complement_hex_color_expression() -> None:
    import apysc as ap
    from apysc._expression import expression_file_util
    expression_file_util.remove_expression_file()

    string_1: ap.String = ap.String('#333')
    string_2: ap.String = color_util.complement_hex_color(
        hex_color_code=string_1)
    expression: str = expression_file_util.get_current_expression()
    var_name: str = string_2.variable_name
    expected_patterns: List[str] = [
        rf'var str_length = {var_name}\.length;',
        r'\nif \(str_length === 1\) {',
        rf'\n  {var_name} = "00000" \+ {var_name};',
        r'\n}else if \(str_length === 3\) {',
        rf'\n  var {var_name}_ = "";',
        rf'\n  for \(var .+? = 0; .+? < {var_name}\.length; .+?\+\+\) {{',
        rf'\n    {var_name}_ \+= {var_name}\[.+?\]\.repeat\(2\);',
        r'\n}',
        rf'\n{var_name} = "#" \+ {var_name};'
    ]
    for expected_pattern in expected_patterns:
        match: Optional[Match] = re.search(
            pattern=expected_pattern,
            string=expression,
            flags=re.MULTILINE | re.DOTALL)
        assert match is not None, expected_pattern
