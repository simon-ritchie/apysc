"""The test project for the Timer class.

Command examples:
$ python test_projects/Timer/main.py
$ python Timer/main.py
"""

import sys
from typing import Any
from typing import Dict

sys.path.append('./')

import os
from types import ModuleType

from apysc import FPS
from apysc import Else
from apysc import If
from apysc import MouseEvent
from apysc import Rectangle
from apysc import Sprite
from apysc import Stage
from apysc import Timer
from apysc import TimerEvent
from apysc import assert_false
from apysc import assert_true
from apysc import save_overall_html
from apysc import trace
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
    stage: Stage = Stage(
        background_color='#333',
        stage_width=1000, stage_height=500)
    sprite: Sprite = Sprite(stage=stage)
    sprite.graphics.begin_fill(color='#0af')
    rectangle_1: Rectangle = sprite.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    timer_1: Timer = Timer(
        handler=on_timer_1, delay=16.6,
        options={'rect': rectangle_1})
    timer_1.start()

    sprite.graphics.begin_fill(color='#f0a')
    rectangle_2: Rectangle = sprite.graphics.draw_rect(
        x=150, y=50, width=50, height=50)
    rectangle_2.click(on_rectangle_click)

    sprite.graphics.begin_fill(color='#a0f')
    rectangle_3: Rectangle = sprite.graphics.draw_rect(
        x=250, y=50, width=50, height=50)
    timer_2: Timer = Timer(
        handler=on_timer_2, delay=16.6, repeat_count=100,
        options={'rect': rectangle_3})
    timer_2.start()

    sprite.graphics.begin_fill(color='#f0a')
    rectangle_4: Rectangle = sprite.graphics.draw_rect(
        x=350, y=50, width=50, height=50)
    timer_3: Timer = Timer(
        handler=on_timer_1, delay=FPS.FPS_60,
        options={'rect': rectangle_4})
    timer_3.start()

    sprite.graphics.begin_fill(color='#a0f')
    rectangle_5: Rectangle = sprite.graphics.draw_rect(
        x=450, y=50, width=50, height=50)
    timer_4: Timer = Timer(
        handler=on_timer_2, delay=FPS.FPS_60, repeat_count=100,
        options={'rect': rectangle_5})
    timer_4.timer_complete(
        on_timer_complete,
        options={'msg': 'Triggered timer complete event!'})
    timer_4.start()

    save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_timer_1(e: TimerEvent, options: Dict[str, Any]) -> None:
    """
    The handler would be called from a timer instance.

    Parameters
    ----------
    e : TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    with If(e.this.current_count >= 100):
        e.this.stop()
        trace('Stapped!')
        assert_false(e.this.running)
    with Else():
        rect: Rectangle = options['rect']
        rect.y += 1
        assert_true(e.this.running)


def on_timer_2(e: TimerEvent, options: Dict[str, Any]) -> None:
    """
    The handler would be called from a timer instance.

    Parameters
    ----------
    e : TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rect: Rectangle = options['rect']
    rect.y += 1


def on_rectangle_click(
        e: MouseEvent[Rectangle], options: Dict[str, Any]) -> None:
    """
    The handler would be called when a rectangle is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    timer: Timer = Timer(
        handler=on_timer_1,
        delay=33.3,
        options={'rect': e.this})
    timer.start()


def on_timer_complete(e: TimerEvent, options: Dict[str, Any]) -> None:
    """
    The handler would be called when a timer complete.

    Parameters
    ----------
    e : TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    trace(options['msg'])


if __name__ == '__main__':
    main()
