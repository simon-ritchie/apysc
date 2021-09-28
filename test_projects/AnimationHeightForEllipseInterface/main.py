"""The test project for the AnimationHeightForEllipseInterface class.

Command examples:
$ python test_projects/AnimationHeightForEllipseInterface/main.py
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
    ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(
        x=100, y=100, width=50, height=50)
    animation_height: ap.AnimationHeightForEllipse = ellipse.animation_height(
        height=100, duration=1000, easing=ap.Easing.EASE_OUT_QUINT)
    animation_height.animation_complete(on_animation_complete_1)
    animation_height.start()

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Ellipse], options: dict) -> None:
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
    animation_height: ap.AnimationHeightForEllipse = ellipse.animation_height(
        height=50, duration=1000, easing=ap.Easing.EASE_OUT_QUINT)
    animation_height.animation_complete(on_animation_complete_2)
    animation_height.start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Ellipse], options: dict) -> None:
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
    animation_height: ap.AnimationHeightForEllipse = ellipse.animation_height(
        height=100, duration=1000, easing=ap.Easing.EASE_OUT_QUINT)
    animation_height.animation_complete(on_animation_complete_1)
    animation_height.start()


if __name__ == '__main__':
    main()
