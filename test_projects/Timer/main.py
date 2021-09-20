"""The test project for the Timer class.

Command examples:
$ python test_projects/Timer/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType
from typing import Any
from typing import Dict

from typing_extensions import TypedDict

import apysc as ap
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


class _RectOptions(TypedDict):
    rect: ap.Rectangle


class _MsgOptions(TypedDict):
    msg: str


class _TimerOptions(TypedDict):
    timer: ap.Timer


def main() -> None:
    """
    Entry point of this test project.
    """
    stage: ap.Stage = ap.Stage(
        background_color='#333',
        stage_width=1000, stage_height=500)
    sprite: ap.Sprite = ap.Sprite(stage=stage)
    sprite.graphics.begin_fill(color='#0af')
    rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    options_1: _RectOptions = {'rect': rectangle_1}
    timer_1: ap.Timer = ap.Timer(
        handler=on_timer_1, delay=16.6,
        options=options_1)
    timer_1.start()

    sprite.graphics.begin_fill(color='#f0a')
    rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
        x=150, y=50, width=50, height=50)
    rectangle_2.click(on_rectangle_click)

    sprite.graphics.begin_fill(color='#a0f')
    rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(
        x=250, y=50, width=50, height=50)
    options_1 = {'rect': rectangle_3}
    timer_2: ap.Timer = ap.Timer(
        handler=on_timer_2, delay=16.6, repeat_count=100,
        options=options_1)
    timer_2.start()

    sprite.graphics.begin_fill(color='#f0a')
    rectangle_4: ap.Rectangle = sprite.graphics.draw_rect(
        x=350, y=50, width=50, height=50)
    options_1 = {'rect': rectangle_4}
    timer_3: ap.Timer = ap.Timer(
        handler=on_timer_1, delay=ap.FPS.FPS_60,
        options=options_1)
    timer_3.start()

    sprite.graphics.begin_fill(color='#a0f')
    rectangle_5: ap.Rectangle = sprite.graphics.draw_rect(
        x=450, y=50, width=50, height=50)
    options_1 = {'rect': rectangle_5}
    timer_4: ap.Timer = ap.Timer(
        handler=on_timer_2, delay=ap.FPS.FPS_60, repeat_count=100,
        options=options_1)
    options_2: _MsgOptions = {'msg': 'Triggered timer complete event!'}
    timer_4.timer_complete(
        on_timer_complete_1,
        options=options_2)
    timer_4.start()

    sprite.graphics.begin_fill(color='#0af')
    rectangle_6: ap.Rectangle = sprite.graphics.draw_rect(
        x=550, y=50, width=50, height=50)
    options_1 = {'rect': rectangle_6}
    timer_5: ap.Timer = ap.Timer(
        handler=on_timer_2, delay=ap.FPS.FPS_60,
        repeat_count=100,
        options=options_1)
    options_3: _TimerOptions = {'timer': timer_5}
    timer_5.timer_complete(
        handler=on_timer_complete_2, options=options_3)
    timer_5.start()

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_timer_1(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler would be called from a timer instance.

    Parameters
    ----------
    e : TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    with ap.If(e.this.current_count >= 100):
        e.this.stop()
        ap.trace('Stapped!')
        ap.assert_false(e.this.running)
    with ap.Else():
        rect: ap.Rectangle = options['rect']
        rect.y += 1
        ap.assert_true(e.this.running)


def on_timer_2(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler would be called from a timer instance.

    Parameters
    ----------
    e : TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rect: ap.Rectangle = options['rect']
    rect.y += 1


def on_rectangle_click(
        e: ap.MouseEvent[ap.Rectangle], options: Dict[Any, Any]) -> None:
    """
    The handler would be called when a rectangle is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    options_: _RectOptions = {'rect': e.this}
    timer: ap.Timer = ap.Timer(
        handler=on_timer_1,
        delay=33.3,
        options=options_)
    timer.start()


def on_timer_complete_1(e: ap.TimerEvent, options: _MsgOptions) -> None:
    """
    The handler would be called when a timer complete.

    Parameters
    ----------
    e : TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace(options['msg'])


def on_timer_complete_2(e: ap.TimerEvent, options: _TimerOptions) -> None:
    """
    The handler would be called when a timer complete.

    Parameters
    ----------
    e : TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace('Timer complete!')
    timer: ap.Timer = options['timer']
    timer.reset()
    timer.start()


if __name__ == '__main__':
    main()
