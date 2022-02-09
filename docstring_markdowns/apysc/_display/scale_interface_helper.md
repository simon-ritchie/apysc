# apysc._display.scale_interface_helper docstrings

## Module summary

Helper module for the scale interfaces.

## get_coordinate_key_for_expression function docstring

Get a key string for the expression from the x or y coordinate.<hr>

**[Parameters]**

- `coordinate`: int or Int
  - X or y coordinate.

<hr>

**[Returns]**

- `key_exp_str`: ExpressionString
  - Key expression string.

## get_scale_updating_expression function docstring

Get a scale updating expression string from a specified coordinate.<hr>

**[Parameters]**

- `coordinate`: Int
  - X or y coordinate.
- `scale_dict`: Dictionary
  - Scale value dictionary.
- `interface_variable_name`: str
  - Scale interface instance variable name.
- `coordinate_type`: CoordinateType
  - Coordinate type to identify the x or y target.

<hr>

**[Returns]**

- `expression`: str
  - A scale updating expression string.

## CoordinateType class docstring

An enumeration.