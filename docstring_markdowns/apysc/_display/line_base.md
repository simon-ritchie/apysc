# `apysc._display.line_base` docstrings

## Module summary

Base class implementation for each lines.

### `__repr__` method docstring

Get a string representation of this instance (for the sake of debugging).

### `_append_basic_vals_expression` method docstring

Append basic values expression to specified one.<hr>

**[Parameters]**

- `expression`: str
  - Target expression.
- `indent_num`: int
  - Indentation number.

<hr>

**[Returns]**

- `expression`: str
  - After appending expression.

### `_set_initial_basic_values` method docstring

Set initial basic values (fill color, line thickness, and so on).<hr>

**[Parameters]**

- `parent`: Graphics
  - Graphics instance to link this graphic.

### `_set_line_setting_if_not_none_value_exists` method docstring

If a line setting (dot, dash, or something else) with a value other than None exists, set that value to the attribute.<hr>

**[Parameters]**

- `parent_graphics`: Graphics
  - Parent Graphics instance.