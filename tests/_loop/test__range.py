import re
from typing import Match
from typing import Optional

import pytest

import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._loop import _range
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test__create_single_arg_case_arr() -> None:
    expression_data_util.empty_expression()
    end: ap.Int = ap.Int(5)
    arr: ap.Array[ap.Int] = _range._create_single_arg_case_arr(end=end)
    expression: str = expression_data_util.get_current_expression()
    expected: str = (
        f"for (var i = 0; i < {end.variable_name}; i++) {{"
        f"\n  {arr.variable_name}.push(i);"
        "\n}"
    )
    assert expected in expression


@apply_test_settings()
def test__create_double_args_case_arr() -> None:
    expression_data_util.empty_expression()
    start: ap.Int = ap.Int(1)
    end: ap.Int = ap.Int(5)
    arr: ap.Array[ap.Int] = _range._create_double_args_case_arr(start=start, end=end)
    expression: str = expression_data_util.get_current_expression()
    expected: str = (
        f"for (var i = {start.variable_name}; i < {end.variable_name}; i++) {{"
        f"\n  {arr.variable_name}.push(i);"
        "\n}"
    )
    assert expected in expression


@apply_test_settings()
def test__create_triple_args_case_arr() -> None:
    expression_data_util.empty_expression()
    start: ap.Int = ap.Int(1)
    end: ap.Int = ap.Int(10)
    step: ap.Int = ap.Int(2)
    arr: ap.Array[ap.Int] = _range._create_triple_args_case_arr(
        start=start, end=end, step=step
    )
    expression: str = expression_data_util.get_current_expression()
    expected: str = (
        f"for (var i = {start.variable_name}; i < {end.variable_name}; "
        f"i += {step.variable_name}) {{"
        f"\n  {arr.variable_name}.push(i);"
        "\n}"
    )
    assert expected in expression


@apply_test_settings()
def test_range() -> None:
    with pytest.raises(ValueError):  # type: ignore
        ap.range()

    expression_data_util.empty_expression()
    arr: ap.Array[ap.Int] = ap.range(5)
    expression: str = expression_data_util.get_current_expression()
    match_: Optional[Match[str]] = re.search(
        pattern=rf"for \(var i = 0\; i \< {var_names.INT}\_.+?; i\+\+\) {{",
        string=expression,
    )
    assert match_ is not None
    match_ = re.search(
        pattern=rf"\n  {arr.variable_name}\.push\(i\)\;",
        string=expression,
    )
    assert match_ is not None

    expression_data_util.empty_expression()
    arr = ap.range(0, 10)
    expression = expression_data_util.get_current_expression()
    match_ = re.search(
        pattern=(
            rf"for \(var i = {var_names.INT}.+?\; i \< {var_names.INT}.+?\; i\+\+\) {{"
        ),
        string=expression,
    )
    assert match_ is not None
    match_ = re.search(
        pattern=rf"\n  {arr.variable_name}\.push\(i\)\;",
        string=expression,
    )
    assert match_ is not None

    expression_data_util.empty_expression()
    arr = ap.range(0, 10, 2)
    expression = expression_data_util.get_current_expression()
    match_ = re.search(
        pattern=(
            rf"for \(var i = {var_names.INT}.+?; i \< {var_names.INT}.+?\; "
            rf"i \+\= {var_names.INT}.+?\) {{"
        ),
        string=expression,
    )
    assert match_ is not None
    match_ = re.search(
        pattern=rf"\n  {arr.variable_name}\.push\(i\)\;",
        string=expression,
    )

    with pytest.raises(ValueError):  # type: ignore
        ap.range(0, 10, 2, 3)
