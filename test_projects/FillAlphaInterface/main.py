"""Test project for FillAlphaInterface class.

Command examples:
$ python test_projects/FillAlphaInterface/main.py
$ python FillAlphaInterface/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from apyscript.console.assertion import assert_equal
from apyscript.display import Sprite
from apyscript.display.rectangle import Rectangle
from apyscript.display.stage import Stage
from apyscript.file import file_util
from apyscript.html import exporter
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
    sprite_1.graphics.begin_fill(color='#aaa', alpha=0.5)
    rectangle: Rectangle = sprite_1.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    fill_alpha_1: Number = rectangle.fill_alpha
    assert_equal(
        expected=0.5, actual=fill_alpha_1)
    rectangle.fill_alpha = Number(0.3)
    fill_alpha_2: Number = rectangle.fill_alpha
    assert_equal(
        expected=0.3, actual=fill_alpha_2)

    exporter.save_expressions_overall_html(
        dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
