# `apysc._event.handler_circular_calling_util` docstrings

## Module summary

Handler circular calling related utilities.

## `_append_handler_name_to_last_of_list` function docstring

Append a specified handler's name to the list last if the last one is the other handler's name. This function is for the unifying last value regardless of the `HandlerScope` setting.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler name.
- `handler_names`: list of str
  - List to be appended.

<hr>

**[Returns]**

- `handler_names`: list of str
  - Result list value.

## `_get_same_name_prev_data` function docstring

Get a previous handler name and variable name values of the same previous name (but the suffix number is different) handler from the current stack.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler's name.

<hr>

**[Returns]**

- `prev_hadler_name`: str
  - A previous same name (but the suffix number is different) handler's name value.
- `prev_variable_name`: str
  - A previous variable name value.

<hr>

**[Raises]**

- ValueError: If there is no previous same name handler's name in the SQLite.

## `_get_same_name_prev_hadler_name` function docstring

Get the same previous name (but the suffix number is different) handler's name from the current stack.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler's name.

<hr>

**[Returns]**

- `same_name_prev_hadler_name`: str
  - A previous same name (but the suffix number is different) handler's name.

## `_get_same_name_prev_variable_name` function docstring

Get the same previous name (but the suffix number is different) handler's binding variable name from the current stack.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler's name.

<hr>

**[Returns]**

- `prev_variable_name`: str
  - A previous handler that binding instance's variable name.

## `_is_already_saved_circular_calling` function docstring

Get a boolean indicating whether the interface already has saved a handler name as the circular calling handler or not.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler's name.

<hr>

**[Returns]**

- `result`: bool
  - If the interface already saves a specified handler name as the circular calling handler, this interface returns True.

## `_read_handler_names` function docstring

Read the current handler names from the calling stack.<hr>

**[Returns]**

- `handler_names`: list of str
  - Target handler names.

## `_save_circular_calling_handler_name` function docstring

Save a circular calling handler name to the SQLite.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler's name.

## `get_prev_handler_name` function docstring

Get a previous handler's name of a specified handler's one if it is a circular calling handler.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler's name.

<hr>

**[Returns]**

- `prev_handler_name`: str
  - A previous handler's name. If there is no previous one, this interface returns a blank string.

## `get_prev_variable_name` function docstring

Get a previous handler binding instance's variable name if a specified handler is a circular calling's handler.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler's name.

<hr>

**[Returns]**

- `prev_variable_name`: str
  - A previous handler binding instance's variable name. If there is no previous (same handler's name prefix) one, this interface returns a blank string.

## `is_handler_circular_calling` function docstring

Get a boolean value whether a specified handler is a circular call or not.<hr>

**[Parameters]**

- `handler_name`: str
  - Targer handler name.

<hr>

**[Returns]**

- `result`: bool
  - If a specified handler is a circular call, this interface returns True.