"""Test project for `If` class.

Command examples:
$ python test_projects/If/main.py
$ python If/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from apysc import Boolean
from apysc import If
from apysc import Int
from apysc import Stage
from apysc import assert_equal
from apysc.file import file_util
from apysc.html import exporter

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


def main() -> None:
    """Entry point of this test project.
    """
    _: Stage = Stage(background_color='#333')

    int_1: Int = Int(10)
    condition_1: Boolean = Boolean(True)
    with If(condition_1, locals(), globals()):
        int_1 += 10
    assert_equal(expected=20, actual=int_1)

    condition_2: Boolean = Boolean(False)
    with If(condition_2, locals(), globals()):
        int_1 += 10
    assert_equal(expected=20, actual=int_1)

    exporter.save_expressions_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
