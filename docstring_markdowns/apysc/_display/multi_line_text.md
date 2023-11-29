# `apysc._display.multi_line_text` docstrings

## Module summary

The class implementation for the `MultiLineText` class.

## `MultiLineText` class docstring

The class implementation for a multiline text element.<hr>

**[References]**

- [MultiLineText class](https://simon-ritchie.github.io/apysc/en/multi_line_text.html)
- [Text fill_color property](https://simon-ritchie.github.io/apysc/en/text_fill_color.html)
- [Text fill_alpha property](https://simon-ritchie.github.io/apysc/en/text_fill_alpha.html)
- [Text bold property](https://simon-ritchie.github.io/apysc/en/text_bold.html)
- [Text italic property](https://simon-ritchie.github.io/apysc/en/text_italic.html)
- [text_align property](https://simon-ritchie.github.io/apysc/en/text_align.html)
- [text_align_last property](https://simon-ritchie.github.io/apysc/en/text_align_last.html)

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
- `font_size`: Union[int, Int], default 16
  - Font size.
- `fill_color`: Color, default Colors.GRAY_666666
  - Text color.
- `fill_alpha`: Union[float, Number], default 1.0
  - Text alpha (opacity). The minimum value is 0.0 (transparent), and the maximum value is 1.0 (solid).
- `bold`: Union[bool, Boolean], default False
  - Whether to display the text in bold.
- `italic`: Union[bool, Boolean], default False
  - Whether to display the text in italic.
- `text_align`: CssTextAlign, default `CssTextAlign.LEFT`
  - Text align setting.
- `text_align_last`: CssTextAlignLast, default `CssTextAlignLast.AUTO`
  - Last line's text-align setting.
- `underline`: Union[bool, Boolean], default False
  - Whether to display the text's underline.
- `parent`: ChildMixIn or None, default None
  - A parent instance to add this instance. If the specified value is None, this interface uses a stage instance.
- `variable_name_suffix`: str, default ""
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     background_color=ap.Color("#333"),
...     stage_width=300,
...     stage_height=100,
...     stage_elem_id="stage",
... )
>>> multi_line_text: ap.MultiLineText = ap.MultiLineText(
...     text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
...     "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
...     "Ut enim ad minim veniam",
...     width=300,
...     font_size=16,
...     fill_color=ap.Color("#00aaff"),
...     x=20,
...     y=20,
... )
>>> multi_line_text.fill_color
Color("#00aaff")
```

<hr>

**[References]**

- [MultiLineText class](https://simon-ritchie.github.io/apysc/en/multi_line_text.html)
- [Text fill_color property](https://simon-ritchie.github.io/apysc/en/text_fill_color.html)
- [Text fill_alpha property](https://simon-ritchie.github.io/apysc/en/text_fill_alpha.html)
- [Text bold property](https://simon-ritchie.github.io/apysc/en/text_bold.html)
- [Text italic property](https://simon-ritchie.github.io/apysc/en/text_italic.html)
- [text_align property](https://simon-ritchie.github.io/apysc/en/text_align.html)
- [text_align_last property](https://simon-ritchie.github.io/apysc/en/text_align_last.html)

### `_initialize_with_base_value` method docstring

Initialize this class with a base value(s).<hr>

**[Returns]**

- `text`: MultiLineText
  - An initialized instance.