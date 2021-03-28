"""Common indentation related utility implementations.

Mainly following interfaces are defined:

- make_spaces_for_html: Make spaces that multiplied 2 to
    specified indentation number.
- append_spaces_to_expression: Append spaces to a expression string.
"""


from typing import List


def make_spaces_for_html(indent_num: int) -> str:
    """
    Make spaces that multiplied 2 to specified indentation number.

    Parameters
    ----------
    indent_num : int
        Indentation number.

    Returns
    -------
    spaces : str
        Result spaces string.
    """
    from apysc.validation import number_validation
    number_validation.validate_integer(integer=indent_num)
    number_validation.validate_num_is_gte_zero(num=indent_num)
    spaces: str = ' ' * (indent_num * 2)
    return spaces


def append_spaces_to_expression(expression: str, indent_num: int) -> str:
    """
    Append spaces to a expression string.

    Notes
    -----
    Only script section will be appended spaces, skipped html section.

    Parameters
    ----------
    expression : str
        Expression string to add spaces to.
    indent_num : int
        Indentation number. If 1 is specified, then spaces will be 2.

    Returns
    -------
    expression : str
        Expression string after adding spaces.
    """
    from apysc.html.html_util import ScriptLineUtil
    script_line_util: ScriptLineUtil = ScriptLineUtil(html=expression)
    if indent_num == 0:
        return expression
    lines: List[str] = expression.splitlines()
    spaces: str = make_spaces_for_html(indent_num=indent_num)
    for i, line in enumerate(lines):
        line_number: int = i + 1
        if not script_line_util.is_script_line(line_number=line_number):
            continue
        lines[i] = f'{spaces}{line}'
    expression = '\n'.join(lines)
    return expression
