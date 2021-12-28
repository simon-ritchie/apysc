"""Test project for ChildInterface class.

Command examples:
$ python test_projects/ChildInterface/main.py
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
    sprite_1: ap.Sprite = ap.Sprite(stage=stage)
    stage.add_child(sprite_1)
    sprite_2: ap.Sprite = ap.Sprite(stage=stage)
    sprite_1.add_child(sprite_2)
    bool_1: ap.Boolean = stage.contains(child=sprite_1)
    ap.assert_true(value=bool_1)
    bool_2: ap.Boolean = sprite_1.contains(child=sprite_2)
    ap.assert_true(value=bool_2)
    bool_3: ap.Boolean = stage.contains(child=sprite_2)
    ap.assert_false(value=bool_3)

    num_children: ap.Int = sprite_1.num_children
    ap.assert_equal(left=1, right=num_children)

    child_1: ap.DisplayObject = sprite_1.get_child_at(index=0)
    ap.assert_defined(value=child_1)
    child_2: ap.DisplayObject = sprite_1.get_child_at(index=1)
    ap.assert_undefined(value=child_2)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
