# `apysc._event.handler_circular_calling_util` docstrings

## Module summary

Handler circular calling related utilities.

## `_append_handler_name_to_last_of_list` function docstring

Append a specified handler's name to the last of the list if the last one is an other handler's name. This function is used to unify last value regardless of `HandlerScope` setting.<hr>

**[Parameters]**

- `handler_name`: str
  - Targer handler name.
- `handler_names`: list of str
  - List to be appended.

<hr>

**[Returns]**

- `handler_names`: list of str
  - Result list value.

## `_get_same_name_prev_data` function docstring

Get previous handler name and variable name values of the previous same name (but the suffix number is different) handler from the current stack.<hr>

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

Get a previous same name (but the suffix number is different) handler's name from the current stack.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler's name.

<hr>

**[Returns]**

- `same_name_prev_hadler_name`: str
  - A previous same name (but the suffix number is different) handler's name.

## `_get_same_name_prev_variable_name` function docstring

Get a previous same name (but the suffix number is different) handler binded variable name from the current stack.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler's name.

<hr>

**[Returns]**

- `prev_variable_name`: str
  - A previous handler binded instance's variable name.

## `_is_already_saved_circular_calling` function docstring

Get a boolean indicating whether a specified handler name has been already saved as the circular calling handler or not.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler's name.

<hr>

**[Returns]**

- `result`: bool
  - If a specified handler name has already been saved as the circular calling handler then True will be returned

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
  - A previous handler's name. If there is no previous one, then blank string will be returned.

## `get_prev_variable_name` function docstring

Get a previous handler binded instance's variable name if a specified handler is a circular calling handler.<hr>

**[Parameters]**

- `handler_name`: str
  - Target handler's name.

<hr>

**[Returns]**

- `prev_variable_name`: str
  - A previous handler binded instance's variable name. If there is no previous (same handler's name prefix) one then blank string will be returned.

## `is_handler_circular_calling` function docstring

Get a boolean value whether a specified handler is a circular call or not.<hr>

**[Parameters]**

- `handler_name`: str
  - Targer handler name.

<hr>

**[Returns]**

- `result`: bool
  - If a specified handler is a circular call, True will be returned.