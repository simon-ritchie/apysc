"""Test project for ChildInterface class.

Command examples:
$ python test_projects/ChildInterface/main.py
$ python ChildInterface/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from apysc import Boolean
from apysc import Int
from apysc import Sprite
from apysc import Stage
from apysc import assert_defined
from apysc import assert_equal
from apysc import assert_false
from apysc import assert_true
from apysc import assert_undefined
from apysc.display.display_object import DisplayObject
from apysc.file import file_util
from apysc.html import exporter

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
    sprite_1: Sprite = Sprite(stage=stage)
    stage.add_child(sprite_1)
    sprite_2: Sprite = Sprite(stage=stage)
    sprite_1.add_child(sprite_2)
    bool_1: Boolean = stage.contains(child=sprite_1)
    assert_true(actual=bool_1)
    bool_2: Boolean = sprite_1.contains(child=sprite_2)
    assert_true(actual=bool_2)
    bool_3: Boolean = stage.contains(child=sprite_2)
    assert_false(actual=bool_3)

    num_children: Int = sprite_1.num_children
    assert_equal(expected=1, actual=num_children)

    child_1: DisplayObject = sprite_1.get_child_at(index=0)
    assert_defined(actual=child_1)
    child_2: DisplayObject = sprite_1.get_child_at(index=1)
    assert_undefined(actual=child_2)

    exporter.save_overall_html(
        dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
