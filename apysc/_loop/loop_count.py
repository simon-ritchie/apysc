"""Implementations for the count of the current loop number
(the For or the other loop class nested number).
"""

import os


def get_current_loop_count() -> int:
    """
    Get the current loop count number.

    Returns
    -------
    loop_count : int
        Current loop count.
    """
    from apysc._expression import expression_file_util
    file_path: str = expression_file_util.LOOP_COUNT_FILE_PATH
    if not os.path.isfile(file_path):
        return 0
    with open(file_path, 'r') as f:
        file_str: str = f.read()
    if file_str == '':
        return 0
    loop_count: int = int(file_str)
    return loop_count


def increment_current_loop_count() -> None:
    """
    Increment the current loop count number.
    """
    from apysc._expression import expression_file_util
    file_path: str = expression_file_util.LOOP_COUNT_FILE_PATH
    current_loop_count: int = get_current_loop_count()
    with open(file_path, 'w') as f:
        f.write(str(current_loop_count + 1))


def decrement_current_loop_count() -> None:
    """
    Decrement the current loop count number.
    """
    from apysc._expression import expression_file_util
    file_path: str = expression_file_util.LOOP_COUNT_FILE_PATH
    current_loop_count: int = get_current_loop_count()
    current_loop_count -= 1
    current_loop_count = max(0, current_loop_count)
    with open(file_path, 'w') as f:
        f.write(str(current_loop_count))
