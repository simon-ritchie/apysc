# `apysc._validation.arg_validation_decos` docstrings

## Module summary

This module is for the argument validations' decorators.

## `not_empty_string` function docstring

Set the validation to check that a specified argument's string is not empty.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.
- `arg_name`: str
  - A target argument name to check.

<hr>

**[Returns]**

- `_wrapped`: Callable
  - Wrapped callable object.