"""Test project for FillColorInterface class.

Command examples:
$ python test_projects/FillColorInterface/main.py
$ python FillColorInterface/main.py
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
    rectangle_1: ap.Rectangle = sprite_1.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    string_1: ap.String = ap.String('#999')
    rectangle_1.fill_color = string_1
    string_2: ap.String = rectangle_1.fill_color
    ap.assert_equal(expected='#999999', actual=string_2)
    string_2.value = '#666666'
    string_3: ap.String = rectangle_1.fill_color
    ap.assert_not_equal(expected=string_2, actual=string_3)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
