"""The test project for the `enter_frame` interface.

Command examples:
$ python test_projects/enter_frame/main.py
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


class _SpriteOptions(TypedDict):
    sprite: ap.Sprite


class _SpriteAndRectOptions(TypedDict):
    sprite: ap.Sprite
    rectangle: ap.Rectangle


def main() -> None:
    """
    Entry point of this test project.
    """
    _: ap.Stage = ap.Stage(background_color="#333", stage_width=2000)
    sprite: ap.Sprite = ap.Sprite()
    sprite.graphics.begin_fill(color="#0af")
    rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
        x=50,
        y=50,
        width=50,
        height=50,
    )
    options: _RectOptions = {
        "rectangle": rectangle_1,
    }
    sprite.enter_frame(
        handler=on_enter_frame_1,
        fps=ap.FPS.FPS_30,
        options=options,
    )

    sprite.graphics.begin_fill(color="#f0a")
    rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
        x=150,
        y=50,
        width=50,
        height=50,
    )
    options = {
        "rectangle": rectangle_2,
    }
    sprite.enter_frame(
        handler=on_enter_frame_2,
        fps=ap.FPS.FPS_60,
        options=options,
    )

    sprite.graphics.begin_fill(color="#0fa")
    rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(
        x=250,
        y=50,
        width=50,
        height=50,
    )
    options = {
        "rectangle": rectangle_3,
    }
    sprite.enter_frame(
        handler=on_enter_frame_3,
        options=options,
    )

    options_: _SpriteOptions = {
        "sprite": sprite,
    }
    ap.Timer(
        handler=on_timer_1,
        delay=1000,
        repeat_count=1,
        options=options_,
    ).start()

    options__: _SpriteAndRectOptions = {
        "sprite": sprite,
        "rectangle": rectangle_1,
    }
    ap.Timer(
        handler=on_timer_3,
        delay=1500,
        repeat_count=1,
        options=options__,
    ).start()

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_timer_1(e: ap.TimerEvent, options: _SpriteOptions) -> None:
    """
    A handler for a timer event.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : _SpriteOptions
        Optional argument dictionary.
    """
    options["sprite"].unbind_enter_frame(handler=on_enter_frame_1)
    ap.Timer(
        handler=on_timer_2,
        delay=1000,
        repeat_count=1,
        options=options,
    ).start()


def on_timer_2(e: ap.TimerEvent, options: _SpriteOptions) -> None:
    """
    A handler for a timer event.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : _SpriteOptions
        Optional argument dictionary.
    """
    options["sprite"].unbind_enter_frame_all()


def on_enter_frame_1(e: ap.EnterFrameEvent[ap.Sprite], options: _RectOptions) -> None:
    """
    A handler for an enter-frame event.

    Parameters
    ----------
    e : ap.EnterFrameEvent[ap.Sprite]
        Event instance.
    options : _RectOptions
        Optional argument dictionary.
    """
    options["rectangle"].x += 2


def on_enter_frame_2(e: ap.EnterFrameEvent[ap.Sprite], options: _RectOptions) -> None:
    """
    A handler for an enter-frame event.

    Parameters
    ----------
    e : ap.EnterFrameEvent[ap.Sprite]
        Event instance.
    options : _RectOptions
        Optional argument dictionary.
    """
    options["rectangle"].x += 1


def on_enter_frame_3(e: ap.EnterFrameEvent[ap.Sprite], options: _RectOptions) -> None:
    """
    A handler for an enter-frame event.

    Parameters
    ----------
    e : ap.EnterFrameEvent[ap.Sprite]
        _description_
    options : _RectOptions
        _description_
    """
    options["rectangle"].x += 1


def on_timer_3(e: ap.TimerEvent, options: _SpriteAndRectOptions) -> None:
    """
    A handler for a timer event.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : _SpriteAndRectOptions
        Optional argument dictionary.
    """
    options_: _RectOptions = {
        "rectangle": options["rectangle"],
    }
    options["sprite"].enter_frame(
        handler=on_enter_frame_1,
        options=options_,
        fps=ap.FPS.FPS_15,
    )


if __name__ == "__main__":
    main()
