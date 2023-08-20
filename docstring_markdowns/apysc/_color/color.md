# `apysc._color.color` docstrings

## Module summary

The color class implementation.

## `Color` class docstring

### `__eq__` method docstring

Comparison method between two color values.<hr>

**[Parameters]**

- `other`: Color
  - The other color value.

<hr>

**[Returns]**

- `result`: Boolean
  - If the two color values are equal, this interface returns True.

### `__init__` method docstring

The color class implementation.<hr>

**[Parameters]**

- `value`: str or String
  - A hexadecimal color code string (e.g., '#000000').
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

### `__repr__` method docstring

Get a representation string of this instance.<hr>

**[Returns]**

- `repr_str`: str
  - Representation string of this instance.