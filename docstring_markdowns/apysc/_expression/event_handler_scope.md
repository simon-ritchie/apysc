# `apysc._expression.event_handler_scope` docstrings

## Module summary

This module is for the event handler's expression scope interfaces implementations.

## `_decrement_scope_count` function docstring

Decrement current scope count.

## `_delete_handler_calling_stack` function docstring

Delete the handler calling stack data from the SQLite.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler's name.

## `_increment_scope_count` function docstring

Increment current scope count.

## `_save_current_scope_count` function docstring

Save current scope count.<hr>

**[Parameters]**

- `count`: int
  - Scope count to save.

## `_save_handler_calling_stack` function docstring

Save the handler calling stack data to the SQLite.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler's name.
- `instance`: VariableNameInterface
  - Instance will be binded the target handler.

## `get_current_event_handler_scope_count` function docstring

Get a current event handler's scope count.<hr>

**[Returns]**

- `scope_count`: int
  - Current event handler's scope count. If normal handler's call, then this interface returns 1, or call the other handler in handler's function, then this interface returns 2 or more count.

## `remove_suffix_num_from_handler_name` function docstring

Remove the suffix number from a specified handler name.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler's name.

<hr>

**[Returns]**

- `handler_name`: str
  - Result handler's name.

## `HandlerScope` class docstring

Class for a handler scope. The apysc uses this class at a with-statement.

### `__enter__` method docstring

Enter and set an event handler scope setting.

### `__exit__` method docstring

Exit and remove an event handler scope setting.<hr>

**[Parameters]**

- `*args`: list
  - Positional arguments.

### `__init__` method docstring

Class for a handler scope. The apysc uses this class at a with-statement.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler's name.
- `instance`: VariableNameInterface
  - Instance will be binded the target handler.

## `TemporaryNotHandlerScope` class docstring

Class temporarily sets up a scope that is not a handler. The apysc uses this at a with-statement.

### `__enter__` method docstring

Enter and set the scope count to zero.

### `__exit__` method docstring

Exit and revert the scope count.<hr>

**[Parameters]**

- `*args`: list
  - Positional arguments.

### `__init__` method docstring

Class temporarily sets up a scope that is not a handler. The apysc uses this at a with-statement.