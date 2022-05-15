# `apysc._validation.handler_validation` docstrings

## Module summary

This module is for the handler interfaces' validation implementations.

## `validate_handler_args_num` function docstring

Validate specified handler's arguments number.<hr>

**[Parameters]**

- `handler`: Callable
  - A target handler to validate.

<hr>

**[Raises]**

- ValueError: <br> ・If handler's arguments number is not 2.

## `validate_options_type` function docstring

Validate a specified options type.<hr>

**[Parameters]**

- `options`: Any
  - Target options value.

<hr>

**[Raises]**

- TypeError: If a specified options type is not the dictionary or None.