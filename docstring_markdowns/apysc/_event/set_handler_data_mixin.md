# `apysc._event.set_handler_data_mixin` docstrings

## Module summary

Class implementation for the `_set_handler_data` mix-in.

## `SetHandlerDataMixIn` class docstring

### `_set_handler_data` method docstring

Set a handler's data to the given dictionary.<hr>

**[Parameters]**

- `handler`: Callable[[_EventClass, _Options], None]
  - Callable that this instance calls when dispatching.
- `handlers_dict`: Dict[str, HandlerData]
  - Dictionary that this instance sets a handler's data.
- `options`: Optional[_Options]
  - Optional arguments dictionary that this instance passes to a handler.