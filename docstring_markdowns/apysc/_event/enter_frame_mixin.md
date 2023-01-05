# `apysc._event.enter_frame_mixin` docstrings

## Module summary

Class implementation for the enter frame mix-in.

## `_get_millisecond_interval_from_fps` function docstring

Get a millisecond interval value from a specified FPS.<hr>

**[Parameters]**

- `fps`: FPS
  - Frame per second.

<hr>

**[Returns]**

- `millisecond_interval`: Number
  - A created millisecond interval value.

## `EnterFrameMixIn` class docstring

### `_append_enter_frame_expression` method docstring

Append an enter frame expression string.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler's name.
- `millisecond_interval`: Number
  - Millisecond interval. This value depends on an FPS setting.
- `is_stopped`: Boolean
  - A boolean to control an animation loop.
- `loop_func_name`: str
  - A loop function name to set.
- `prev_time`: DateTime
  - Previous time to calculate the duration.

### `_append_enter_frame_rebinding_expression` method docstring

Append an enter-frame's rebinding expression string.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler's name.
- `fps`: FPS, default FPS.FPS_60
  - Frame per second to set.

### `_initialize_enter_frame_handlers_if_not_initialized` method docstring

Initialize the `_enter_frame_handlers`'s attribute if this instance has not initialized it yet.

### `_initialize_fps_millisecond_intervals_settings_if_not_initialized` method docstring

Initialize the `_fps_millisecond_intervals_settings`'s attribute if this instance has not initialized it yet.

### `_initialize_is_stopped_settings_if_not_initialized` method docstring

Initialize the `_is_stopped_settings`'s attribute if this instance has not initialized it yet.

### `_initialize_loop_func_name_settings_if_not_initialized` method docstring

Initialize the `_loop_func_name_settings`'s attribute if this instance has not initialized it yet.

### `_initialize_prev_time_settings_if_not_initialized` method docstring

Initialize the `_prev_time_settings`'s attribute if this instance has not initialized it yet.

### `enter_frame` method docstring

Add an enter frame event listener setting.<hr>

**[Parameters]**

- `handler`: Callable[[EnterFrameEvent, _Options], None]
  - A handler function to handle the enter frame event.
- `fps`: FPS, default FPS.FPS_60
  - Frame per second to set.
- `options`: Optional[_Options], optional
  - Optional arguments to pass to a handler function.

<hr>

**[Notes]**

If this is the second call of this interface and an argument is the same function, this interface ignores `options` argument (it changes only the running status and `fps` setting).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> rectangle: ap.Rectangle = ap.Rectangle(
...     x=50, y=50, width=50, height=50, fill_color="#0af"
... )
>>> def on_enter_frame(e: ap.EnterFrameEvent, options: dict) -> None:
...     rectangle.x += 1
>>> stage.enter_frame(handler=on_enter_frame, fps=ap.FPS.FPS_30)
```

<hr>

**[References]**

- [enter_frame interface](https://simon-ritchie.github.io/apysc/en/enter_frame.html)

### `unbind_enter_frame` method docstring

Unbind a specified handler's enter-frame event.<hr>

**[Parameters]**

- `handler`: Callable[[EnterFrameEvent, _Options], None]
  - Unbinding target callable.

<hr>

**[Raises]**

- _EnterFrameEventNotRegistered: If there is no unbinding target of a specified handler.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> rectangle: ap.Rectangle = ap.Rectangle(
...     x=50, y=50, width=50, height=50, fill_color="#0af"
... )
>>> def on_enter_frame(e: ap.EnterFrameEvent, options: dict) -> None:
...     rectangle.x += 1
>>> stage.enter_frame(handler=on_enter_frame, fps=ap.FPS.FPS_30)
>>> # Any implementations here...
>>> stage.unbind_enter_frame(handler=on_enter_frame)
```

<hr>

**[References]**

- [unbind_enter_frame and unbind_enter_frame_all interfaces](https://simon-ritchie.github.io/apysc/en/unbind_enter_frame_and_unbind_enter_frame_all.html)

### `unbind_enter_frame_all` method docstring

Unbind all enter-frame events.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> rectangle: ap.Rectangle = ap.Rectangle(
...     x=50, y=50, width=50, height=50, fill_color="#0af"
... )
>>> def on_enter_frame(e: ap.EnterFrameEvent, options: dict) -> None:
...     rectangle.x += 1
>>> stage.enter_frame(handler=on_enter_frame, fps=ap.FPS.FPS_30)
>>> # Any implementations here...
>>> stage.unbind_enter_frame_all()
```

<hr>

**[References]**

- [unbind_enter_frame and unbind_enter_frame_all interfaces](https://simon-ritchie.github.io/apysc/en/unbind_enter_frame_and_unbind_enter_frame_all.html)

## `_EnterFrameEventNotRegistered` class docstring