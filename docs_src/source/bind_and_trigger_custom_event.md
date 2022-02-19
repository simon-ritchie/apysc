# Bind and trigger the custom event

This page explains the `bind_custom_event` and `trigger_custom_event` interfaces.

## What interfaces are these?

The `bind_custom_event` interface registers your custom event to the instance, and the `trigger_custom_event` one triggers the registered custom events at any time.

## Basic usage

The `bind_custom_event` interface has the `custom_event_type`, `handler`, `e`, and `options` arguments (`options` is optional).

The `custom_event_type` argument is the custom event type name's string. This value needs to specify the same one at the calling of the `trigger_custom_event` interface.

The `e` argument is an event instance that may become the subclass of the `Event` class, such as the `MouseEvent` or `TimerEvent`\.

The following example rotates the rectangle when you click it. If the rectangle rotated 90 degrees, then the custom event (`rotate_90_degrees`) is triggered, and the `on_rotate_90_degrees` handler (custom event) is called and display the second rectangle (toggle the `visible` property):

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap

# Custom event type name.
ROTATE_90_DEGREES: str = 'rotate_90_degrees'


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_rectangle_click(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.unbind_click(on_rectangle_click)
    options_: _RectOptions = {'rectangle': e.this}
    timer: ap.Timer = ap.Timer(
        on_timer, delay=ap.FPS.FPS_60, repeat_count=90,
        options=options_)
    timer.timer_complete(
        on_timer_complete,
        options=options_)
    timer.start()


def on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.rotation_around_center += 1


def on_timer_complete(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler that timer calls when its end.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.trigger_custom_event(custom_event_type=ROTATE_90_DEGREES)


def on_rotate_90_degrees(e: ap.Event, options: _RectOptions) -> None:
    """
    The handler that the rectangle rates 90 degrees (custom event).

    Parameters
    ----------
    e : ap.Event
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.visible = ap.Boolean(True)


ap.Stage(
    stage_width=250, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle_1.click(on_rectangle_click)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50)
rectangle_2.visible = ap.Boolean(False)

e: ap.Event = ap.Event(this=rectangle_1)
rectangle_1.bind_custom_event(
    custom_event_type=ROTATE_90_DEGREES, handler=on_rotate_90_degrees, e=e,
    options={'rectangle': rectangle_2})

ap.save_overall_html(
    dest_dir_path='bind_and_trigger_custom_event_basic_usage/')
```

<iframe src="static/bind_and_trigger_custom_event_basic_usage/index.html" width="250" height="150"></iframe>


## bind_custom_event API

<!-- Docstring: apysc._event.custom_event_interface.CustomEventInterface.bind_custom_event -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `bind_custom_event(self, custom_event_type:Union[apysc._event.custom_event_type.CustomEventType, str], handler:Callable[[Any, Any], NoneType], e:apysc._event.event.Event, *, options:Union[Any, NoneType]=None, in_handler_head_expression:str='') -> str`<hr>

**[Interface summary]** Add a custom event listener setting.<hr>

**[Parameters]**

- `custom_event_type`: CustomEventType or str
  - Target custom event type.
- `handler`: _Handler
  - Callable that this instance calls when its event's dispatching.
- `e`: Event
  - Event instance.
- `options`: dict or None, default None
  - Optional arguments dictionary to be passed to a handler.
- `in_handler_head_expression`: str, default ''
  - Optional expression to be added at the handler function's head position.

<hr>

**[Returns]**

- `name`: str
  - Handler's name.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_custom_event(
...         e: ap.Event[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> e: ap.Event = ap.Event(this=rectangle)
>>> _ = rectangle.bind_custom_event(
...     custom_event_type='my_custom_event',
...     handler=on_custom_event, e=e)
>>> # Do something here and then trigger the custom event
>>> rectangle.trigger_custom_event(
...     custom_event_type='my_custom_event')
```

<hr>

**[References]**

- [About the handler options' type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

## trigger_custom_event API

<!-- Docstring: apysc._event.custom_event_interface.CustomEventInterface.trigger_custom_event -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `trigger_custom_event(self, custom_event_type:Union[apysc._event.custom_event_type.CustomEventType, str]) -> None`<hr>

**[Interface summary]** Add a custom event trigger setting.<hr>

**[Parameters]**

- `custom_event_type`: CustomEventType or str
  - Target custom event type.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_custom_event(
...         e: ap.Event[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> e: ap.Event = ap.Event(this=rectangle)
>>> _ = rectangle.bind_custom_event(
...     custom_event_type='my_custom_event',
...     handler=on_custom_event, e=e)
>>> # Do something here and then trigger the custom event
>>> rectangle.trigger_custom_event(
...     custom_event_type='my_custom_event')
```