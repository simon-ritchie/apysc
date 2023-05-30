from typing import Optional, Match
import re

import apysc as ap
from apysc._expression import expression_data_util
from apysc._type.string_strip_mixin import StringStripMixIn
from apysc._type import string_strip_mixin
from apysc._testing.testing_helper import apply_test_settings
from apysc._expression import var_names


@apply_test_settings()
def test__create_string_none_case_expression() -> None:
    expression_data_util.empty_expression()
    result_string: ap.String = ap.String("test")
    expression: str = string_strip_mixin._create_string_none_case_expression(
        result_string=result_string,
        self_variable_name="test_variable_name",
    )
    expected: str = (
        f"{result_string.variable_name} = test_variable_name.trim();"
    )
    assert expected in expression


@apply_test_settings()
def test__create_string_not_none_case_expression() -> None:
    expression_data_util.empty_expression()
    result_string: ap.String = ap.String("aaabbbcccaaa")
    expression: str = string_strip_mixin._create_string_not_none_case_expression(
        result_string=result_string,
        removing_string="a",
        self_variable_name="test_variable_name",
        variable_name_suffix="test_suffix",
    )
    match_: Optional[Match] = re.search(
        pattern=(
            rf"{result_string.variable_name} = test_variable_name"
            rf'\.replace\(new RegExp\(\`\^\(\${{{var_names.STRING}\_.+}}\)\+\`\), ""\);'
        ),
        string=expression,
        flags=re.MULTILINE,
    )
    assert match_ is not None
    match_ = re.search(
        pattern=(
            rf"{result_string.variable_name} = test_variable_name"
            rf'\.replace\(new RegExp\(\`\(\${{{var_names.STRING}\_.+}}\)\+\$\`\), ""\);'
        ),
        string=expression,
        flags=re.MULTILINE,
    )

    expression_data_util.empty_expression()
    removing_string: ap.String = ap.String("a")
    expression = string_strip_mixin._create_string_not_none_case_expression(
        result_string=result_string,
        removing_string=removing_string,
        self_variable_name="test_variable_name",
        variable_name_suffix="test_suffix",
    )
    expected: str = (
        f"{result_string.variable_name} = test_variable_name"
        f'.replace(new RegExp(`^(${{{removing_string.variable_name}}})+`), "");'
    )
    assert expected in expression
    expected = (
        f"\n{result_string.variable_name} = test_variable_name"
        f'.replace(new RegExp(`(${{{removing_string.variable_name}}})+$`), "");'
    )
    assert expected in expression


@apply_test_settings()
def test__get_py_str_from_current_value() -> None:
    py_str: str = string_strip_mixin._get_py_str_from_current_value(
        self_str=ap.String("  \n  aabbaa  "),
        removing_string=None,
    )
    assert py_str == "aabbaa"

    py_str = string_strip_mixin._get_py_str_from_current_value(
        self_str=ap.String("aabbaa"),
        removing_string=ap.String("a"),
    )
    assert py_str == "bb"

    py_str = string_strip_mixin._get_py_str_from_current_value(
        self_str=ap.String("aabbaa"),
        removing_string="a",
    )
    assert py_str == "bb"
