"""Test project for `assert_defined` and `assert_undefined` interfaces.

Command examples:
$ python test_projects/assert_defined/main.py
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
    """
    Entry point of this test project.
    """
    stage: ap.Stage = ap.Stage(background_color='#333')

    int_1: ap.Int = ap.Int(3)
    ap.assert_defined(value=int_1)

    sprite_1: ap.Sprite = ap.Sprite(stage=stage)
    child_1: ap.DisplayObject = sprite_1.get_child_at(index=0)
    ap.assert_undefined(value=child_1)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
