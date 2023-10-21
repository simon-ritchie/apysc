# `apysc._display.svg_text_span` docstrings

## Module summary

Class implementation for an SVG text-span.

## `_get_init_fill_alpha_num` function docstring

Get an initial fill-alpha number.<hr>

**[Parameters]**

- `fill_alpha`: Optional[Union[float, Number]]
  - A fill-alpha setting.

<hr>

**[Returns]**

- `fill_alpha_`: Union[float, Number]
  - If the specified value is None, this interface returns a 1.0 number.

## `_get_init_fill_color` function docstring

Get an initial fill-color.<hr>

**[Parameters]**

- `fill_color`: Optional[Color]
  - A fill-color setting.

<hr>

**[Returns]**

- `fill_color_`: Color
  - If the specified value is None, this interface returns the COLORLESS constant.

## `_get_init_line_alpha_num` function docstring

Get an initial line-alpha number.<hr>

**[Parameters]**

- `line_alpha`: Optional[Union[float, Number]]
  - A line-alpha setting.

<hr>

**[Returns]**

- `line_alpha_`: Union[float, Number]
  - If the specified value is None, this interface returns a 1.0 number.

## `_get_init_line_color` function docstring

Get an initial line-color.<hr>

**[Parameters]**

- `line_color`: Optional[Color]
  - A line-color.

<hr>

**[Returns]**

- `line_color_`: Color
  - If the specified value is None, this interface returns the COLORLESS constant.

## `_get_init_line_thickness_num` function docstring

Get an initial line-thickness (line-width) number.<hr>

**[Parameters]**

- `line_thickness`: Optional[Union[int, Int]]
  - A line-thickness (line-width) setting.

<hr>

**[Returns]**

- `line_thickness_`: Union[int, Int]
  - If the specified value is None, this interface returns 1 number.

## `SVGTextSpan` class docstring

The class for an SVG text-span (the child class of `SVGText`).<hr>

**[Notes]**

 ・If style settings are `None`, its styles inherit parent style settings.<hr>

**[References]**

- [SVGText class](https://simon-ritchie.github.io/apysc/en/svg_text.html)
- [SVGTextSpan class](https://simon-ritchie.github.io/apysc/en/svg_text_span.html)

### `__init__` method docstring

The class for an SVG text-span (the child class of `SVGText`).<hr>

**[Parameters]**

- `text`: Union[str, String]
  - A text to use in this class.
- `font_size`: Optional[Union[int, Int]], optional
  - A font-size setting.
- `font_family`: Optional[Union[Array[String], List[str]]], optional
  - A font-family setting. Each string in an array needs to be a font name (e.g., `Times New Roman`).
- `fill_color`: Optional[Color], optional
  - A fill-color setting.
- `fill_alpha`: Optional[Union[float, Number]], optional
  - A fill-alpha setting.
- `line_color`: Optional[Color], optional
  - A line-color setting.
- `line_alpha`: Optional[Union[float, Number]], optional
  - A line-alpha setting.
- `line_thickness`: Optional[Union[int, Int]], optional
  - A line-thickness (line-width) to set.
- `bold`: Optional[Union[bool, Boolean]], optional
  - A boolean, whether this text is a bold style or not.
- `italic`: Optional[Union[bool, Boolean]], optional
  - A boolean, whether a text is an italic style or not (normal).
- `delta_x`: Union[float, Number], optional
  - A coordinate delta-x setting. Notes: This setting also changes a coordinate of subsequent `SVGTextSpan`'s instance.
- `delta_y`: Union[float, Number], optional
  - A coordinate delta-y setting. Notes: This setting also changes a coordinate of subsequent `SVGTextSpan`'s instance.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Notes]**

 ・If style settings are `None`, its styles inherit parent style settings.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     background_color=ap.Color("#333"), stage_width=200, stage_height=50
... )
>>> svg_text: ap.SVGText = ap.SVGText.create_with_svg_text_spans(
...     text_spans=[
...         ap.SVGTextSpan(text="Hello, "),
...         ap.SVGTextSpan(text="Hello, ", font_size=14),
...     ],
...     font_size=20,
...     fill_color=ap.Color("#0af"),
... )
```

<hr>

**[References]**

- [SVGText class](https://simon-ritchie.github.io/apysc/en/svg_text.html)
- [SVGTextSpan class](https://simon-ritchie.github.io/apysc/en/svg_text_span.html)

### `__repr__` method docstring

Get a string representation of this instance (for the sake of debugging).<hr>

**[Returns]**

- `repr_str`: str
  - This interface returns a type name and variable name (e.g., `SVGTextSpan("<variable_name>")`).

### `_append_constructor_expression` method docstring

Append a constructor expression string.

### `_initialize_with_base_value` method docstring

Initialize this class with a base value(s).<hr>

**[Returns]**

- `svg_text_span`: SVGTextSpan
  - An initialized text span instance.