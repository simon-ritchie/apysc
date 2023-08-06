"""The test project for the `FlipXMixIn` class.

Command examples:
$ python test_projects/FlipXMixIn/main.py
"""

import sys

sys.path.append("./")

import os
from types import ModuleType

from typing_extensions import TypedDict

import apysc as ap
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module), "test_output/"
)


class _PolygonOptions(TypedDict):
    polygon: ap.Polygon


def main() -> None:
    """
    Entry point of this test project.
    """
    ap.Stage(
        background_color=ap.Color("#333"),
        stage_width=1000,
        stage_height=500,
        stage_elem_id="stage",
    )
    sprite_1: ap.Sprite = ap.Sprite()
    sprite_1.graphics.begin_fill(color=ap.Color("#0af"))
    sprite_1.x = ap.Number(150)

    polygon_1: ap.Polygon = sprite_1.graphics.draw_polygon(
        points=[
            ap.Point2D(x=0, y=50),
            ap.Point2D(x=0, y=100),
            ap.Point2D(x=50, y=75),
        ]
    )
    options: _PolygonOptions = {"polygon": polygon_1}
    timer_1: ap.Timer = ap.Timer(on_timer_1, delay=1000, options=options)
    timer_1.start()

    polygon_2: ap.Polygon = sprite_1.graphics.draw_polygon(
        points=[
            ap.Point2D(x=0, y=150),
            ap.Point2D(x=0, y=200),
            ap.Point2D(x=50, y=175),
        ]
    )
    polygon_2.x = ap.Number(50)
    options = {"polygon": polygon_2}
    timer_2: ap.Timer = ap.Timer(on_timer_1, delay=1000, options=options)
    timer_2.start()

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


def on_timer_1(e: ap.TimerEvent, options: _PolygonOptions) -> None:
    """
    The handler will be called from a timer.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    polygon: ap.Polygon = options["polygon"]
    flip_x: ap.Boolean = polygon.flip_x
    flip_x = flip_x.not_
    polygon.flip_x = flip_x


if __name__ == "__main__":
    main()
