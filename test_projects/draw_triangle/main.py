"""The test project for the `draw_triangle` method interface.

Command examples:
$ python test_projects/draw_triangle/main.py
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
    _: ap.Stage = ap.Stage(
        background_color="#333",
        stage_width=1200,
        stage_height=900,
    )

    sprite: ap.Sprite = ap.Sprite()
    sprite.graphics.begin_fill(color="#0af", alpha=0.5)
    sprite.graphics.line_style(color="#fff", thickness=3, alpha=0.3)
    sprite.graphics.draw_triangle(
        x1=200,
        y1=50,
        x2=100,
        y2=250,
        x3=300,
        y3=250,
    )
    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
