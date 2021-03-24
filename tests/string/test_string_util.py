from apysc.string import string_util


def test_escape_str() -> None:
    string: str = 'a\nb'
    string = string_util.escape_str(string=string)
    assert string == 'a\\nb'


def test_wrap_by_double_quotation_if_value_is_string() -> None:
    value_1: int = string_util.wrap_by_double_quotation_if_value_is_string(
        value=100)
    assert value_1 == 100

    value_2: str = string_util.wrap_by_double_quotation_if_value_is_string(
        value='Hello!')
    assert value_2 == '"Hello!"'
