from random import randint
import os
import shutil
from types import ModuleType
from typing import List

from retrying import retry

from apysc._lint_and_doc import docstring_to_markdown_converter
from apysc._file import file_util, module_util


_MODULE_STR: str = \
'''"""Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

Notes
-----
Ut enim ad minim veniam, quis nostrud exercitation ullamco
laboris nisi ut aliquip ex ea commodo consequat.

References
----------
- Duis aute irure dolor in reprehenderit in voluptate
    - https://simon-ritchie.github.io/apysc/test_doc_1.html
- Velit esse cillum dolore eu fugiat nulla pariatur
    - https://simon-ritchie.github.io/apysc/test_doc_2.html
"""

import os


def sample_func_1(a: int, b: bool) -> str:
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    sed do eiusmod tempor incididunt ut labore et dolore
    magna aliqua.

    Parameters
    ----------
    a : int
        cupidatat non proident, sunt in culpa qui officia
        deserunt mollit anim id est laborum.
    b : bool
        At vero eos et accusamus et iusto odio dignissimos.

    Returns
    -------
    c : str
        Lorem ipsum dolor sit amet, consectetur adipiscing elit,
        sed do eiusmod tempor incididunt.
    d : float
        cupidatat non proident, sunt in culpa qui officia
        deserunt mollit anim id est laborum.

    Notes
    -----
    Duis aute irure dolor in reprehenderit in voluptate.

    - Cupidatat non proident, sunt in culpa qui officia.
    - Deserunt mollit anim id est laborum.

    Examples
    --------
    >>> a: int = 10
    >>> b: int = a + 20
    >>> b
    30

    References
    ----------
    - Duis aute irure dolor in reprehenderit in voluptate
        - https://simon-ritchie.github.io/apysc/test_doc_3.html
    - Velit esse cillum dolore eu fugiat nulla pariatur
        - https://simon-ritchie.github.io/apysc/test_doc_4.html
    """
    ...


class _SampleClass:
    """Cupidatat non proident, sunt in culpa qui officia
    deserunt mollit anim id est laborum.
    """

    def __init__(self) -> None:
        """Cupidatat non proident, sunt in culpa qui officia
        deserunt mollit anim id est laborum.
        """
        ...

    def sample_method_1(self, e: int) -> str:
        """
        Cupidatat non proident, sunt in culpa qui officia.

        Parameters
        ----------
        e : int
            Lorem ipsum dolor sit amet, consectetur adipiscing
            elit, sed do eiusmod tempor incididunt.

        Returns
        -------
        d : str
            Velit esse cillum dolore eu fugiat nulla pariatur.
        """
        ...
'''

_TEST_MODULE_DIR_PATH: str = './tmp/test_docstring_to_markdown_converter/'
_TEST_MODULE_PATH: str = os.path.join(
    _TEST_MODULE_DIR_PATH, 'test_module_1.py'
)


def _save_test_module() -> None:
    """Save the test module.
    """
    os.makedirs(_TEST_MODULE_DIR_PATH, exist_ok=True)
    init_path: str = os.path.join(_TEST_MODULE_DIR_PATH, '__init__.py')
    file_util.save_plain_txt(txt='', file_path=init_path)
    file_util.save_plain_txt(
        txt=_MODULE_STR, file_path=_TEST_MODULE_PATH)


def _remove_test_module_dir() -> None:
    """Remove the test modules directory.
    """
    shutil.rmtree(_TEST_MODULE_DIR_PATH, ignore_errors=True)


def teardown() -> None:
    _remove_test_module_dir()


# @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__append_module_docstring_to_markdown() -> None:
    _save_test_module()
    markdown: str = docstring_to_markdown_converter.\
        _append_module_docstring_to_markdown(
            markdown='', module_docstring=None)
    assert markdown == ''

    module: ModuleType = module_util.read_target_path_module(
        module_path=_TEST_MODULE_PATH)
    markdown = docstring_to_markdown_converter.\
        _append_module_docstring_to_markdown(
            markdown='# Test module docstring',
            module_docstring=module.__doc__)
    expected_strs: List[str] = [
        '# Test module docstring\n\n',
        '## Module summary\n\n'
        'Lorem ipsum dolor sit amet, consectetur adipiscing '
        'elit, sed do eiusmod tempor incididunt ut labore et '
        'dolore magna aliqua.<hr>\n\n',
        '**[Notes]**\n\n',
        '**[References]**\n\n',
    ]
    for expected_str in expected_strs:
        assert expected_str in markdown
    _remove_test_module_dir()
