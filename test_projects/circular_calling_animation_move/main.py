"""The test project for the animation_move interface's circular calling.

Command examples:
$ python test_projects/circular_calling_animation_move/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from typing_extensions import TypedDict

import apysc as ap
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def main() -> None:
    """
    Entry point of this test project.
    """
    stage: ap.Stage = ap.Stage(
        background_color='#333',
        stage_width=1000, stage_height=500, stage_elem_id='stage')
    sprite: ap.Sprite = ap.Sprite(stage=stage)
    sprite.graphics.begin_fill(color='#00aaff')

    rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    animation_move: ap.AnimationMove = rectangle.animation_move(
        x=100, y=50, duration=1000, easing=ap.Easing.EASE_OUT_QUINT)
    options: _RectOptions = {'rectangle': rectangle}
    animation_move.animation_complete(
        on_animation_complete_1, options=options)
    animation_move.start()

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_animation_complete_1(
        e: ap.AnimationEvent, options: _RectOptions) -> None:
    """
    The handler will be called when the animation is completed.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    animation_move: ap.AnimationMove = rectangle.animation_move(
        x=50, y=50, duration=1000, easing=ap.Easing.EASE_OUT_QUINT)
    animation_move.animation_complete(
        on_animation_complete_2, options=options)
    animation_move.start()


def on_animation_complete_2(
        e: ap.AnimationEvent, options: _RectOptions) -> None:
    """
    The handler will be called when the animation is completed.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    animation_move: ap.AnimationMove = rectangle.animation_move(
        x=100, y=50, duration=1000, easing=ap.Easing.EASE_OUT_QUINT)
    animation_move.animation_complete(
        on_animation_complete_1, options=options)
    animation_move.start()


if __name__ == '__main__':
    main()
