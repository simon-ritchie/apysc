"""The test project for the Rectangle class's VariableNameSuffixMixIn.

Command examples:
$ python test_projects/RectangleVariableNameSuffixMixIn/main.py
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
    ap.Stage(
        background_color="#333",
        stage_width=1000,
        stage_height=500,
        stage_elem_id="stage",
        variable_name_suffix="stage",
    )

    ap.Rectangle(
        x=50,
        y=50,
        width=50,
        height=50,
        fill_color="#0af",
        variable_name_suffix="rectangle_1",
    )

    sprite: ap.Sprite = ap.Sprite(variable_name_suffix="sprite_1")
    sprite.graphics.begin_fill(color="#f0a", alpha=0.5)
    sprite.graphics.line_style(color="#fff", thickness=3, alpha=0.7)
    sprite.graphics.draw_rect(
        x=50, y=50, width=50, height=50, variable_name_suffix="rectangle_2"
    )

    sprite.graphics.draw_round_rect(
        x=50,
        y=50,
        width=50,
        height=50,
        ellipse_width=10,
        ellipse_height=10,
        variable_name_suffix="rectangle_3",
    )

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
