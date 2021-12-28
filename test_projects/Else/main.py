"""Test project for `Else` class.

Command examples:
$ python test_projects/Else/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

import apysc as ap
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


def main() -> None:
    """Entry point of this test project.
    """
    _: ap.Stage = ap.Stage(background_color='#333')

    int_1: ap.Int = ap.Int(10)
    with ap.If(int_1 == 20, locals_=locals(), globals_=globals()):
        int_1.value = 100
    with ap.Else(locals_=locals(), globals_=globals()):
        ap.assert_equal(left=10, right=int_1)
        int_1.value = 300
    ap.assert_equal(left=300, right=int_1)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
