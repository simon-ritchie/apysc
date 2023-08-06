"""The test project for the AnimationFinishMixIn class.

Command examples:
$ python test_projects/AnimationFinishMixIn/main.py
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


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


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

    rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
    rectangle.animation_x(
        x=200,
        duration=3000,
    ).animation_complete(on_animation_complete).start()

    options: _RectOptions = {
        "rectangle": rectangle,
    }
    timer: ap.Timer = ap.Timer(
        handler=on_timer, delay=1000, repeat_count=1, options=options
    )
    timer.start()

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler will be called from a timer.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options["rectangle"]
    rectangle.animation_finish()


def on_animation_complete(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler will be called when an animation is completed.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace("Animation completed!")


if __name__ == "__main__":
    main()
