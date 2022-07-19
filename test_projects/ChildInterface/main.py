"""Test project for ChildInterface class.

Command examples:
$ python test_projects/ChildInterface/main.py
"""

import sys

sys.path.append("./")

import os
from types import ModuleType

import apysc as ap
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module), "test_output/"
)


def main() -> None:
    """
    Entry point of this test project.
    """
    stage: ap.Stage = ap.Stage(background_color="#333")
    sprite_1: ap.Sprite = ap.Sprite()
    stage.add_child(sprite_1)
    sprite_2: ap.Sprite = ap.Sprite()
    sprite_1.add_child(sprite_2)
    bool_1: ap.Boolean = stage.contains(child=sprite_1)
    ap.assert_true(value=bool_1, msg="assertion_0001")
    bool_2: ap.Boolean = sprite_1.contains(child=sprite_2)
    ap.assert_true(value=bool_2, msg="assertion_0002")
    bool_3: ap.Boolean = stage.contains(child=sprite_2)
    ap.assert_false(value=bool_3, msg="assertion_0003")

    num_children: ap.Int = sprite_1.num_children
    ap.assert_equal(left=2, right=num_children, msg="assertion_0101")

    child_1: ap.DisplayObject = sprite_1.get_child_at(index=0)
    ap.assert_defined(value=child_1, msg="assertion_0201")
    child_2: ap.DisplayObject = sprite_1.get_child_at(index=2)
    ap.assert_undefined(value=child_2, msg="assertion_0202")

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
