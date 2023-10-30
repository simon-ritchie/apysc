# `apysc._display.multi_line_text` docstrings

## Module summary

The class implementation for the `MultiLineText` class.

## `MultiLineText` class docstring

### `__init__` method docstring

The class implementation for a multiline text element.<hr>

**[Parameters]**

- `text`: Union[str, String]
  - Text to display. An HTML tag is available.
- `x`: Union[float, Number], default 0
  - X-coordinate.
- `y`: Union[float, Number], default 0
  - Y-coordinate.
- `width`: Union[int, Int], default 200
  - Width of the text to wrap.
- `fill_color`: Color, default Colors.GRAY_666666
  - Text color.
- `fill_alpha`: Union[float, Number], default 1.0
  - Text alpha (opacity). The minimum value is 0.0 (transparent), and the maximum value is 1.0 (solid).
- `bold`: Union[bool, Boolean], default False
  - Whether to display the text in bold.
- `parent`: ChildMixIn or None, default None
  - A parent instance to add this instance. If the specified value is None, this interface uses a stage instance.
- `variable_name_suffix`: str, default ""
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

### `_initialize_with_base_value` method docstring

Initialize this class with a base value(s).<hr>

**[Returns]**

- `text`: MultiLineText
  - An initialized instance.