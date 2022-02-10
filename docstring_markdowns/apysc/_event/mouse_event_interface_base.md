# `apysc._event.mouse_event_interface_base` docstrings

## Module summary

Class implementation for each mouse event interface's base class.

## `MouseEventInterfaceBase` class docstring

### `_append_mouse_event_binding_expression` method docstring

Append a mouse event binding expression.<hr>

**[Parameters]**

- `name`: str
  - Handler's name.
- `mouse_event_type`: MouseEventType
  - Event type to bind.

### `_set_mouse_event_handler_data` method docstring

Set a handler's data to the given dictionary.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable would be called when event is dispatched.
- `handlers_dict`: dict
  - Dictionary to be set handler's data.
- `options`: dict or None
  - Optional arguments dictionary to be passed to handler.

### `_unbind_all_mouse_events` method docstring

Unbind specified all mouse event type's event.<hr>

**[Parameters]**

- `mouse_event_type`: MouseEventType
  - Event type to unbind.
- `handlers_dict`: dict
  - Dictionary that has handler's data.

### `_unbind_mouse_event` method docstring

Unbind specified handler's mouse event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.
- `mouse_event_type`: MouseEventType
  - Event type to unbind.
- `handlers_dict`: dict
  - Dictionary that has handler's data.