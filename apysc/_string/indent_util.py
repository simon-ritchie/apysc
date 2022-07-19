"""Common indentation related utility implementations.

Mainly following interfaces are defined:

- make_spaces_for_html: Make spaces that multiply 2 to
    a specified indentation number.
- append_spaces_to_expression: Append spaces to a expression string.
"""


from typing import List

from apysc._validation import arg_validation_decos


@arg_validation_decos.is_builtin_integer(arg_position_index=0)
@arg_validation_decos.num_is_gte_zero(arg_position_index=0)
def make_spaces_for_html(*, indent_num: int) -> str:
    """
    Make spaces that multiply 2 to a specified indentation number.

    Parameters
    ----------
    indent_num : int
        Indentation number.

    Returns
    -------
    spaces : str
        Result spaces string.
    """
    spaces: str = " " * (indent_num * 2)
    return spaces


def append_spaces_to_expression(*, expression: str, indent_num: int) -> str:
    """
    Append spaces to a js expression string.

    Parameters
    ----------
    expression : str
        JavaScript expression string to add spaces.
    indent_num : int
        Indentation number. If 1 is specified, spaces become 2.

    Returns
    -------
    expression : str
        Expression string after adding spaces.
    """
    if indent_num == 0:
        return expression
    lines: List[str] = expression.splitlines()
    spaces: str = make_spaces_for_html(indent_num=indent_num)
    for i, line in enumerate(lines):
        lines[i] = f"{spaces}{line}"
    expression = "\n".join(lines)
    return expression
