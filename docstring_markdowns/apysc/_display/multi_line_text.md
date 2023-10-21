# `apysc._display.multi_line_text` docstrings

## Module summary

The class implementation for the `MultiLineText` class.

## `MultiLineText` class docstring

### `__init__` method docstring

The class implementation for a multiline text element.<hr>

**[Parameters]**

- `text`: Union[str, String]
  - Text to display. An HTML tag is available.
- `width`: Union[int, Int]
  - Width of the text to wrap.
- `variable_name_suffix`: str, default ""
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

### `_initialize_with_base_value` method docstring

Initialize this class with a base value(s).<hr>

**[Returns]**

- `text`: MultiLineText
  - An initialized instance.