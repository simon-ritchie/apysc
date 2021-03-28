"""Test project for `Elif` class.

Command examples:
$ python test_projects/Elif/main.py
$ python Elif/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from apysc.branch import If, Elif
from apysc.console import assert_equal
from apysc.display import Stage
from apysc.file import file_util
from apysc.html import exporter
from apysc.type import Boolean
from apysc.type import Int

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
    condition_1: Boolean = Boolean(False)
    condition_2: Boolean = Boolean(True)
    with If(condition_1, locals(), globals()):
        int_1 += 10
    with Elif(condition_2, locals(), globals()):
        int_1 += 50
    assert_equal(expected=60, actual=int_1)

    int_2: Int = Int(10)
    with If(condition_1, locals(), globals()):
        int_2 += 10
    with Elif(condition_1, locals(), globals()):
        int_2 += 50
    assert_equal(expected=10, actual=int_2)

    exporter.save_expressions_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
