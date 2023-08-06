"""The test project for the AnimationMoveMixIn class.

Command examples:
$ python test_projects/AnimationMoveMixIn/main.py
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


class _MsgOptions(TypedDict):
    msg: str


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
    rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
        x=50, y=50, width=50, height=50
    )
    animation_move: ap.AnimationMove[ap.Rectangle] = rectangle_1.animation_move(
        x=100, y=100, duration=1000, easing=ap.Easing.EASE_OUT_QUINT
    )
    options: _MsgOptions = {"msg": "Animation move 1 completed!"}
    animation_move.animation_complete(
        handler=on_animation_move_1_complete, options=options
    )
    animation_move.start()

    rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
        x=150, y=50, width=50, height=50
    )
    rectangle_2.animation_move(
        x=600, y=100, duration=3000, delay=1000, easing=ap.Easing.EASE_OUT_QUINT
    ).start()

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_animation_move_1_complete(
    e: ap.AnimationEvent[ap.Rectangle], options: _MsgOptions
) -> None:
    """
    The handler will be called when an animation is completed.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace(options["msg"])
    assert isinstance(e.this, ap.AnimationMove)
    rectangle: ap.Rectangle = e.this.target
    ap.assert_equal(100, rectangle.x)
    ap.assert_equal(100, rectangle.y)
    animation_move: ap.AnimationMove = rectangle.animation_move(
        x=50, y=50, duration=1000, easing=ap.Easing.EASE_OUT_QUINT
    )
    animation_move.animation_complete(on_animation_move_2_complete)
    animation_move.start()


def on_animation_move_2_complete(
    e: ap.AnimationEvent[ap.Rectangle], options: dict
) -> None:
    """
    The handler will be called when an animation is completed.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this.target
    ap.assert_equal(50, rectangle.x)
    ap.assert_equal(50, rectangle.y)
    animation_move: ap.AnimationMove = rectangle.animation_move(
        x=100, y=100, duration=1000, easing=ap.Easing.EASE_OUT_QUINT
    )
    options_: _MsgOptions = {"msg": "Animation move 1 completed!"}
    animation_move.animation_complete(on_animation_move_1_complete, options=options_)
    animation_move.start()


if __name__ == "__main__":
    main()
