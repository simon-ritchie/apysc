"""The test project for the handlers circular calling.

Command examples:
$ python test_projects/handler_circular_calling/main.py
$ python handler_circular_calling/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType
from typing import Any, Dict

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
    rectangle_1.animation_move(x=300, y=50, duration=1000).start()
    timer_1: ap.Timer = ap.Timer(
        on_timer_1, delay=3000, options={'rectangle': rectangle_1})
    timer_1.start()

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_timer_1(e: ap.TimerEvent, options: Dict[str, Any]) -> None:
    """
    The handler will be called from a timer.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.animation_move(x=50, y=50, duration=1000).start()
    timer_2: ap.Timer = ap.Timer(
        on_timer_2, delay=3000, options={'rectangle': rectangle})
    timer_2.start()


def on_timer_2(e: ap.TimerEvent, options: Dict[str, Any]) -> None:
    """
    The handler will be called from a timer.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.animation_move(x=300, y=50, duration=1000).start()
    timer_3: ap.Timer = ap.Timer(
        on_timer_1, delay=3000, options={'rectangle': rectangle})
    timer_3.start()


if __name__ == '__main__':
    main()
