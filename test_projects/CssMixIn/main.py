"""The test project for the CssMixIn class.

Command examples:
$ python test_projects/CssMixIn/main.py
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


class _Sp1AndRectOptions(TypedDict):
    sprite_1: ap.Sprite
    rectangle: ap.Rectangle


def main() -> None:
    """
    Entry point of this test project.
    """
    ap.Stage(background_color=ap.Color("#333"), stage_width=1000, stage_height=500)
    sprite_1: ap.Sprite = ap.Sprite()
    sprite_1.graphics.begin_fill(color=ap.Color("#0af"))
    sprite_1.graphics.draw_rect(x=50, y=50, width=50, height=50)

    sprite_2: ap.Sprite = ap.Sprite()
    sprite_2.graphics.begin_fill(color=ap.Color("#f0a"))
    rectangle: ap.Rectangle = sprite_2.graphics.draw_rect(
        x=150, y=50, width=50, height=50
    )

    options: _Sp1AndRectOptions = {
        "sprite_1": sprite_1,
        "rectangle": rectangle,
    }
    timer: ap.Timer = ap.Timer(handler=on_timer, delay=1000, options=options)
    timer.start()

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


def on_timer(e: ap.TimerEvent, options: _Sp1AndRectOptions) -> None:
    """
    The handler would be called from a timer.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    sprite_1: ap.Sprite = options["sprite_1"]
    rectangle: ap.Rectangle = options["rectangle"]
    display_css: ap.String = sprite_1.get_css(name="display")
    condition: ap.Boolean = display_css == ""
    with ap.If(condition):
        sprite_1.set_css(name="display", value="none")
        rectangle.set_css(name="display", value="none")
    with ap.Else():
        sprite_1.set_css(name="display", value="")
        rectangle.set_css(name="display", value="")


if __name__ == "__main__":
    main()
