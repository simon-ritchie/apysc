# `apysc._display.svg_text` docstrings

## Module summary

Class implementation for a SVG text.

## `SVGText` class docstring

### `__init__` method docstring

The class for a SVG text.<hr>

**[Parameters]**

- `text`: Union[str, String]
  - A text to use in this class.
- `x`: float or Number, default 0.0
  - X-coordinate to start drawing.
- `y`: float or Number, default 0.0
  - Y-coordinate to start drawing.
- `fill_color`: str or String, default '#666'
  - A fill-color to set.
- `fill_alpha`: float or Number, default 1.0
  - A fill-alpha to set.
- `line_color`: str or String, default ''
  - A line-color to set.
- `line_alpha`: float or Number, default 1.0
  - A line-alpha to set.
- `line_thickness`: int or Int, default 1
  - A line-thickness (line-width) to set.
- `parent`: ChildMixIn or None, default None
  - A parent instance to add this instance. If a specified value is None, this interface uses a stage instance.
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

### `__repr__` method docstring

Get a string representation of this instance (for the sake of debugging).<hr>

**[Returns]**

- `repr_str`: str
  - This interface returns a type name and variable name (e.g., `SVGText("<variable_name>")`).

### `_append_constructor_expression` method docstring

Append a constructor expression string.

### `_set_text_value` method docstring

Set a text value.<hr>

**[Parameters]**

- `text`: Union[str, String]
  - A target text.

<hr>

**[Returns]**

- `text_`: String
  - A set text.