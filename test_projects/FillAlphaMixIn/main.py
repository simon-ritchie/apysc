"""Test project for FillAlphaMixIn class.

Command examples:
$ python test_projects/FillAlphaMixIn/main.py
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
    ap.Stage(background_color=ap.Color("#333"))
    sprite_1: ap.Sprite = ap.Sprite()
    sprite_1.graphics.begin_fill(color=ap.Color("#aaa"), alpha=0.5)
    rectangle: ap.Rectangle = sprite_1.graphics.draw_rect(
        x=50, y=50, width=50, height=50
    )
    fill_alpha_1: ap.Number = rectangle.fill_alpha
    ap.assert_equal(left=0.5, right=fill_alpha_1)
    rectangle.fill_alpha = ap.Number(0.3)
    fill_alpha_2: ap.Number = rectangle.fill_alpha
    ap.assert_equal(left=0.3, right=fill_alpha_2)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == "__main__":
    main()
