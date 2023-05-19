import apysc as ap
from apysc._testing.testing_helper import apply_test_settings
from apysc._expression import expression_data_util
from apysc._loop import _range


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
