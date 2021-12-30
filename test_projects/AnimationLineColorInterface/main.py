"""The test project for the AnimationLineColorInterface class.

Command examples:
$ python test_projects/AnimationLineColorInterface/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

import apysc as ap
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


def main() -> None:
    """
    Entry point of this test project.
    """
    ap.Stage(
        background_color='#333',
        stage_width=1000, stage_height=500, stage_elem_id='stage')
    sprite: ap.Sprite = ap.Sprite()
    sprite.graphics.line_style(color='f0a', thickness=5)
    rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    rectangle.animation_line_color(
        line_color='0af',
        duration=1000,
        delay=500,
        easing=ap.Easing.EASE_OUT_QUINT,
    ).animation_complete(on_animation_complete_1).start()

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
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
    ap.assert_equal('#00aaff', rectangle.line_color)
    rectangle.animation_line_color(
        line_color='f0a',
        duration=1000,
        delay=500,
        easing=ap.Easing.EASE_OUT_QUINT,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
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
    ap.assert_equal('#ff00aa', rectangle.line_color)
    rectangle.animation_line_color(
        line_color='0af',
        duration=1000,
        delay=500,
        easing=ap.Easing.EASE_OUT_QUINT,
    ).animation_complete(on_animation_complete_1).start()


if __name__ == '__main__':
    main()
