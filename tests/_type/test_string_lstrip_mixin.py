import re
from typing import Optional, Match

import apysc as ap
from apysc._expression import expression_data_util, var_names
from apysc._type.string_lstrip_mixin import StringLStripMixIn
from apysc._type import string_lstrip_mixin
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test__create_string_none_case_expression() -> None:
    result_string: ap.String = ap.String("test_result_string")
    expression: str = string_lstrip_mixin._create_string_none_case_expression(
        result_string=result_string,
        self_variable_name="test_string",
    )
    expected: str = (
        f"{result_string.variable_name} = test_string.trimStart();"
    )
    assert expected in expression


@apply_test_settings()
def test__create_string_not_none_case_expression() -> None:
    expression_data_util.empty_expression()
    result_string: ap.String = ap.String("aaabbb")
    expression: str = string_lstrip_mixin._create_string_not_none_case_expression(
        result_string=result_string,
        removing_string="a",
        self_variable_name="test_mixin",
        variable_name_suffix="test_suffix",
    )
    match_: Optional[Match] = re.search(
        pattern=(
            rf"{result_string.variable_name} = test_mixin\.replace"
            rf'\(new RegExp\(`\^\(\${var_names.STRING}\_.+?\)\+`\), ""\)\;'
        ),
        string=expression,
        flags=re.MULTILINE,
    )
    assert match_ is not None

    expression_data_util.empty_expression()
    removing_string = ap.String("a")
    expresion = string_lstrip_mixin._create_string_not_none_case_expression(
        result_string=result_string,
        removing_string=removing_string,
        self_variable_name="test_mixin",
        variable_name_suffix="test_suffix",
    )
    expected: str = (
        f"{result_string.variable_name} = test_mixin.replace"
        f'(new RegExp(`^(${removing_string.variable_name})+`), "");'
    )
    assert expected in expresion


@apply_test_settings()
def test__get_py_str_from_current_value() -> None:
    self_str: ap.String = ap.String("aaabbcc")
    py_str: str = string_lstrip_mixin._get_py_str_from_current_value(
        self_str=self_str,
        removing_string="a",
    )
    assert py_str == "bbcc"

    py_str = string_lstrip_mixin._get_py_str_from_current_value(
        self_str=self_str,
        removing_string=ap.String("a"),
    )
    assert py_str == "bbcc"


class TestLStripMixIn:
    @apply_test_settings()
    def test_lstrip(self) -> None:
        expression_data_util.empty_expression()
        string: ap.String = ap.String("aabbcc")
        pass
