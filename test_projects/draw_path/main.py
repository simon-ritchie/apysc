"""The test project for the draw_path interface.

Command examples:
$ python test_projects/draw_path/main.py
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
    stage: ap.Stage = ap.Stage(
        background_color='#333',
        stage_width=1000, stage_height=500, stage_elem_id='stage')

    sprite: ap.Sprite = ap.Sprite(stage=stage)
    sprite.graphics.line_style(color='#fff', thickness=5)

    # Test pattern for the MoveTo, LineTo, Horizontal, Vertical,
    # and Close (with absolute coordinates).
    sprite.graphics.draw_path(
        path_data_list=[
            ap.PathData.MoveTo(x=50, y=50),
            ap.PathData.LineTo(x=100, y=100),
            ap.PathData.Horizontal(x=150),
            ap.PathData.Vertical(y=50),
            ap.PathData.Close(),
        ])

    # Test pattern for the fill color setting and 2D bezier curve.
    sprite.graphics.begin_fill(color='#0af')
    sprite.graphics.draw_path(
        path_data_list=[
            ap.PathData.MoveTo(x=200, y=100),
            ap.PathData.Bezier2D(
                control_x=250, control_y=50, dest_x=300, dest_y=100),
            ap.PathData.Bezier2DContinual(
                x=400, y=100),
        ])

    # Test pattern for the 3D bezier curve.
    sprite.graphics.draw_path(
        path_data_list=[
            ap.PathData.MoveTo(x=450, y=100),
            ap.PathData.Bezier3D(
                control_x1=450,
                control_y1=50,
                control_x2=500,
                control_y2=50,
                dest_x=550,
                dest_y=100),
            ap.PathData.Bezier3DContinual(
                control_x=650,
                control_y=150,
                dest_x=650,
                dest_y=100),
        ])

    # Test pattern for the relative coordinates setting.
    sprite.graphics.draw_path(
        path_data_list=[
            ap.PathData.MoveTo(x=50, y=200),
            ap.PathData.LineTo(x=50, y=50, relative=True),
            ap.PathData.Horizontal(x=50, relative=True),
            ap.PathData.Vertical(y=-50, relative=True),
            ap.PathData.Close(),
        ])

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == '__main__':
    main()
