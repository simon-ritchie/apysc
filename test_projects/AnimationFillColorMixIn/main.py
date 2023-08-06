"""The test project for the AnimationFillColorMixIn class.

Command examples:
$ python test_projects/AnimationFillColorMixIn/main.py
"""

import sys

sys.path.append("./")

import os
from types import ModuleType

import apysc as ap
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module), "test_output/"
)


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
    animation_fill_color: ap.AnimationFillColor = rectangle_1.animation_fill_color(
        fill_color=ap.Color("0af"), duration=1000, delay=500, easing=ap.Easing.EASE_OUT_QUINT
    )
    animation_fill_color.animation_complete(on_animation_complete_1)
    animation_fill_color.start()

    rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
        x=150, y=50, width=50, height=50
    )
    rectangle_2.animation_fill_color(
        fill_color=ap.Color("#f0a"),
        duration=1000,
    ).start()

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_animation_complete_1(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler will be called when the animation is completed.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this.target
    animation_fill_color: ap.AnimationFillColor = rectangle.animation_fill_color(
        fill_color=ap.Color("f0a"), duration=1000, delay=500, easing=ap.Easing.EASE_OUT_QUINT
    )
    animation_fill_color.animation_complete(on_animation_complete_2)
    animation_fill_color.start()


def on_animation_complete_2(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler will be called when the animation is completed.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this.target
    animation_fill_color: ap.AnimationFillColor = rectangle.animation_fill_color(
        fill_color=ap.Color("0af"), duration=1000, delay=500, easing=ap.Easing.EASE_OUT_QUINT
    )
    animation_fill_color.animation_complete(on_animation_complete_1)
    animation_fill_color.start()


if __name__ == "__main__":
    main()
