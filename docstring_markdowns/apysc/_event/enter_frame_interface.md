# `apysc._event.enter_frame_interface` docstrings

## Module summary

Class implementation for the enter frame interface.

## `EnterFrameInterface` class docstring

### `_initialize_enter_frame_handlers_if_not_initialized` method docstring

Initialize the `_enter_frame_handlers` attribute if this interface has not initialized it yet.

### `enter_frame` method docstring

Add an enter frame event listener setting.<hr>

**[Parameters]**

- `handler`: Callable[[EnterFrameEvent, _Options], None]
  - An handler function to handle the enter frame event.
- `fps`: FPS, default FPS.FPS_60
  - Frame per second to set.
- `options`: Optional[_Options], optional
  - Optional arguments to pass to a handler function.

## `_HandlerSettings` class docstring