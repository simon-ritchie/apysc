# Timer class delay setting

This page will explain the `Timer` class `delay` argument setting.

## What argument is this?

The `delay` argument setting will determine the timer tick interval. This setting is a milliseconds unit, so a value of 1000 will tick every 1 second.

The `int`, `float`, `Int`, `Number`, and `FPS` enum can be acceptable.

## Basic usage

You can set the `delay` parameter at the `Timer` class constructor. The following example will set each timer (`timer_1`, `timer_2`, `timer_3`) and passing the delay values of `100`, `333.3333333`, `16.6666667`.

The first-timer (`delay` is 100) will be called 10 times in a second, and the second one (`delay` is 33.3333333) will be called approximately 30 times in a second, and the third one (`delay` is 16.6666667) will be called approximately 60 times.

```py
# runnable
from typing import Any, Dict

import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=350, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)

sprite.graphics.begin_fill(color='#0af')
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50)
rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(
    x=250, y=50, width=50, height=50)


def on_timer(e: ap.TimerEvent, options: Dict[str, Any]):
    """
    The handler would be called every timer tick.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.rotate_around_center(additional_rotation=1)


timer_1: ap.Timer = ap.Timer(
    handler=on_timer, delay=100, options={'rectangle': rectangle_1})
timer_1.start()

timer_2: ap.Timer = ap.Timer(
    handler=on_timer, delay=33.3333333, options={'rectangle': rectangle_2})
timer_2.start()

timer_3: ap.Timer = ap.Timer(
    handler=on_timer, delay=16.6666667, options={'rectangle': rectangle_3})
timer_3.start()

ap.save_overall_html(dest_dir_path='timer_delay_basic_usage/')
```

<iframe src="static/timer_delay_basic_usage/index.html" width="350" height="150"></iframe>

## Set the FPS enum value to the delay argument

You can also pass the `FPS` (frames per second) enum value to the `delay` argument. If the `FPS.FPS_60` is specified, a timer delay will be 60 frames per second (16.6666667 milliseconds). Likely, the `FPS.FPS_30` is specified, a timer delay will be 30 frames per second (33.3333333 milliseconds).

```py
# runnable
from typing import Any, Dict

import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)


def on_timer(e: ap.TimerEvent, options: Dict[str, Any]):
    """
    The handler would be called every timer tick.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.rotate_around_center(additional_rotation=1)


timer: ap.Timer = ap.Timer(
    handler=on_timer, delay=ap.FPS.FPS_60,
    options={'rectangle': rectangle})
timer.start()

ap.save_overall_html(dest_dir_path='timer_delay_fps_enum/')
```

<iframe src="static/timer_delay_fps_enum/index.html" width="150" height="150"></iframe>

## See also

- [FPS enum](fps.md)
