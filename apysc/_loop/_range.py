"""The implementation for the `range` function.
"""

from typing import Optional, Union, Any

from apysc._type.int import Int
from apysc._type.array import Array
from apysc._validation import arg_validation_decos


@arg_validation_decos.variadic_args_len_is_between(min_length=1, max_length=3)
@arg_validation_decos.all_variadic_args_are_integers(optional=False)
def range(*args: Any) -> Array[Int]:
    """
    Create an array of integers from `start` to `end` - 1.

    Returns
    -------
    arr : Array[Int]
        A create array.
    """
    from apysc._converter import to_apysc_val_from_builtin

    if len(args) == 1:
        end: Int = to_apysc_val_from_builtin.get_copied_int_from_builtin_val(
            integer=args[0]
        )
        arr: Array[Int] = _create_single_arg_case_arr(end=end)
        return arr
    pass


def _create_single_arg_case_arr(*, end: Int) -> Array[Int]:
    """
    Create a single argument case's array.

    Parameters
    ----------
    end : Int
        An end position argument.

    Returns
    -------
    arr : Array[Int]
        A created array of integers.
    """
    import apysc as ap

    arr: Array[Int] = Array([])
    expression: str = (
        f"for (var i = 0; i < {end.variable_name}; i++) {{"
        f"\n  {arr.variable_name}.push(i);"
        "\n}"
    )
    ap.append_js_expression(expression=expression)
    return arr
