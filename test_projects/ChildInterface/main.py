"""Test project for ChildInterface class.

Command examples:
$ python test_projects/ChildInterface/main.py
$ python ChildInterface/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from apyscript.console.assertion import assert_not_equal, assert_true
from apyscript.console.assertion import assert_false
from apyscript.display import Sprite
from apyscript.display.rectangle import Rectangle
from apyscript.display.stage import Stage
from apyscript.file import file_util
from apyscript.html import exporter
from apyscript.type import Int, Boolean
from apyscript.type import Number

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

    exporter.save_expressions_overall_html(
        dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
