import os
import re

from apysc._file import file_util
from apysc._string import string_util
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test_escape_str() -> None:
    string: str = "a\nb"
    string = string_util.escape_str(string=string)
    assert string == "a\\nb"

    string = string_util.escape_str(string=string)
    assert string == "a\\nb"


@apply_test_settings()
def test_wrap_by_double_quotation_if_value_is_string() -> None:
    value_1: int = string_util.wrap_by_double_quotation_if_value_is_string(value=100)
    assert value_1 == 100

    value_2: str = string_util.wrap_by_double_quotation_if_value_is_string(
        value="Hello!"
    )
    assert value_2 == '"Hello!"'


@apply_test_settings()
def test_escape_double_quotation() -> None:
    string: str = string_util.escape_double_quotation(string='"Hello", "World!"')
    assert string == '\\"Hello\\", \\"World!\\"'


@apply_test_settings()
def test_substitute_file_by_pattern() -> None:
    tmp_file_path: str = "../tmp_test_string_util.txt"
    with open(tmp_file_path, "w") as f:
        f.write("a = 1 + 1" "\nprint(200)" "\nb = a * 10")
    string_util.substitute_file_by_pattern(
        file_path=tmp_file_path, pattern=r"^print.+?\n", repl="", flags=re.MULTILINE
    )
    txt: str = file_util.read_txt(file_path=tmp_file_path)
    assert txt == ("a = 1 + 1" "\nb = a * 10")
    os.remove(tmp_file_path)


@apply_test_settings()
def test_replace_double_spaces_to_single_space() -> None:
    string: str = "Lorem   ipsum  dolor sit    amet"
    string = string_util.replace_double_spaces_to_single_space(string=string)
    assert string == "Lorem ipsum dolor sit amet"


@apply_test_settings()
def test_get_tails_lines_str() -> None:
    string: str = "a" "\nb" "\nc" "\nd" "\ne"
    tails_lines_str: str = string_util.get_tails_lines_str(string=string, n=3)
    assert tails_lines_str == ("c" "\nd" "\ne")
