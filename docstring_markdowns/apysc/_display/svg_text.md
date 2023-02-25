# `apysc._display.svg_text` docstrings

## Module summary

Class implementation for a SVG text.

## `SVGText` class docstring

### `__init__` method docstring

The class for a SVG text.<hr>

**[Parameters]**

- `text`: Union[str, String]
  - A text to use in this class.
- `font_size`: Union[int, Int], optional
  - A font-size setting.
- `font_family`: Optional[Union[Array[String], List[str]]], optional
  - A font-family setting. Each string in an array needs to be a font name (e.g., `Times New Roman`).
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
- `leading`: float or Number, default 1.5
  - A text-leading size.
- `align`: SVGTextAlign, default SVGTextAlign.LEFT
  - A text-align setting.
- `bold`: Union[bool, Boolean], default False
  - A boolean whether this text is bold style or not.
- `italic`: Union[bool, Boolean], default False
  - A boolean indicating whether a text is italic style or not (normal).
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

### `_set_align` method docstring

Set a text-align setting.<hr>

**[Parameters]**

- `align`: SVGTextAlign
  - A text-align setting.

### `_set_bold` method docstring

Set a bold style setting.<hr>

**[Parameters]**

- `bold`: Union[bool, Boolean]
  - A boolean, whether a text is a bold style or not (normal).

### `_set_font_family` method docstring

Set a font-family value.<hr>

**[Parameters]**

- `font_family`: Optional[Array[String]]
  - A font-family setting.

### `_set_font_size_value` method docstring

Set a font-size value.<hr>

**[Parameters]**

- `font_size`: Union[int, Int]
  - A target font-size value.

### `_set_italic` method docstring

Set an italic style setting.<hr>

**[Parameters]**

- `italic`: Union[bool, Boolean]
  - A boolean whether a text is in an italic style or not (normal).

### `_set_leading` method docstring

Set a leading value.<hr>

**[Parameters]**

- `leading`: Union[float, Number]
  - A text-leading value.

### `_set_text_value` method docstring

Set a text value.<hr>

**[Parameters]**

- `text`: Union[str, String]
  - A target text.

<hr>

**[Returns]**

- `text_`: String
  - A set text.