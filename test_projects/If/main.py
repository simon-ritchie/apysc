"""Test project for `If` class.

Command examples:
$ python test_projects/If/main.py
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
    condition_1: ap.Boolean = ap.Boolean(True)
    with ap.If(condition_1, locals_=locals(), globals_=globals()):
        int_1 += 10
    ap.assert_equal(expected=20, actual=int_1)

    condition_2: ap.Boolean = ap.Boolean(False)
    with ap.If(condition_2, locals_=locals(), globals_=globals()):
        int_1 += 10
    ap.assert_equal(expected=20, actual=int_1)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
