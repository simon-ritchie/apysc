# MultiLineText class

This page explains the `MultiLineText` class.

## What class is this?

The `MultiLineText` class creates a multi-line text instance.

This text instance wraps at a certain width.

## Basic usage

The `MultiLineText` class requires the `text` argument.

The constructor also accepts each style setting, such as the `width`, `fill_color`, `bold`, and `text_align`.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=300,
    stage_height=200,
    stage_elem_id="stage",
)

multi_line_text: ap.MultiLineText = ap.MultiLineText(
    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
    "Ut enim ad minim veniam",
    width=250,
    font_size=16,
    fill_color=ap.Colors.CYAN_00AAFF,
    x=25,
    y=25,
)
ap.save_overall_html(dest_dir_path="multi_line_text_basic_usage/")
```

<iframe src="static/multi_line_text_basic_usage/index.html" width="300" height="200"></iframe>

## MultiLineText constructor API

<!-- Docstring: apysc._display.multi_line_text.MultiLineText.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, *, text: Union[str, apysc._type.string.String], x: Union[float, apysc._type.number.Number] = 0, y: Union[float, apysc._type.number.Number] = 0, width: Union[int, apysc._type.int.Int] = 200, font_size: Union[int, apysc._type.int.Int] = 16, fill_color: apysc._color.color.Color = Color("#666666"), fill_alpha: Union[float, apysc._type.number.Number] = 1.0, bold: Union[bool, apysc._type.boolean.Boolean] = False, italic: Union[bool, apysc._type.boolean.Boolean] = False, text_align: apysc._display.css_text_align.CssTextAlign = <CssTextAlign.LEFT: 'left'>, text_align_last: apysc._display.css_text_align_last.CssTextAlignLast = <CssTextAlignLast.LEFT: 'left'>, underline: Union[bool, apysc._type.boolean.Boolean] = False, parent: Union[apysc._display.child_mixin.ChildMixIn, NoneType] = None, variable_name_suffix: str = '') -> None`<hr>

**[Interface summary]**

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
- `text_align_last`: CssTextAlignLast, default `CssTextAlignLast.LEFT`
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

- [Text fill_color property](https://simon-ritchie.github.io/apysc/en/text_fill_color.html)