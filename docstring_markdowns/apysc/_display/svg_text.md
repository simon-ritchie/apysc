# `apysc._display.svg_text` docstrings

## Module summary

Class implementation for an SVG text.

## `SvgText` class docstring

The class for an SVG text.<hr>

**[Notes]**

 ・SvgText's y-coordinate zero-position starts at the bottom of a text. So if you set y=0, a text becomes almost invisible.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     background_color=ap.Color("#333"),
...     stage_width=200,
...     stage_height=50,
... )
>>> svg_text: ap.SvgText = ap.SvgText(
...     text="Hello, world!",
...     font_size=20,
...     fill_color=ap.Color("#0af"),
... )
>>> svg_text.text
String("Hello, world!")

>>> svg_text.font_size
Int(20)

>>> svg_text.fill_color
Color("#00aaff")
```

<hr>

**[References]**

- [SvgText class](https://simon-ritchie.github.io/apysc/en/svg_text.html)

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
- `line_color`: str or String, optional
  - A line-color setting.
- `line_alpha`: float or Number, optional
  - A line-alpha setting.
- `line_thickness`: int or Int, optional
  - A line-thickness (line-width) setting.
- `leading`: float or Number, optional
  - A text-leading size.
- `align`: SvgTextAlign, default SvgTextAlign.LEFT
  - A text-align setting.
- `bold`: Union[bool, Boolean], optional
  - A boolean, whether this text is a bold style or not.
- `italic`: Union[bool, Boolean], optional
  - A boolean, whether a text is an italic style or not (normal).
- `parent`: ChildMixIn or None, optional
  - A parent instance to add this instance. If the specified value is None, this interface uses a stage instance.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Notes]**

 ・SvgText's y-coordinate zero-position starts at the bottom of a text. So if you set y=0, a text becomes almost invisible.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     background_color=ap.Color("#333"),
...     stage_width=200,
...     stage_height=50,
...     stage_elem_id="stage",
... )
>>> svg_text: ap.SvgText = ap.SvgText(
...     text="Hello, world!",
...     font_size=20,
...     fill_color=ap.Color("#0af"),
... )
>>> svg_text.text
String("Hello, world!")

>>> svg_text.font_size
Int(20)

>>> svg_text.fill_color
Color("#00aaff")
```

<hr>

**[References]**

- [SvgText class](https://simon-ritchie.github.io/apysc/en/svg_text.html)

### `__repr__` method docstring

Get a string representation of this instance (for the sake of debugging).<hr>

**[Returns]**

- `repr_str`: str
  - This interface returns a type name and variable name (e.g., `SvgText("<variable_name>")`).

### `_append_constructor_expression` method docstring

Append a constructor expression string.

### `_convert_text_spans_list_to_array` method docstring

Convert text spans' list to an array.<hr>

**[Parameters]**

- `text_spans`: Union[List[SvgTextSpan], Array[SvgTextSpan]]
  - Text spans.

<hr>

**[Returns]**

- `text_spans_`: Array[SvgTextSpan]
  - A converted array.

### `_initialize_with_base_value` method docstring

Initialize this class with a base value(s).<hr>

**[Returns]**

- `svg_text`: SvgText
  - An initialized svg text instance.

### `create_with_svg_text_spans` method docstring

Create an `SvgText` instance with specified text spans.<hr>

**[Parameters]**

- `text_spans`: Union[List[SvgTextSpan], Array[SvgTextSpan]]
  - Text spans.
- `font_size`: Union[int, Int], optional
  - A font-size setting for an overall text.
- `font_family`: Optional[Union[Array[String], List[str]]], optional
  - A font-family setting for an overall text. Each string in an array needs to be a font name (e.g., `Times New Roman`).
- `x`: Union[float, Number], optional
  - X-coordinate to start drawing.
- `y`: Union[float, Number], optional
  - Y-coordinate to start drawing (please see also the `Notes` section).
- `fill_color`: Color, optional
  - A fill-color setting for an overall text.
- `fill_alpha`: float or Number, optional
  - A fill-alpha setting for an overall text.
- `line_color`: str or String, optional
  - A line-color setting for an overall text.
- `line_alpha`: float or Number, optional
  - A line-alpha setting for an overall text.
- `line_thickness`: int or Int, optional
  - A line-thickness (line-width) setting for an overall text.
- `leading`: float or Number, optional
  - A text-leading size for an overall text.
- `align`: SvgTextAlign, optional
  - A text-align setting for an overall text.
- `bold`: Union[bool, Boolean], optional
  - A boolean, whether this text is a bold style or not.
- `italic`: Union[bool, Boolean], optional
  - A boolean, whether a text is an italic style or not (normal).
- `parent`: Optional[ChildMixIn], optional
  - A parent instance to add this instance. If the specified value is None, this interface uses a stage instance.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `svg_text`: SvgText
  - A created `SvgText` instance.

<hr>

**[Notes]**

 ・SvgText's y-coordinate zero-position starts at the bottom of a text. So if you set y=0, a text becomes almost invisible.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     background_color=ap.Color("#333"),
...     stage_width=200,
...     stage_height=50,
... )
>>> svg_text: ap.SvgText = ap.SvgText.create_with_svg_text_spans(
...     text_spans=[
...         ap.SvgTextSpan(text="Hello, "),
...         ap.SvgTextSpan(text="Hello, ", font_size=14),
...     ],
...     font_size=20,
...     fill_color=ap.Color("#0af"),
... )
```

<hr>

**[References]**

- [SvgText class](https://simon-ritchie.github.io/apysc/en/svg_text.html)
- [SvgTextSpan class](https://simon-ritchie.github.io/apysc/en/svg_text_span.html)