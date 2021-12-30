"""The test project for the SkewYInterface class.

Command examples:
$ python test_projects/SkewYInterface/main.py
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
    ap.Stage(
        background_color='#333',
        stage_width=1000, stage_height=500, stage_elem_id='stage')
    sprite: ap.Sprite = ap.Sprite()
    sprite.graphics.begin_fill(color='#00aaff')
    rect_1: ap.Rectangle = sprite.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    rect_1.skew_y = ap.Int(50)
    rect_1.skew_y = ap.Int(0)

    rect_2: ap.Rectangle = sprite.graphics.draw_rect(
        x=150, y=50, width=50, height=50)
    options: _RectOptions = {'rectangle': rect_2}
    timer: ap.Timer = ap.Timer(
        on_timer, delay=ap.FPS.FPS_60,
        options=options)
    timer.start()

    rect_3: ap.Rectangle = sprite.graphics.draw_rect(
        x=250, y=50, width=50, height=50)
    rect_3.skew_y = ap.Int(50)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


def on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
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
    rectangle.skew_y += 1


if __name__ == '__main__':
    main()
