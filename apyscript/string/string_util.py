"""Common string utilities.
"""


def escape_str(string: str) -> str:
    """
    Escape special characters (e.g. line breaks of `\n`).

    Parameters
    ----------
    string : str
        String to escape.

    Returns
    -------
    string : str
        Escaped string.
    """
    string = repr(string)[1:-1]
    return string
