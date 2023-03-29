# `apysc._display.svg_text` docstrings

## Module summary

Class implementation for a SVG text.

## `SVGText` class docstring

### `__init__` method docstring

The class for an SVG text.<hr>

**[Parameters]**

- `text`: Union[str, String]
  - A text to use in this class.
- `font_size`: Union[int, Int], optional
  - A font-size setting.
- `font_family`: Optional[Union[Array[String], List[str]]], optional
  - A font-family setting. Each string in an array needs to be a font name (e.g., `Times New Roman`).
- `x`: float or Number, optional
  - X-coordinate to start drawing.
- `y`: float or Number, optional
  - Y-coordinate to start drawing (please see also the `Notes` section).
- `fill_color`: str or String, optional
  - A fill-color setting.
- `fill_alpha`: float or Number, optional
  - A fill-alpha setting.
- `line_color`: str or String, default ''
  - A line-color setting.
- `line_alpha`: float or Number, optional
  - A line-alpha setting.
- `line_thickness`: int or Int, optional
  - A line-thickness (line-width) setting.
- `leading`: float or Number, optional
  - A text-leading size.
- `align`: SVGTextAlign, default SVGTextAlign.LEFT
  - A text-align setting.
- `bold`: Union[bool, Boolean], optional
  - A boolean, whether this text is bold style or not.
- `italic`: Union[bool, Boolean], optional
  - A boolean, whether a text is an italic style or not (normal).
- `parent`: ChildMixIn or None, optional
  - A parent instance to add this instance. If a specified value is None, this interface uses a stage instance.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Notes]**

 ・SVGText's y-coordinate zero-position starts at the bottom of a text. So if you set y=0, a text becomes almost invisible.

### `__repr__` method docstring

Get a string representation of this instance (for the sake of debugging).<hr>

**[Returns]**

- `repr_str`: str
  - This interface returns a type name and variable name (e.g., `SVGText("<variable_name>")`).

### `_append_constructor_expression` method docstring

Append a constructor expression string.

### `_convert_text_spans_list_to_array` method docstring

Convert text spans' list to an array.<hr>

**[Parameters]**

- `text_spans`: Union[List[SVGTextSpan], Array[SVGTextSpan]]
  - Text spans.

<hr>

**[Returns]**

- `text_spans_`: Array[SVGTextSpan]
  - A converted array.

### `create_with_svg_text_spans` method docstring

Create an `SVGText` instance with specified text spans.<hr>

**[Parameters]**

- `text_spans`: Union[List[SVGTextSpan], Array[SVGTextSpan]]
  - Text spans.
- `font_size`: Union[int, Int], optional
  - A font-size setting for an overall text.
- `font_family`: Optional[Union[Array[String], List[str]]], optional
  - A font-family setting for an overall text. Each string in an array needs to be a font name (e.g., `Times New Roman`).
- `x`: Union[float, Number], optional
  - X-coordinate to start drawing.
- `y`: Union[float, Number], optional
  - Y-coordinate to start drawing (please see also the `Notes` section).
- `fill_color`: str or String, optional
  - A fill-color setting for an overall text.
- `fill_alpha`: float or Number, optional
  - A fill-alpha setting for an overall text.
- `line_color`: str or String, optional
  - A line-color setting for an overall text.
- `line_alpha`: float or Number, optional
  - A line-alpha setting.
- `line_thickness`: int or Int, optional
  - A line-thickness (line-width) setting.
- `leading`: float or Number, optional
  - A text-leading size for an overall text.
- `align`: SVGTextAlign, optional
  - A text-align setting for an overall text.
- `bold`: Union[bool, Boolean], optional
  - A boolean, whether this text is bold style or not.
- `italic`: Union[bool, Boolean], optional
  - A boolean, whether a text is an italic style or not (normal).
- `parent`: Optional[ChildMixIn], optional
  - A parent instance to add this instance. If a specified value is None, this interface uses a stage instance.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `svg_text`: SVGText
  - A created `SVGText` instance.

<hr>

**[Notes]**

 ・SVGText's y-coordinate zero-position starts at the bottom of a text. So if you set y=0, a text becomes almost invisible.