"""A test project for the Polyline class's VariableNameSuffixMixIn.

Command examples:
$ python test_projects/PolylineVariableNameSuffixMixIn/main.py
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

    ap.Polyline(
        points=[
            ap.Point2D(50, 50, variable_name_suffix="polyline_1_point_1"),
            ap.Point2D(50, 100, variable_name_suffix="polyline_1_point_2"),
            ap.Point2D(100, 100, variable_name_suffix="polyline_1_point_3"),
        ],
        line_color="#0af",
        line_thickness=3,
        variable_name_suffix="polyline_1",
    )

    sprite: ap.Sprite = ap.Sprite(variable_name_suffix="sprite_1")
    sprite.graphics.line_style(color="#fff", thickness=3, alpha=0.7)
    sprite.graphics.move_to(x=50, y=150, variable_name_suffix="polyline_2")
    sprite.graphics.line_to(x=50, y=200, variable_name_suffix="polyline_2")
    sprite.graphics.line_to(x=100, y=200, variable_name_suffix="polyline_2")

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
