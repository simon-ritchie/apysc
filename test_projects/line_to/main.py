"""Test project for line_to interface.

Command examples:
$ python test_projects/line_to/main.py
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
    ap.Stage(background_color=ap.Color("#111"), stage_width=1000, stage_height=500)

    sprite: ap.Sprite = ap.Sprite()
    sprite.graphics.begin_fill(color=ap.Color("#0af"), alpha=0.5)
    sprite.graphics.line_style(color=ap.Color("#eee"), thickness=4, alpha=0.75)
    polyline_1: ap.Polyline = sprite.graphics.line_to(x=100, y=0)
    ap.assert_equal(polyline_1.x, 0)
    ap.assert_equal(polyline_1.y, 0)
    sprite.graphics.line_to(x=100, y=100)
    sprite.graphics.line_to(x=-30, y=-40)
    ap.assert_equal(polyline_1.x, -30)
    ap.assert_equal(polyline_1.y, -40)

    sprite.graphics.begin_fill(color=ap.Color("#f0a"), alpha=0.5)
    sprite.graphics.move_to(x=100, y=100)
    sprite.graphics.line_to(x=100, y=200)
    sprite.graphics.line_to(x=200, y=200)
    sprite.graphics.line_to(x=100, y=100)

    sprite.graphics.move_to(x=ap.Number(0), y=ap.Number(0))
    sprite.graphics.line_to(x=ap.Number(100), y=ap.Number(0))
    polyline: ap.Polyline = sprite.graphics.line_to(x=ap.Number(100), y=ap.Number(100))
    polyline.x = ap.Number(200)
    polyline.y = ap.Number(200)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
