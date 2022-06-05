# `apysc._validation.bool_validation` docstrings

## Module summary

Boolean value's validation implementations.

## `validate_bool` function docstring

Validate whether a specified value is `bool` or `Boolean` type.<hr>

**[Parameters]**

- `value`: bool or Boolean
  - A boolean value to check.
- `additional_err_msg`: str, optional
  - An additional error message to display.

<hr>

**[Raises]**

- ValueError: If a specified value isn't the `bool` or `Boolean` type.

## `validate_builtin_bool` function docstring

Validate whether a specified value is the built-in's `bool` type.<hr>

**[Parameters]**

- `value`: bool
  - A boolean value to check.
- `additional_err_msg`: str, optional
  - An additional error message to display.

<hr>

**[Raises]**

- ValueError: If a specified value isn't the `bool` type.