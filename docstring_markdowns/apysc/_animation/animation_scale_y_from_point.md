# `apysc._animation.animation_scale_y_from_point` docstrings

## Module summary

Class implementation for the scale-y from the given point animation value.

## `AnimationScaleYFromPoint` class docstring

The animation class for a scale-y from the given point.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> animation: ap.AnimationScaleYFromPoint
>>> animation = rectangle.animation_scale_y_from_point(
...     scale_y_from_point=0.5,
...     y=ap.Number(100),
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... )
>>> _ = animation.start()
```

<hr>

**[References]**

- [animation_scale_from_point interfaces](https://simon-ritchie.github.io/apysc/en/animation_scale_x_and_y_from_point.html)
- [Animation interfaces duration setting](https://simon-ritchie.github.io/apysc/en/animation_duration.html)
- [Animation interfaces delay setting](https://simon-ritchie.github.io/apysc/en/animation_delay.html)
- [Each animation interface return value](https://simon-ritchie.github.io/apysc/en/animation_return_value.html)
- [Sequential animation setting](https://simon-ritchie.github.io/apysc/en/sequential_animation.html)
- [animation_parallel interface](https://simon-ritchie.github.io/apysc/en/animation_parallel.html)
- [Easing enum](https://simon-ritchie.github.io/apysc/en/easing_enum.html)

### `__init__` method docstring

The animation class for a scale-y from the given point.<hr>

**[Parameters]**

- `target`: ScaleYFromPointMixIn
  - A target instance of the animation target (e.g., `Rectangle` instance).
- `scale_y_from_point`: float or Number
  - The final scale-y from the given point of the animation.
- `y`: float or Number
  - Y-coordinate.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Raises]**

- TypeError: If a specified target is not a ScaleXFromPointMixIn instance.

### `_get_animation_func_expression` method docstring

Get a animation function expression.<hr>

**[Returns]**

- `expression`: str
  - Animation function expression.

### `_get_complete_event_in_handler_head_expression` method docstring

Get an expression to insert into the heading of the complete event handler.<hr>

**[Returns]**

- `expression`: str
  - An expression to insert into the heading of the complete event handler.