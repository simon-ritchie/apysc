"""Test project for draw_polygon interface.

Command examples:
$ python test_projects/draw_polygon/main.py
$ python draw_polygon/main.py
"""

import sys
from typing import Any
from typing import Dict

sys.path.append('./')

import os
from types import ModuleType

from apysc import LineJoints
from apysc import LineRoundDotSetting
from apysc import MouseEvent
from apysc import Point2D
from apysc import Polygon
from apysc import Sprite
from apysc import Stage
from apysc import save_overall_html
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
    stage: Stage = Stage(
        background_color='#333',
        stage_width=1000, stage_height=500)
    sprite: Sprite = Sprite(stage=stage)
    sprite.graphics.begin_fill(color='#0af')
    sprite.graphics.line_style(
        color='#fff', thickness=10, joints=LineJoints.BEVEL)
    _: Polygon = sprite.graphics.draw_polygon(
        points=[Point2D(50, 50), Point2D(150, 50), Point2D(100, 100)])

    sprite.graphics.line_style(
        color='#fff',
        round_dot_setting=LineRoundDotSetting(round_size=6, space_size=5))
    polygon_2: Polygon = sprite.graphics.draw_polygon(
        points=[Point2D(200, 50), Point2D(300, 50), Point2D(250, 100)])
    polygon_2.click(on_polygon_click)

    save_overall_html(dest_dir_path=_DEST_DIR_PATH)


def on_polygon_click(
        e: MouseEvent[Polygon], options: Dict[str, Any]) -> None:
    """
    Handler that called when polygon is clicked.

    Parameters
    ----------
    e : MouseEvent
        Created MouseEvent instance.
    options : dict
        Optional parameters.
    """
    polygon: Polygon = e.this
    polygon.line_round_dot_setting = None


if __name__ == '__main__':
    main()
