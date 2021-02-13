"""Common indentation related utility implementations.
"""


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
    spaces: str = ' ' * (indent_num * 2)
    return spaces
