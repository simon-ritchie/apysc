# `apysc._validation.handler_validation` docstrings

## Module summary

This module is for the handler interfaces' validation implementations.

## `_remove_docstring_from_source` function docstring

Remove a docstring from a specified source code string.<hr>

**[Parameters]**

- `docstring`: Optional[str]
  - A handler's docstring.
- `source`: str
  - A handler's source code string.

<hr>

**[Returns]**

- `source`: str
  - A result source code string.

## `_remove_handlers_name_and_args_from_source` function docstring

Remove a handler's keyword, name, arguments, and return values type annotations from a specified source string.<hr>

**[Parameters]**

- `source`: str
  - A source string.

<hr>

**[Returns]**

- `source`: str
  - A result source string.

## `_remove_type_annotation_from_source_variable` function docstring

Remove variables' type annotations from a specified source code string.<hr>

**[Parameters]**

- `source`: str
  - A handler's source code string.

<hr>

**[Returns]**

- `source`: str
  - A result source code string.

## `validate_handler_args_num` function docstring

Validate specified handler's arguments number.<hr>

**[Parameters]**

- `handler`: Callable
  - A target handler to validate.
- `additional_err_msg`: str, optional
  - An additional error message to display.

<hr>

**[Raises]**

- ValueError: <br> ・If handler's arguments number is not 2.
- TypeError: <br> ・If a specified handler is not callable.

## `validate_in_handler_assignment` function docstring

Validate whether there isn't an assignment of the basic type values (e.g., ap.Int, ap.String) in a specified handler's source.<hr>

**[Parameters]**

- `handler`: Callable
  - A target handler's callable object.

<hr>

**[Raises]**

- InvalidAssignmentInHandler: If using a prohibited assignment in a handler's code.

## `validate_options_type` function docstring

Validate a specified options type.<hr>

**[Parameters]**

- `options`: Any
  - Target options value.
- `additional_err_msg`: str, optional
  - An additional error message to display.

<hr>

**[Raises]**

- TypeError: If a specified options type is not the dictionary or None.

## `InvalidAssignmentInHandler` class docstring