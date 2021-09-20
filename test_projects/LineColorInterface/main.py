"""Test project for LineColorInterface class.

Command examples:
$ python test_projects/LineColorInterface/main.py
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
    rectangle: ap.Rectangle = sprite_1.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    rectangle.line_color = ap.String('#aaa')
    ap.assert_equal(expected='#aaaaaa', actual=rectangle.line_color)

    string_1: ap.String = rectangle.line_color
    string_1.value = '#bbb'
    ap.assert_not_equal(expected=rectangle.line_color, actual=string_1)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
