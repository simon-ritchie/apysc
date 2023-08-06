"""The test project for the RotationAroundPointMixIn class.

Command examples:
$ python test_projects/RotationAroundPointMixIn/main.py
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


class _Rect1And2Options(TypedDict):
    rectangle_1: ap.Rectangle
    rectangle_2: ap.Rectangle


class _Rect3Options(TypedDict):
    rectangle_3: ap.Rectangle


def main() -> None:
    """
    Entry point of this test project.
    """
    ap.Stage(background_color=ap.Color("#333"), stage_width=1000, stage_height=500)

    sprite_1: ap.Sprite = ap.Sprite()
    sprite_1.graphics.begin_fill(color=ap.Color("#0af"), alpha=0.5)
    rectangle_1: ap.Rectangle = sprite_1.graphics.draw_rect(
        x=50, y=50, width=50, height=50
    )

    rectangle_2: ap.Rectangle = sprite_1.graphics.draw_rect(
        x=50, y=50, width=50, height=50
    )

    options_1: _Rect1And2Options = {
        "rectangle_1": rectangle_1,
        "rectangle_2": rectangle_2,
    }
    timer_1: ap.Timer = ap.Timer(
        handler=on_timer_1, delay=ap.FPS.FPS_60, options=options_1
    )
    timer_1.start()

    sprite_2: ap.Sprite = ap.Sprite()
    sprite_2.graphics.begin_fill(color=ap.Color("#f0a"), alpha=0.5)
    sprite_2.x = ap.Number(50)
    sprite_2.y = ap.Number(50)
    rectangle_3: ap.Rectangle = sprite_2.graphics.draw_rect(
        x=50, y=50, width=50, height=50
    )
    options_2: _Rect3Options = {"rectangle_3": rectangle_3}
    timer_2: ap.Timer = ap.Timer(
        handler=on_timer_2, delay=ap.FPS.FPS_60, options=options_2
    )
    timer_2.start()

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_timer_1(e: ap.TimerEvent, options: _Rect1And2Options) -> None:
    """
    The handler would be called from the first timer.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle_1: ap.Rectangle = options["rectangle_1"]
    x: ap.Number = ap.Number(50)
    y: ap.Number = ap.Number(50)
    rotation: ap.Int = rectangle_1.get_rotation_around_point(x=x, y=y)
    rotation += 1
    rectangle_1.set_rotation_around_point(rotation=rotation, x=x, y=y)

    rectangle_2: ap.Rectangle = options["rectangle_2"]
    x = ap.Number(100)
    y = ap.Number(100)
    rotation = rectangle_1.get_rotation_around_point(x=x, y=y)
    rotation += 1
    rectangle_2.set_rotation_around_point(rotation=rotation, x=x, y=y)


def on_timer_2(e: ap.TimerEvent, options: _Rect3Options) -> None:
    """
    The handler would be called from the second timer.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle_3: ap.Rectangle = options["rectangle_3"]
    x: ap.Number = ap.Number(50)
    y: ap.Number = ap.Number(50)
    rotation: ap.Int = rectangle_3.get_rotation_around_point(x=x, y=y)
    rotation += 1
    rectangle_3.set_rotation_around_point(rotation=rotation, x=x, y=y)


if __name__ == "__main__":
    main()
