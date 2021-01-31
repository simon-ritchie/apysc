"""The implementation of manipulating HTL and js expression files.
"""

import os
import shutil
from typing import Optional

EXPRESSION_ROOT_DIR: str = './.action_py_script_expression/'


def empty_expression_dir() -> None:
    """Remove expression directory (EXPRESSION_ROOT_DIR) to initialize.
    """
    shutil.rmtree(EXPRESSION_ROOT_DIR, ignore_errors=True)
    os.makedirs(EXPRESSION_ROOT_DIR, exist_ok=True)


ROOT_SCOPE: str = 'root'


def append_expression(expression: str, scope: Optional[str] = None) -> None:
    """
    Append html and js expression to specified scope's file.

    Parameters
    ----------
    expression : str
        HTML and js Expression string.
    scope : str, optional
        Target scope name. If skipped, this will be root scope.
    """
    if scope is None:
        scope = ROOT_SCOPE
    if not scope.endswith('.html'):
        scope += '.html'
    scope_file_path: str = os.path.join(EXPRESSION_ROOT_DIR, scope)
    with open(scope_file_path, 'a') as f:
        f.write(f'{expression}\n')
