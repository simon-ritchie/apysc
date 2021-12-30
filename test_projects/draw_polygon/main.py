"""Test project for draw_polygon interface.

Command examples:
$ python test_projects/draw_polygon/main.py
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
        background_color='#333',
        stage_width=1000, stage_height=500)
    sprite: ap.Sprite = ap.Sprite()
    sprite.graphics.begin_fill(color='#0af')
    sprite.graphics.line_style(
        color='#fff', thickness=10, joints=ap.LineJoints.BEVEL)
    _: ap.Polygon = sprite.graphics.draw_polygon(
        points=[
            ap.Point2D(50, 50), ap.Point2D(150, 50), ap.Point2D(100, 100)])

    sprite.graphics.line_style(
        color='#fff',
        round_dot_setting=ap.LineRoundDotSetting(round_size=6, space_size=5))
    polygon_2: ap.Polygon = sprite.graphics.draw_polygon(
        points=[
            ap.Point2D(200, 50), ap.Point2D(300, 50), ap.Point2D(250, 100)])
    polygon_2.click(on_polygon_click)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


def on_polygon_click(
        e: ap.MouseEvent[ap.Polygon], options: dict) -> None:
    """
    Handler that called when polygon is clicked.

    Parameters
    ----------
    e : MouseEvent
        Created MouseEvent instance.
    options : dict
        Optional parameters.
    """
    polygon: ap.Polygon = e.this
    polygon.line_round_dot_setting = None


if __name__ == '__main__':
    main()
