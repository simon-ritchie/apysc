# `apysc._validation.string_validation` docstrings

## Module summary

String's validation implementations.

## `validate_apysc_string_type` function docstring

Validate whether the specified argument is the apysc's `String` type or not.<hr>

**[Parameters]**

- `string`: Any
  - The target string to check.

<hr>

**[Returns]**

- `string`: String
  - An apysc's string.

<hr>

**[Raises]**

- TypeError: If the specified argument is not the apysc's `String` type.

## `validate_builtin_string_type` function docstring

Validate a specified string's type is Python built-in's str.<hr>

**[Parameters]**

- `string`: str
  - A string to check.
- `additional_err_msg`: str, optional
  - An additional error message to display.

<hr>

**[Raises]**

- ValueError: <br> ・If a non-string value is specified.

## `validate_not_empty_string` function docstring

Validate whether a specified string is not empty.<hr>

**[Parameters]**

- `string`: String or str
  - String to check.
- `additional_err_msg`: str, optional
  - An additional error message to display.

<hr>

**[Raises]**

- ValueError: <br> ・If empty string ('' or "") is specified. <br> ・If specified value is not str type.

## `validate_string_type` function docstring

Validate a specified string's type is str.<hr>

**[Parameters]**

- `string`: String or str
  - A string to check.
- `additional_err_msg`: str, optional
  - An additional error message to display.

<hr>

**[Raises]**

- ValueError: <br> ・If a non-string value is specified.