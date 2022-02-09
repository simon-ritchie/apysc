# `apysc._time.timer` docstrings

## Module summary

Class implementation for the timer.

## `Timer` class docstring

Timer class to handle function calling at regular intervals.<hr>

**[Examples]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options['rectangle']
...     rectangle.x += 1
>>> def on_timer_complete(e: ap.TimerEvent, options: dict) -> None:
...     ap.trace('Timer completed!')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> options: RectOptions = {'rectangle': rectangle}
>>> timer: ap.Timer = ap.Timer(
...     on_timer, delay=ap.FPS.FPS_60, repeat_count=50,
...     options=options)
>>> _ = timer.timer_complete(on_timer_complete)
>>> timer.start()
```

<hr>

**[References]**

- [Timer document](https://simon-ritchie.github.io/apysc/timer.html)
- [TimerEvent class document](https://simon-ritchie.github.io/apysc/timer_event.html)
- [Timer class delay setting document](https://simon-ritchie.github.io/apysc/timer_delay.html)
- [FPS enum document](https://simon-ritchie.github.io/apysc/fps.html)
- [Timer class repeat_count setting](https://simon-ritchie.github.io/apysc/timer_repeat_count.html)

### `__init__` method docstring

Timer class to handle function calling at regular intervals.<hr>

**[Parameters]**

- `handler`: _Handler
  - A handler would be called at regular intervals.
- `delay`: Int or int or Number or float or FPS
  - A delay between each `Handler` calling in a millisecond or FPS value. If an `FPS` value is specified, this value becomes a millisecond calculated with that FPS value (e.g., if the `FPS_60` value is specified, then `delay` becomes 16.6666667).
- `repeat_count`: Int or int
  - Max count of a `Handler`'s calling. A timer stops if the `Handler`'s calling count has reached this value. If 0 is specified, then a timer loops forever.
- `options`: dict or None, default None
  - Optional arguments dictionary to pass a `Handler` callable.

<hr>

**[Examples]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options['rectangle']
...     rectangle.x += 1
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> options: RectOptions = {'rectangle': rectangle}
>>> _ = ap.Timer(
...     on_timer, delay=ap.FPS.FPS_60, options=options).start()
```

<hr>

**[References]**

- [Timer document](https://simon-ritchie.github.io/apysc/timer.html)
- [TimerEvent class document](https://simon-ritchie.github.io/apysc/timer_event.html)
- [Timer class delay setting document](https://simon-ritchie.github.io/apysc/timer_delay.html)
- [FPS enum document](https://simon-ritchie.github.io/apysc/fps.html)
- [Timer class repeat_count setting](https://simon-ritchie.github.io/apysc/timer_repeat_count.html)
- [About the handler options' type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### `_append_count_branch_expression` method docstring

Append the timer stopping expression by the counting.

### `_convert_delay_to_number` method docstring

Convert each type of delay value to a `Number` value.<hr>

**[Parameters]**

- `delay`: int or float or Int or Number or FPS
  - A delay between each handler's calling in milisecond or FPS value.

<hr>

**[Returns]**

- `delay`: Number
  - Converted delay value.

### `_get_stop_expression` method docstring

Get a stop interface expression string.<hr>

**[Parameters]**

- `indent_num`: int
  - Indentation number to append.

<hr>

**[Returns]**

- `expression`: str
  - Stop interface expression string.

### `_wrap_handler` method docstring

Wrap a handler to update a current count value when it is called.<hr>

**[Parameters]**

- `handler`: _Handler
  - Target handler.

<hr>

**[Returns]**

- `wrapped`: _Handler
  - Wrapped handler.

### `reset` method docstring

Reset the timer count and stop this timer.<hr>

**[Examples]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options['rectangle']
...     rectangle.x += 1
...     with ap.If(rectangle.x > 100):
...         timer: ap.Timer = e.this
...         timer.reset()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> options: RectOptions = {'rectangle': rectangle}
>>> _ = ap.Timer(
...     on_timer, delay=33.3, options=options).start()
```

<hr>

**[References]**

- [Timer class reset interface document](https://simon-ritchie.github.io/apysc/timer_reset.html)

### `start` method docstring

Start this timer.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_timer(e: ap.TimerEvent, options: dict) -> None:
...     pass
>>> _ = ap.Timer(
...     on_timer, delay=33.3, repeat_count=50).start()
```

<hr>

**[References]**

- [Timer class start and stop interfaces](https://simon-ritchie.github.io/apysc/timer_start_and_stop.html)

### `stop` method docstring

Stop this timer.<hr>

**[Examples]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options['rectangle']
...     rectangle.x += 1
...     with ap.If(rectangle.x > 100):
...         timer: ap.Timer = e.this
...         timer.stop()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> options: RectOptions = {'rectangle': rectangle}
>>> _ = ap.Timer(
...     on_timer, delay=33.3, options=options).start()
```

<hr>

**[References]**

- [Timer class start and stop interfaces document](https://simon-ritchie.github.io/apysc/timer_start_and_stop.html)

### `timer_complete` method docstring

Add a timer complete event listener setting.<hr>

**[Parameters]**

- `handler`: _Handler
  - A callable that a timer calls when complete.
- `options`: dict or None, default None
  - Optional arguments dictionary to be passed to a handler.

<hr>

**[Returns]**

- `name`: str
  - Handler's name.

<hr>

**[Examples]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options['rectangle']
...     rectangle.x += 1
>>> def on_timer_complete(
...         e: ap.TimerEvent, options: RectOptions) -> None:
...     ap.trace('Timer completed!')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> options: RectOptions = {'rectangle': rectangle}
>>> timer: ap.Timer = ap.Timer(
...     on_timer, delay=33.3, options=options)
>>> _ = timer.timer_complete(on_timer_complete)
>>> timer.start()
```

<hr>

**[References]**

- [Timer class timer_complete interface document](https://simon-ritchie.github.io/apysc/timer_complete.html)
- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)