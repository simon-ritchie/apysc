from apyscript.string import string_util


def test_escape_str() -> None:
    string: str = 'a\nb'
    string = string_util.escape_str(string=string)
    assert string == 'a\\nb'
