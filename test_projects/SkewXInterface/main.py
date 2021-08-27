"""The test project for the SkewXInterface class.

Command examples:
$ python test_projects/SkewXInterface/main.py
$ python SkewXInterface/main.py
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
    rect_1: ap.Rectangle = sprite.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    rect_1.skew_x = ap.Int(50)
    rect_1.skew_x = ap.Int(0)

    rect_2: ap.Rectangle = sprite.graphics.draw_rect(
        x=150, y=50, width=50, height=50)
    timer: ap.Timer = ap.Timer(
        on_timer, delay=ap.FPS.FPS_60,
        options={'rectangle': rect_2})
    timer.start()

    rect_3: ap.Rectangle = sprite.graphics.draw_rect(
        x=250, y=50, width=50, height=50)
    rect_3.skew_x = ap.Int(50)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


def on_timer(e: ap.TimerEvent, options: Dict[str, Any]) -> None:
    """
    The handler will be called from the timer.

    Parameters
    ----------
    e : TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.skew_x += 1


if __name__ == '__main__':
    main()
