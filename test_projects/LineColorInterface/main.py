"""Test project for LineColorInterface class.

Command examples:
$ python test_projects/LineColorInterface/main.py
$ python LineColorInterface/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from apysc.console import assert_equal
from apysc.console import assert_not_equal
from apysc.display import Rectangle
from apysc.display import Sprite
from apysc.display import Stage
from apysc.file import file_util
from apysc.html import exporter
from apysc.type import String

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
    rectangle: Rectangle = sprite_1.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    rectangle.line_color = String('#aaa')
    assert_equal(expected='#aaaaaa', actual=rectangle.line_color)

    string_1: String = rectangle.line_color
    string_1.value = '#bbb'
    assert_not_equal(expected=rectangle.line_color, actual=string_1)

    exporter.save_expressions_overall_html(
        dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
