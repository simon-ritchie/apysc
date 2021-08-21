"""The test project for the `FlipYInterface` class.

Command examples:
$ python test_projects/FlipYInterface/main.py
$ python FlipYInterface/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType
from typing import Any
from typing import Dict

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
    sprite_1: ap.Sprite = ap.Sprite(stage=stage)
    sprite_1.graphics.begin_fill(color='#0af')
    sprite_1.y = ap.Int(150)

    polygon_1: ap.Polygon = sprite_1.graphics.draw_polygon(
        points=[
            ap.Point2D(x=75, y=0),
            ap.Point2D(x=50, y=50),
            ap.Point2D(x=100, y=50),
        ])
    timer_1: ap.Timer = ap.Timer(
        on_timer_1, delay=1000, options={'polygon': polygon_1})
    timer_1.start()

    polygon_2: ap.Polygon = sprite_1.graphics.draw_polygon(
        points=[
            ap.Point2D(x=175, y=0),
            ap.Point2D(x=150, y=50),
            ap.Point2D(x=200, y=50),
        ])
    polygon_2.y = ap.Int(50)
    timer_2: ap.Timer = ap.Timer(
        on_timer_1, delay=1000, options={'polygon': polygon_2})
    timer_2.start()

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


def on_timer_1(e: ap.TimerEvent, options: Dict[str, Any]) -> None:
    """
    The handler will be called from a timer.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    polygon: ap.Polygon = options['polygon']
    flip_y: ap.Boolean = polygon.flip_y
    flip_y = flip_y.not_
    polygon.flip_y = flip_y


if __name__ == '__main__':
    main()
