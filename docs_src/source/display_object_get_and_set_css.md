# Display object get_css and set_css interfaces

This page will explain the `DisplayObject` class `get_css` and `set_css` method interfaces.

## What interfaces are these?

The `get_css` method will return a `css` string, and the `set_css` method will set the CSS setting to a `DisplayObject` instance.

## Basic usage

Each interface requires the `name` argument as the CSS name. In addition, the `set_css` method interface also requires the `value` argument as the CSS value string.

The following example sets the `none` value to the `display` CSS if the current CSS value is the default (blank string, `''`). Otherwise, revert the value to default (`Else` case) by the timer event (ticks every second).

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _SpriteOptions(TypedDict):
    sprite: ap.Sprite


def on_timer(e: ap.TimerEvent, options: _SpriteOptions) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    sprite: ap.Sprite = options['sprite']
    display_css_val: ap.String = sprite.get_css(name='display')
    condition: ap.Boolean = display_css_val == 'none'
    with ap.If(condition):
        sprite.set_css(name='display', value='')
    with ap.Else():
        sprite.set_css(name='display', value='none')


ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
options: _SpriteOptions = {'sprite': sprite}
timer: ap.Timer = ap.Timer(
    handler=on_timer, delay=1000, options=options)
timer.start()

ap.save_overall_html(
    dest_dir_path='display_object_get_and_set_css_basic_usage/')
```

<iframe src="static/display_object_get_and_set_css_basic_usage/index.html" width="150" height="150"></iframe>