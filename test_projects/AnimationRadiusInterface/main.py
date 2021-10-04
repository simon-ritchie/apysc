"""The test project for the AnimationRadiusInterface class.

Command examples:
$ python test_projects/AnimationRadiusInterface/main.py
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
    stage: ap.Stage = ap.Stage(
        background_color='#333',
        stage_width=1000, stage_height=500, stage_elem_id='stage')
    sprite: ap.Sprite = ap.Sprite(stage=stage)
    sprite.graphics.begin_fill(color='#00aaff')
    circle: ap.Circle = sprite.graphics.draw_circle(
        x=100, y=100, radius=50)
    animation_radius: ap.AnimationRadius = circle.animation_radius(
        radius=100, duration=1000, delay=500, easing=ap.Easing.EASE_OUT_QUINT)
    animation_radius.animation_complete(on_animation_complete_1)
    animation_radius.start()

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Circle], options: dict) -> None:
    """
    The handler will be called when an animation is completed.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    circle: ap.Circle = e.this.target
    ap.assert_equal(100, circle.radius)
    animation_radius: ap.AnimationRadius = circle.animation_radius(
        radius=50, duration=1000, delay=500, easing=ap.Easing.EASE_OUT_QUINT)
    animation_radius.animation_complete(on_animation_complete_2)
    animation_radius.start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Circle], options: dict) -> None:
    """
    The handler will be called when an animation is completed.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    circle: ap.Circle = e.this.target
    ap.assert_equal(50, circle.radius)
    animation_radius: ap.AnimationRadius = circle.animation_radius(
        radius=100, duration=1000, delay=500, easing=ap.Easing.EASE_OUT_QUINT)
    animation_radius.animation_complete(on_animation_complete_1)
    animation_radius.start()


if __name__ == '__main__':
    main()
