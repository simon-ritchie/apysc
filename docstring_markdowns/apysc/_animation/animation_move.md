# `apysc._animation.animation_move` docstrings

## Module summary

Class implementation for the move animation value.

## `AnimationMove` class docstring

The animation class for moving x and y coordinates.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> animation: ap.AnimationMove = rectangle.animation_move(
...     x=100, y=150,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... )
>>> _ = animation.start()
```

<hr>

**[References]**

- [animation_move interface document](https://simon-ritchie.github.io/apysc/animation_move.html)
- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

### `__init__` method docstring

The animation class for moving x and y coordinates.<hr>

**[Parameters]**

- `target`: VariableNameInterface
  - A target instance of the animation target (e.g., `DisplayObject` instance).
- `x`: int or Int
  - Destination of the x-coordinate.
- `y`: int or Int
  - Destination of the y-coordinate.
- `duration`: int or Int, default 3000
  - Milliseconds before an animation ends.
- `delay`: int or Int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

### `_get_animation_func_expression` method docstring

Get a animation function expression.<hr>

**[Returns]**

- `expression`: str
  - Animation function expression.

### `_get_complete_event_in_handler_head_expression` method docstring

Get an expression to be inserted into the complete event handler's head.<hr>

**[Returns]**

- `expression`: str
  - An expression to insert into the complete event handler's head.