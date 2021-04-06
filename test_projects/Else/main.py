"""Test project for `Else` class.

Command examples:
$ python test_projects/Else/main.py
$ python Else/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from apysc import Else
from apysc import If
from apysc import assert_equal
from apysc import Stage
from apysc.file import file_util
from apysc.html import exporter
from apysc import Int

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
    with If(int_1 == 20, locals(), globals()):
        int_1.value = 100
    with Else(locals(), globals()):
        assert_equal(expected=10, actual=int_1)
        int_1.value = 300
    assert_equal(expected=300, actual=int_1)

    exporter.save_expressions_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
