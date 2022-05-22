# `apysc._validation.color_validation` docstrings

## Module summary

Validations related to color.

## `validate_hex_color_code_format` function docstring

Validate a specified hexadecimal color code format.<hr>

**[Parameters]**

- `hex_color_code`: str
  - Hexadecimal color code (not including '#'). e.g., 'ff0000', '666', '0'
- `additional_err_msg`: str, optional
  - An additional error message to display.

<hr>

**[Raises]**

- ValueError: If invalid hex color code specified.