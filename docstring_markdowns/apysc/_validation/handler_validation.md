# `apysc._validation.handler_validation` docstrings

## Module summary

This module is for the handler interfaces' validation implementations.

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