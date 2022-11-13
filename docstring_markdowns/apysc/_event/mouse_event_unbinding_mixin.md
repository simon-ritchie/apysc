# `apysc._event.mouse_event_unbinding_mixin` docstrings

## Module summary

Class implementation for mouse event unbingins-related mix-in.

## `MouseEventUnbindingMixIn` class docstring

### `_unbind_all_mouse_events` method docstring

Unbind specified all mouse event type's events.<hr>

**[Parameters]**

- `mouse_event_type`: MouseEventType
  - Event type to unbind.
- `handlers_dict`: dict
  - Dictionary that has handler's data.

### `_unbind_mouse_event` method docstring

Unbind a specified handler's mouse event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.
- `mouse_event_type`: MouseEventType
  - Event type to unbind.
- `handlers_dict`: dict
  - Dictionary that has handler's data.