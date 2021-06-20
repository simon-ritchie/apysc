"""Test project for `assert_defined` and `assert_undefined` interfaces.

Command examples:
$ python test_projects/assert_defined/main.py
$ python assert_defined/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from apysc import Int
from apysc import Sprite
from apysc import Stage
from apysc import assert_defined
from apysc import assert_undefined
from apysc import save_overall_html
from apysc import DisplayObject
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
    stage: Stage = Stage(background_color='#333')

    int_1: Int = Int(3)
    assert_defined(actual=int_1)

    sprite_1: Sprite = Sprite(stage=stage)
    child_1: DisplayObject = sprite_1.get_child_at(index=0)
    assert_undefined(actual=child_1)

    save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
