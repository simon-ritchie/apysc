import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings
from apysc._type import string_lstrip_mixin


@apply_test_settings()
def test__create_string_none_case_expression() -> None:
    result_string: ap.String = ap.String("test_result_string")
    expression: str = string_lstrip_mixin._create_string_none_case_expression(
        result_string=result_string,
        self_variable_name="test_string",
    )
    expected: str = f"{result_string.variable_name} = test_string.trimStart();"
    assert expected in expression


@apply_test_settings()
def test__create_string_not_none_case_expression() -> None:
    ap.Stage()
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
            rf'\(new RegExp\(`\^\(\${{{var_names.STRING}\_.+?}}\)\+`\), ""\)\;'
        ),
        string=expression,
        flags=re.MULTILINE,
    )
    assert match_ is not None

    ap.Stage()
    removing_string = ap.String("a")
    expresion = string_lstrip_mixin._create_string_not_none_case_expression(
        result_string=result_string,
        removing_string=removing_string,
        self_variable_name="test_mixin",
        variable_name_suffix="test_suffix",
    )
    expected: str = (
        f"{result_string.variable_name} = test_mixin.replace"
        f'(new RegExp(`^(${{{removing_string.variable_name}}})+`), "");'
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
        string: ap.String = ap.String("aabbccaa")
        result: ap.String = string.lstrip(
            string="a", variable_name_suffix="test_suffix_1"
        )
        assert "test_suffix_1" in result.variable_name
        assert result == ap.String("bbccaa")
        expression: str = expression_data_util.get_current_expression()
        assert f"{string.variable_name}.replace(" in expression

        ap.Stage()
        replacing_string: ap.String = ap.String("a")
        result = string.lstrip(
            string=replacing_string, variable_name_suffix="test_suffix_2"
        )
        assert "test_suffix_2" in result.variable_name
        assert result == ap.String("bbccaa")
        expression = expression_data_util.get_current_expression()
        assert (
            f"{string.variable_name}.replace(new RegExp("
            f'`^(${{{replacing_string.variable_name}}})+`), "");'
        ) in expression

        ap.Stage()
        string = ap.String("  aabbccaa\n ")
        result = string.lstrip(string=None, variable_name_suffix="test_suffix_3")
        assert "test_suffix_3" in result.variable_name
        assert result == ap.String("aabbccaa\n ")
        expression = expression_data_util.get_current_expression()
        assert f"{string.variable_name}.trimStart();"
