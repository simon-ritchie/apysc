import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings
from apysc._type import string_rstrip_mixin


@apply_test_settings()
def test__create_string_none_case_expression() -> None:
    expression_data_util.empty_expression()
    result_string: ap.String = ap.String("test")
    expression: str = string_rstrip_mixin._create_string_none_case_expression(
        result_string=result_string,
        self_variable_name="test_variable_name",
    )
    expected: str = (
        f"{result_string.variable_name} = test_variable_name.trimEnd();"
    )
    assert expected in expression


@apply_test_settings()
def test__create_string_not_none_case_expression() -> None:
    expression_data_util.empty_expression()
    result_string: ap.String = ap.String("aabbaa")
    expression: str = string_rstrip_mixin._create_string_not_none_case_expression(
        result_string=result_string,
        removing_string="",
        self_variable_name="test_mixin",
        variable_name_suffix="test_suffix",
    )
    match_: Optional[Match] = re.search(
        pattern=(
            rf"{result_string.variable_name} = test_mixin"
            rf'\.replace\(new RegExp\(`\(\${{{var_names.STRING}_.+?}}\)\+\$`\), ""\);'
        ),
        string=expression,
        flags=re.MULTILINE,
    )
    assert match_ is not None

    expression_data_util.empty_expression()
    removing_string: ap.String = ap.String("a")
    expression = string_rstrip_mixin._create_string_not_none_case_expression(
        result_string=result_string,
        removing_string=removing_string,
        self_variable_name="test_mixin",
        variable_name_suffix="test_suffix",
    )
    expected: str = (
        f"{result_string.variable_name} = test_mixin"
        f'.replace(new RegExp(`(${{{removing_string.variable_name}}})+$`), "");'
    )
    assert expected in expression


# @apply_test_settings()
def test__get_py_str_from_current_value() -> None:
    py_str: str = string_rstrip_mixin._get_py_str_from_current_value(
        self_str=ap.String("  \n aabbccaa  \n  "),
        removing_string=None,
    )
    assert py_str == "  \\n aabbccaa"

    py_str = string_rstrip_mixin._get_py_str_from_current_value(
        self_str=ap.String("aabbccaa"),
        removing_string="a",
    )
    assert py_str == "aabbcc"

    py_str = string_rstrip_mixin._get_py_str_from_current_value(
        self_str=ap.String("aabbccaa"),
        removing_string=ap.String("a"),
    )
    assert py_str == "aabbcc"
