"""The implementation of manipulating HTL and js expression files.
"""

import shutil

EXPRESSION_ROOT_DIR: str = './.action_py_script_expression/'


def empty_expression_dir() -> None:
    """Remove expression directory (EXPRESSION_ROOT_DIR) to initialize.
    """
    shutil.rmtree(EXPRESSION_ROOT_DIR, ignore_errors=True)
