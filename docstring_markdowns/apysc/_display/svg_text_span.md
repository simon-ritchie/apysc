# `apysc._display.svg_text_span` docstrings

## Module summary

Class implementation for an SVG text-span.

## `SVGTextSpan` class docstring

### `__init__` method docstring

The class for an SVG text-span (the child class of `SVGText`).<hr>

**[Parameters]**

- `text`: Union[str, String]
  - A text to use in this class.
- `font_size`: Union[int, Int], optional
  - A font-size setting.
- `font_family`: Optional[Union[Array[String], List[str]]], optional
  - A font-family setting. Each string in an array needs to be a font name (e.g., `Times New Roman`).
- `fill_color`: Union[str, String], optional
  - A fill-color to set.
- `fill_alpha`: Union[float, Number], optional
  - A fill-alpha to set.
- `line_color`: Union[str, String], optional
  - A line-color to set.
- `line_alpha`: Union[float, Number], optional
  - A line-alpha to set.
- `line_thickness`: Union[int, Int], optional
  - A line-thickness (line-width) to set.
- `bold`: Union[bool, Boolean], optional
  - A boolean, whether this text is bold style or not.
- `italic`: Union[bool, Boolean], optional
  - A boolean, whether a text is an italic style or not (normal).
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

### `__repr__` method docstring

Get a string representation of this instance (for the sake of debugging).<hr>

**[Returns]**

- `repr_str`: str
  - This interface returns a type name and variable name (e.g., `SVGTextSpan("<variable_name>")`).

### `_append_constructor_expression` method docstring

Append a constructor expression string.