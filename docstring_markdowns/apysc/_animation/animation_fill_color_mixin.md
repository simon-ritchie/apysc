# `apysc._animation.animation_fill_color_mixin` docstrings

## Module summary

Class implementation for the animation_fill_color mix-in.

## `AnimationFillColorMixIn` class docstring

### `animation_fill_color` method docstring

Set the fill color animation setting.<hr>

**[Parameters]**

- `fill_color`: str or String
  - The final fill color (hex color code) of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_fill_color`: AnimationFillColor
  - Created animation setting instance.

<hr>

**[Notes]**

To start this animation, you need to call the `start` method of the returned instance.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.animation_fill_color(
...     fill_color=ap.Color("#f0a"),
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_fill_color interface](https://simon-ritchie.github.io/apysc/en/animation_fill_color.html)
- [Animation interfaces duration setting](https://simon-ritchie.github.io/apysc/en/animation_duration.html)
- [Animation interfaces delay setting](https://simon-ritchie.github.io/apysc/en/animation_delay.html)
- [Each animation interface return value](https://simon-ritchie.github.io/apysc/en/animation_return_value.html)
- [Sequential animation setting](https://simon-ritchie.github.io/apysc/en/sequential_animation.html)
- [animation_parallel interface](https://simon-ritchie.github.io/apysc/en/animation_parallel.html)
- [Easing enum](https://simon-ritchie.github.io/apysc/en/easing_enum.html)