"""Test project for line_joints setting.

Command examples:
$ python test_projects/line_joints/main.py
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
    ap.Stage(
        background_color='#111',
        stage_width=1000, stage_height=500)
    sprite: ap.Sprite = ap.Sprite()
    sprite.graphics.line_style(color='#0af', thickness=10)
    sprite.graphics.move_to(x=50, y=100)
    sprite.graphics.line_to(x=80, y=20)
    sprite.graphics.line_to(x=110, y=100)

    sprite.graphics.line_style(
        color='#0af', thickness=10, joints=ap.LineJoints.ROUND)
    sprite.graphics.move_to(x=140, y=100)
    sprite.graphics.line_to(x=170, y=20)
    sprite.graphics.line_to(x=200, y=100)

    sprite.graphics.line_style(
        color='#0af', thickness=10, joints=ap.LineJoints.BEVEL)
    polyline: ap.Polyline = sprite.graphics.move_to(x=230, y=100)
    sprite.graphics.line_to(x=260, y=20)
    sprite.graphics.line_to(x=290, y=100)
    polyline.click(on_polyline_click)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_polyline_click(
        e: ap.MouseEvent[ap.Polyline], options: dict) -> None:
    """
    Handler that called when polyline is clicked.

    Parameters
    ----------
    e : MouseEvent
        Created MouseEvent instance.
    options : dict
        Optional parameters.
    """
    polyline: ap.Polyline = e.this
    polyline.line_joints = ap.LineJoints.ROUND


if __name__ == '__main__':
    main()
