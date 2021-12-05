"""Test project for `Elif` class.

Command examples:
$ python test_projects/Elif/main.py
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
    condition_1: ap.Boolean = ap.Boolean(False)
    condition_2: ap.Boolean = ap.Boolean(True)
    with ap.If(condition_1, locals_=locals(), globals_=globals()):
        int_1 += 10
    with ap.Elif(condition_2, locals_=locals(), globals_=globals()):
        int_1 += 50
    ap.assert_equal(expected=60, actual=int_1)

    int_2: ap.Int = ap.Int(10)
    with ap.If(condition_1, locals_=locals(), globals_=globals()):
        int_2 += 10
    with ap.Elif(condition_1, locals_=locals(), globals_=globals()):
        int_2 += 50
    ap.assert_equal(expected=10, actual=int_2)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
