# `apysc._animation.animation_reset_mixin` docstrings

## Module summary

Class implementation for the animation_reset mix-in.

## `AnimationResetMixIn` class docstring

### `animation_reset` method docstring

Stop all animations and reset.<hr>

**[Examples]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
...
>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options["rectangle"]
...     rectangle.animation_reset()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.animation_x(
...     x=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
>>> options: RectOptions = {"rectangle": rectangle}
>>> ap.Timer(on_timer, delay=750, options=options).start()
```

<hr>

**[References]**

- [animation_reset interface](https://simon-ritchie.github.io/apysc/en/animation_reset.html)