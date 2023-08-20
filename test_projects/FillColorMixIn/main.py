"""Test project for FillColorMixIn class.

Command examples:
$ python test_projects/FillColorMixIn/main.py
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
    stage: ap.Stage = ap.Stage(background_color=ap.Color("#333"))
    sprite_1: ap.Sprite = ap.Sprite()
    stage.add_child(sprite_1)
    rectangle_1: ap.Rectangle = sprite_1.graphics.draw_rect(
        x=50, y=50, width=50, height=50
    )
    rectangle_1.fill_color = ap.Color("#999")
    color_1: ap.Color = rectangle_1.fill_color
    ap.assert_equal(left=ap.Color("#999999"), right=color_1)
    color_1._value.value = "#666666"
    color_2: ap.Color = rectangle_1.fill_color
    ap.assert_not_equal(left=color_1, right=color_2)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
