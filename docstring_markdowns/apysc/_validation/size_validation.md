# `apysc._validation.size_validation` docstrings

## Module summary

Size's (width or height) common validation implementation.

## `validate_size_is_gt_zero` function docstring

Check whether a specified size is greater than zero or not.<hr>

**[Parameters]**

- `size`: Int or int
  - Target size (width or height) value.
- `err_msg`: str or None, default None
  - The error message which displays at error raised.

<hr>

**[Raises]**

- ValueError: If a specified size is less than or equal to zero.

## `validate_size_is_gte_zero` function docstring

Check whether a specified size is greater than or equal to zero or not.<hr>

**[Parameters]**

- `size`: Int or int
  - Target size (width or height) value.
- `err_msg`: str or None, default None
  - The error message which displays at error raised.

<hr>

**[Raises]**

- ValueError: If a specified size is less than zero.

## `validate_size_is_int` function docstring

Check whether a specified size is an integer or not.<hr>

**[Parameters]**

- `size`: Int or int
  - Target size (width or height) value.
- `err_msg`: str or None, default None
  - The error message that display at error raised.

<hr>

**[Raises]**

- ValueError: The error message which displays at error raised.