"""The test project for the timer event circular calling and
updating cx-coordinate interface.

Command examples:
$ python test_projects/timer_circular_calling_cx/main.py
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


class _CircleOptions(TypedDict):
    circle: ap.Circle


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
    sprite: ap.Sprite = ap.Sprite()
    sprite.graphics.begin_fill(color=ap.Color("#00aaff"))

    circle: ap.Circle = sprite.graphics.draw_circle(x=75, y=75, radius=50)
    options: _CircleOptions = {"circle": circle}
    timer_1: ap.Timer = ap.Timer(
        on_timer_1, delay=ap.FPS.FPS_60, repeat_count=100, options=options
    )
    timer_1.timer_complete(on_timer_complete_1, options=options)
    timer_1.start()

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_timer_1(e: ap.TimerEvent, options: _CircleOptions) -> None:
    """
    The handler will be called from a timer.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    circle: ap.Circle = options["circle"]
    circle.x += 1


def on_timer_complete_1(e: ap.TimerEvent, options: _CircleOptions) -> None:
    """
    The handler will be called when a timer has completed.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    timer_2: ap.Timer = ap.Timer(
        on_timer_2, delay=ap.FPS.FPS_60, repeat_count=100, options=options
    )
    timer_2.timer_complete(on_timer_complete_2, options=options)
    timer_2.start()


def on_timer_2(e: ap.TimerEvent, options: _CircleOptions) -> None:
    """
    The handler will be called from a timer.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    circle: ap.Circle = options["circle"]
    circle.x -= 1


def on_timer_complete_2(e: ap.TimerEvent, options: _CircleOptions) -> None:
    """
    The handler will be called when a timer has completed.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    timer_3: ap.Timer = ap.Timer(
        on_timer_1, delay=ap.FPS.FPS_60, repeat_count=100, options=options
    )
    timer_3.timer_complete(on_timer_complete_1, options=options)
    timer_3.start()


if __name__ == "__main__":
    main()
