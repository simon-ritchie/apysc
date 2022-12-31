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


def main() -> None:
    """
    Entry point of this test project.
    """
    _: ap.Stage = ap.Stage(background_color="#333")
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

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_enter_frame_1(e: ap.EnterFrameEvent[ap.Sprite], options: _RectOptions) -> None:
    """
    The handler for an enter-frame event.

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
    The handler for an enter-frame event.

    Parameters
    ----------
    e : ap.EnterFrameEvent[ap.Sprite]
        Event instance.
    options : _RectOptions
        Optional argument dictionary.
    """
    options["rectangle"].x += 1


if __name__ == "__main__":
    main()
