# `apysc._event.enter_frame_mixin` docstrings

## Module summary

Class implementation for the enter frame mix-in.

## `EnterFrameMixIn` class docstring

### `_append_enter_frame_expression` method docstring

Append an enter frame expression string.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler's name.
- `fps`: FPS
  - Frame per second to set.
- `is_stopped`: Boolean
  - A boolean to control an animation loop.

### `_initialize_enter_frame_handlers_if_not_initialized` method docstring

Initialize the `_enter_frame_handlers`'s attribute if this interface has not initialized it yet.

### `_initialize_is_stopped_settings_if_not_initialized` method docstring

Initialize the `_is_stopped_settings`'s attribute if this interface has not initialized it yet.

### `enter_frame` method docstring

Add an enter frame event listener setting.<hr>

**[Parameters]**

- `handler`: Callable[[EnterFrameEvent, _Options], None]
  - A handler function to handle the enter frame event.
- `fps`: FPS, default FPS.FPS_60
  - Frame per second to set.
- `options`: Optional[_Options], optional
  - Optional arguments to pass to a handler function.

## `_HandlerSettings` class docstring