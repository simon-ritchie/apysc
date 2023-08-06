"""The test project for the AnimationWidthForEllipseMixIn class.

Command examples:
$ python test_projects/AnimationWidthForEllipseMixIn/main.py
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
    ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(
        x=100, y=100, width=50, height=50
    )
    animation_width: ap.AnimationWidthForEllipse = ellipse.animation_width(
        width=100, duration=1000, delay=500, easing=ap.Easing.EASE_OUT_QUINT
    )
    animation_width.animation_complete(on_animation_complete_1)
    animation_width.start()

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_animation_complete_1(e: ap.AnimationEvent[ap.Ellipse], options: dict) -> None:
    """
    The handler will be called when an animation is completed.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ellipse: ap.Ellipse = e.this.target
    ap.assert_equal(100, ellipse.width)
    animation_width: ap.AnimationWidthForEllipse = ellipse.animation_width(
        width=50, duration=1000, delay=500, easing=ap.Easing.EASE_OUT_QUINT
    )
    animation_width.animation_complete(on_animation_complete_2)
    animation_width.start()


def on_animation_complete_2(e: ap.AnimationEvent[ap.Ellipse], options: dict) -> None:
    """
    The handler will be called when an animation is completed.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ellipse: ap.Ellipse = e.this.target
    ap.assert_equal(50, ellipse.width)
    animation_width: ap.AnimationWidthForEllipse = ellipse.animation_width(
        width=100, duration=1000, delay=500, easing=ap.Easing.EASE_OUT_QUINT
    )
    animation_width.animation_complete(on_animation_complete_1)
    animation_width.start()


if __name__ == "__main__":
    main()
