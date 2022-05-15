# `apysc._validation.arg_validation_decos` docstrings

## Module summary

This module is for the argument validations' decorators.

## `not_empty_string` function docstring

Set the validation to check a specified argument's string is not empty.<hr>

**[Parameters]**

- `arg_name`: str
  - A target argument name to check.

<hr>

**[Returns]**

- `_wrapped`: Callable
  - Wrapped callable object.

<hr>

**[Notes]**

This decorator function checks when a code passes an argument as a keyword argument.