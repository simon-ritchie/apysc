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
