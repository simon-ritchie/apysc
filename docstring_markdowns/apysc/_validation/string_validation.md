# `apysc._validation.string_validation` docstrings

## Module summary

String's validation implementations.

## `validate_not_empty_string` function docstring

Validate whether a specified string is not empty.<hr>

**[Parameters]**

- `string`: String or str
  - String to check.

<hr>

**[Raises]**

- ValueError: <br> ・If empty string ('' or "") is specified. <br> ・If specified value is not str type.

## `validate_string_type` function docstring

Validate specified string's type is str.<hr>

**[Parameters]**

- `string`: String or str
  - String to check.

<hr>

**[Raises]**

- ValueError: <br> ・If not string value is specified.