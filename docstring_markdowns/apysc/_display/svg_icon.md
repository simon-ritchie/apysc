# `apysc._display.svg_icon` docstrings

## Module summary

The SVG icon class implementation.

## `SvgIcon` class docstring

### `__init__` method docstring

The SVG icon class implementation.<hr>

**[Parameters]**

- `svg_icon_html`: str
  - An SVG icon html string. For example, "<svg xmlns="http://www.w3.org/2000/svg" ...>...</svg>"
- `x`: float or Number, optional
  - X-coordinate of the icon.
- `y`: float or Number, optional
  - Y-coordinate of the icon.
- `parent`: ChildMixIn or None, default None
  - A parent instance to add this instance. If the specified value is None, this interface uses a stage instance.
- `variable_name_suffix`: str, default ""
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

### `_append_constructor_expression` method docstring

Append a constructor expression.