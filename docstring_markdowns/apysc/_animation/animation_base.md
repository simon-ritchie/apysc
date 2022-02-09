# `apysc._animation.animation_base` docstrings

## Module summary

Base class implementation for the animation.

## `AnimationBase` class docstring

### `__init__` method docstring

Base class for each animation setting.<hr>

**[Parameters]**

- `variable_name`: str
  - Variable name.

### `_get_animation_basic_expression` method docstring

Get an animation basic expression string.<hr>

**[Returns]**

- `expression`: str
  - An animation basic expression string.

### `_get_animation_complete_handler_expression` method docstring

Get an expression of the animation complete handlers setting.<hr>

**[Returns]**

- `expression`: str
  - Target expression string. e.g., ' .after(handler_name)'

<hr>

**[Notes]**

If multiple handlers are registered, then this method returns multiple lines expression.

### `_get_animation_func_expression` method docstring

Get an animation function expression.

### `_get_complete_event_in_handler_head_expression` method docstring

Get an expression to be inserted into the complete event handler's head.

### `_set_basic_animation_settings` method docstring

Set the basic animation settings.<hr>

**[Parameters]**

- `target`: VariableNameInterface
  - A target instance of the animation target (e.g., `DisplayObject` instance).
- `duration`: int or Int, default 3000
  - Milliseconds before an animation ends.
- `delay`: int or Int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting. If None, Linear calculation is used.

### `_validate_animation_not_started` method docstring

Validate whether an animation has not already started.<hr>

**[Raises]**

- Exception: If an animation has already started.

### `animation_complete` method docstring

Add an animation complete event listener setting.<hr>

**[Parameters]**

- `handler`: _Handler
  - A callable that an instance calls when an animation is complete.
- `options`: dict or None, default None
  - Optional arguments dictionary to be passed to a handler.

<hr>

**[Returns]**

- `self`: AnimatonBase
  - This instance.

<hr>

**[Raises]**

- Exception: If calling this interface after an animation starts

<hr>

**[Notes]**

This interface can only use before an animation starts<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_animation_complete(
...         e: ap.AnimationEvent[ap.Rectangle],
...         options: dict) -> None:
...     ap.trace('Animation completed!')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_x(
...     x=100,
... ).animation_complete(on_animation_complete).start()
```

<hr>

**[References]**

- [AnimationBase class animation_complete interface document](https://simon-ritchie.github.io/apysc/animation_complete.html)
- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### `start` method docstring

Start an animation with current settings.<hr>

**[Returns]**

- `self`: AnimatonBase
  - This instance.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_x(x=100).start()
```

<hr>

**[References]**

- [AnimationBase class start interface](https://simon-ritchie.github.io/apysc/animation_base_start.html)