# apysc._animation.animation_reverse_interface docstrings

## Module summary

Class implementation for the animation_reverse interface.

### animation_reverse method docstring

Reverse the all running animations.<hr>

**[Notes]**

Suppose you call this interface multiple times and animations reach the beginning or end of the animation. In that case, this interface ignores the reverse instruction. This behavior means that the same interval's timer tick reverse setting does not work correctly (since the same interval setting reaches the animation start).<hr>

**[Examples]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
>>> def on_timer(
...         e: ap.TimerEvent,
...         options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options['rectangle']
...     rectangle.animation_reverse()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_x(
...     x=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
>>> options: RectOptions = {'rectangle': rectangle}
>>> ap.Timer(on_timer, delay=750, options=options).start()
```

<hr>

**[References]**

- [animation_reverse interface document](https://simon-ritchie.github.io/apysc/animation_reverse.html)