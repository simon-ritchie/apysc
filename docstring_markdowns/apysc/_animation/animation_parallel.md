# `apysc._animation.animation_parallel` docstrings

## Module summary

Class implementation for the parallel animation value.

## `AnimationParallel` class docstring

The parallel animation setting class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> animation: ap.AnimationParallel = rectangle.animation_parallel(
...     animations=[
...         rectangle.animation_x(x=100),
...         rectangle.animation_fill_color(fill_color='#f0a'),
...         rectangle.animation_fill_alpha(alpha=0.5),
...     ],
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... )
>>> _ = animation.start()
```

<hr>

**[References]**

- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

### `__init__` method docstring

The parallel animation setting class.<hr>

**[Parameters]**

- `target`: VariableNameInterface
  - A target instance of the animation target (e.g., `DisplayObject` instance).
- `animations`: list of AnimationBase
  - Target animations (e.g., `AnimationX`, `AnimationFillColor`).
- `duration`: int or Int, default 3000
  - Milliseconds before an animation ends.
- `delay`: int or Int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Raises]**

- ValueError: <br> ・If the animations's target is not unified. <br> ・If there are changed `duration`, `delay`, or `easing` animation settings in the `animations` list.

### `_get_animation_func_expression` method docstring

Get a animation function expression.<hr>

**[Returns]**

- `expression`: str
  - Animation function expression.

### `_get_complete_event_in_handler_head_expression` method docstring

Get an expression to be inserted into the complete event handler's head.<hr>

**[Returns]**

- `expression`: str
  - An expression to be inserted into the complete event handler's head.

### `_make_animation_attr_exp` method docstring

Make an animation attribute expression string.<hr>

**[Parameters]**

- `attr_strs`: list of str
  - Target attribute strings.

<hr>

**[Returns]**

- `expression`: str
  - Created attribute expression string.

### `_validate_animation_targets_are_unified` method docstring

Validate whether the specified animation's targets are unified.<hr>

**[Raises]**

- ValueError: If the specified animation targets are not unified.

### `_validate_animations_delay_are_default_vals` method docstring

Validate whether the animations delay settings are default values (not changed).<hr>

**[Raises]**

- ValueError: If there is an animation target that is changed delay setting.

### `_validate_animations_duration_are_default_vals` method docstring

Validate whether the animations duration settings are default values (not changed).<hr>

**[Raises]**

- ValueError: If there is an animation target that is changed duration setting.

### `_validate_animations_easing_are_default_vals` method docstring

Validate whether the animations easing settings are default values (not changed).<hr>

**[Raises]**

- ValueError: If there is an animation target that is changed easing setting.