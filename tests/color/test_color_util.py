from random import randint

from retrying import retry

from apyscript.color import color_util


def test__fill_one_digit_hex_color_code() -> None:
    filled_color_code: str = color_util._fill_one_digit_hex_color_code(
        hex_color_code='a')
    assert filled_color_code == '00000a'


def test__fill_three_digit_hex_color_code() -> None:
    filled_color_code: str = color_util._fill_three_digit_hex_color_code(
        hex_color_code='a03')
    assert filled_color_code == 'aa0033'


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test_complement_hex_color() -> None:
    from apyscript.type import String
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
    hex_color_code_5: String = color_util.complement_hex_color(
        hex_color_code=hex_color_code_4)
    assert hex_color_code_5 == '#222222'
    assert isinstance(hex_color_code_4, String)
    assert hex_color_code_4.variable_name != hex_color_code_5.variable_name


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test__append_complement_hex_color_expression() -> None:
    from apyscript.expression import expression_file_util
    from apyscript.type import String
    expression_file_util.remove_expression_file()

    string_1: String = String('#333')
    string_2: String = color_util.complement_hex_color(
        hex_color_code=string_1)
    expression: str = expression_file_util.get_current_expression()
    var_name: str = string_2.variable_name
    expected: str = f"""var str_length = {var_name}.length;
if (str_length === 1) {{
  {var_name} = "00000" + {var_name};
}}else if (str_length === 3) {{
  {var_name} = {var_name}.repeat(2);
}}"""
    assert expected in expression
