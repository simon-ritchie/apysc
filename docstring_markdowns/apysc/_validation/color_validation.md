# `apysc._validation.color_validation` docstrings

## Module summary

Validations related to color.

## `validate_alpha_range` function docstring

Validate specified alpha (opacity) value's range.<hr>

**[Parameters]**

- `alpha`: float or Number
  - Opacity value to check.

<hr>

**[Raises]**

- ValueError: If specified opacity is out of 0.0 to 1.0 range.

## `validate_hex_color_code_format` function docstring

Validate a specified hexadecimal color code's format.<hr>

**[Parameters]**

- `hex_color_code`: str
  - Hexadecimal color code (not including '#'). e.g., 'ff0000', '666', '0'

<hr>

**[Raises]**

- ValueError: If invalid hex color code specified.