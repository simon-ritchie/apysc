"""Common indentation related utility implementations.
"""

from apyscript.validation import number_validation


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
    number_validation.validate_integer(integer=indent_num)
    number_validation.validate_num_is_gte_zero(num=indent_num)
    spaces: str = ' ' * (indent_num * 2)
    return spaces
