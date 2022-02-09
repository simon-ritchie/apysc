# apysc._event.timer_event docstrings

## Module summary

Class implementation for the timer event.

## TimerEvent class docstring

Timer event class.<hr>

**[Examples]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options['rectangle']
...     rectangle.x += 1
...     with ap.If(rectangle.x >= 100):
...         timer: ap.Timer = e.this
...         timer.stop()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> options: RectOptions = {'rectangle': rectangle}
>>> ap.Timer(
...     on_timer, delay=ap.FPS.FPS_60, options=options,
... ).start()
```

<hr>

**[References]**

- [TimerEvent class document](https://simon-ritchie.github.io/apysc/timer_event.html)

### __init__ method docstring

Timer event class.<hr>

**[Parameters]**

- `this`: Timer
  - Target timer instance.

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
>>> ap.Timer(
...     on_timer, delay=ap.FPS.FPS_60, options=options,
... ).start()
```

<hr>

**[References]**

- [TimerEvent class document](https://simon-ritchie.github.io/apysc/timer_event.html)