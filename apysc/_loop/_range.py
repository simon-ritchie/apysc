"""The implementation for the `range` function.
"""

from typing import Any

from apysc._type.array import Array
from apysc._type.int import Int
from apysc._validation import arg_validation_decos


@arg_validation_decos.variadic_args_len_is_between(min_length=1, max_length=3)
@arg_validation_decos.all_variadic_args_are_integers(optional=False)
def range(*args: Any) -> Array[Int]:
    """
    Create a range array of integers.

    Returns
    -------
    arr : Array[Int]
        A created array.

    References
    ----------
    - range function
        - https://simon-ritchie.github.io/apysc/en/range.html

    Examples
    --------
    >>> import apysc as ap

    >>> range_arr: ap.Array[ap.Int] = ap.range(5)
    >>> ap.assert_equal(range_arr, [0, 1, 2, 3, 4])

    >>> range_arr = ap.range(2, 4)
    >>> ap.assert_equal(range_arr, [2, 3])

    >>> range_arr = ap.range(2, 10, 2)
    >>> ap.assert_equal(range_arr, [2, 4, 6, 8])
    """
    from apysc._converter import to_apysc_val_from_builtin

    if len(args) == 1:
        end: Int = to_apysc_val_from_builtin.get_copied_int_from_builtin_val(
            integer=args[0]
        )
        arr: Array[Int] = _create_single_arg_case_arr(end=end)
        return arr

    if len(args) == 2:
        start: Int = to_apysc_val_from_builtin.get_copied_int_from_builtin_val(
            integer=args[0]
        )
        end = to_apysc_val_from_builtin.get_copied_int_from_builtin_val(integer=args[1])
        arr = _create_double_args_case_arr(start=start, end=end)
        return arr

    start = to_apysc_val_from_builtin.get_copied_int_from_builtin_val(integer=args[0])
    end = to_apysc_val_from_builtin.get_copied_int_from_builtin_val(integer=args[1])
    step: Int = to_apysc_val_from_builtin.get_copied_int_from_builtin_val(
        integer=args[2]
    )
    arr = _create_triple_args_case_arr(start=start, end=end, step=step)
    return arr


def _create_triple_args_case_arr(*, start: Int, end: Int, step: Int) -> Array[Int]:
    """
    Create a triple arguments case array.

    Parameters
    ----------
    start : Int
        A start position argument.
    end : Int
        An end position argument.
    step : Int
        A step number argument.

    Returns
    -------
    arr : Array[Int]
        A created array of integers.
    """
    from apysc._expression import expression_data_util

    arr: Array[Int] = Array([])
    expression: str = (
        f"for (var i = {start.variable_name}; i < {end.variable_name}; "
        f"i += {step.variable_name}) {{"
        f"\n  {arr.variable_name}.push(i);"
        "\n}"
    )
    expression_data_util.append_js_expression(expression=expression)
    return arr


def _create_double_args_case_arr(*, start: Int, end: Int) -> Array[Int]:
    """
    Create a double arguments case array.

    Parameters
    ----------
    start : Int
        A start position argument.
    end : Int
        An end position argument.

    Returns
    -------
    arr : Array[Int]
        A created array of integers.
    """
    from apysc._expression import expression_data_util

    arr: Array[Int] = Array([])
    expression: str = (
        f"for (var i = {start.variable_name}; i < {end.variable_name}; i++) {{"
        f"\n  {arr.variable_name}.push(i);"
        "\n}"
    )
    expression_data_util.append_js_expression(expression=expression)
    return arr


def _create_single_arg_case_arr(*, end: Int) -> Array[Int]:
    """
    Create a single argument case array.

    Parameters
    ----------
    end : Int
        An end position argument.

    Returns
    -------
    arr : Array[Int]
        A created array of integers.
    """
    from apysc._expression import expression_data_util

    arr: Array[Int] = Array([])
    expression: str = (
        f"for (var i = 0; i < {end.variable_name}; i++) {{"
        f"\n  {arr.variable_name}.push(i);"
        "\n}"
    )
    expression_data_util.append_js_expression(expression=expression)
    return arr
