"""Implementations of expression's indent number related interfaces.
"""

import os


def get_current_indent_num() -> int:
    """
    Get a current indent number.

    Returns
    -------
    current_indent_num : int
        Current indent number.
    """
    from apysc.expression import expression_file_util
    from apysc.file import file_util
    INDENT_NUM_FILE_PATH: str = expression_file_util.INDENT_NUM_FILE_PATH
    if not os.path.isfile(INDENT_NUM_FILE_PATH):
        return 0
    indent_num_txt: str = file_util.read_txt(file_path=INDENT_NUM_FILE_PATH)
    indent_num_txt = indent_num_txt.strip()
    if indent_num_txt == '':
        return 0
    current_indent_num: int = int(indent_num_txt)
    return current_indent_num


def increment() -> None:
    pass
