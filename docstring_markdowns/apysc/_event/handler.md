# apysc._event.handler docstrings

## Module summary

Class implementation for handler.

## _append_in_handler_head_expression function docstring

Append an in-handler head expression if it is not blank.<hr>

**[Parameters]**

- `in_handler_head_expression`: str
  - Optional expression to be added at the handler function's head position if it is not blank.

## append_handler_expression function docstring

Append a handler's expression.<hr>

**[Parameters]**

- `handler_data`: HandlerData
  - Target handler's data to append.
- `handler_name`: str
  - Target handler's name.
- `e`: Event
  - Created event instance.
- `in_handler_head_expression`: str, default ''
  - Optional expression to be added at the handler function's head position.

## append_unbinding_all_expression function docstring

Append all events unbinding expression.<hr>

**[Parameters]**

- `this`: VariableNameInterface
  - Instance that events are binded.
- `mouse_event_type`: MouseEventType
  - Event type to unbind.

## append_unbinding_expression function docstring

Append event unbinding expression.<hr>

**[Parameters]**

- `this`: VariableNameInterface
  - Instance that event is binded.
- `handler_name`: str
  - Target handler's name.
- `mouse_event_type`: MouseEventType
  - Event type to unbind.

## get_handler_name function docstring

Get a handler name.<hr>

**[Parameters]**

- `handler`: _Handler
  - Target handler.
- `instance`: VariableNameInterface
  - Instance to bind target handler.

<hr>

**[Returns]**

- `handler_name`: str
  - Handler name (method path + class name (if handler is method) + function or method name) + instance's variable name.