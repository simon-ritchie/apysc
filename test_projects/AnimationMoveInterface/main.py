"""The test project for the AnimationMoveInterface class.

Command examples:
$ python test_projects/AnimationMoveInterface/main.py
$ python AnimationMoveInterface/main.py
"""

import sys
from typing import Any
from typing import Dict

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
    rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    animation_move_1: ap.AnimationMove[ap.Rectangle] = \
        rectangle_1.animation_move(
            x=500, y=100, duration=3000,
            easing=ap.Easing.EASE_OUT_QUINT)
    animation_move_1.animation_complete(
        handler=on_animation_move_1_complete,
        options={'msg': 'Animation move 1 completed!'})
    animation_move_1.start()

    rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
        x=150, y=50, width=50, height=50)
    rectangle_2.animation_move(
        x=600, y=100, duration=3000, delay=1000,
        easing=ap.Easing.EASE_OUT_QUINT).start()

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_animation_move_1_complete(
        e: ap.AnimationEvent[ap.Rectangle],
        options: Dict[str, Any]) -> None:
    """
    The handler will be called when an animation is complete.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace(options['msg'])
    assert isinstance(e.this, ap.AnimationMove)
    rectangle: ap.Rectangle = e.this.target
    rectangle.animation_move(
        x=50, y=50, duration=3000,
        easing=ap.Easing.EASE_OUT_QUINT).start()


if __name__ == '__main__':
    main()
