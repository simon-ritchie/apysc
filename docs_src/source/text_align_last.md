# text_align_last property

This page explains the text-related `text_align_last` property.

## What property is this?

The `text_align_last` property updates or gets the text last line's alignment setting.

## Basic usage

The getter and setter interfaces' type becomes an `ap.CssTextAlignLast` enum value.

The acceptable enum values are as follows:

- `CssTextAlignLast.AUTO` (default)
- `CssTextAlignLast.LEFT`
- `CssTextAlignLast.CENTER`
- `CssTextAlignLast.RIGHT`
- `CssTextAlignLast.JUSTIFY`

## Example of CssTextAlignLast.AUTO

Notes: This setting is a default setting.

The `CssTextAlignLast.AUTO` setting inherits the `text_align` setting.

For example, if the `text_align` setting is the `CssTextAlign.CENTER`, the `text_align_last` property also behaves as the center align.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=350,
    stage_height=170,
    stage_elem_id="stage",
)
multi_line_text: ap.MultiLineText = ap.MultiLineText(
    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
    "Ut enim ad minim veniam",
    width=300,
    font_size=16,
    fill_color=ap.Color("#00aaff"),
    x=25,
    y=25,
)
multi_line_text.text_align = ap.CssTextAlign.CENTER
multi_line_text.text_align_last = ap.CssTextAlignLast.AUTO

ap.save_overall_html(dest_dir_path="./css_text_align_last_auto/")
```

<iframe src="static/css_text_align_last_auto/index.html" width="350" height="170"></iframe>

## Example of CssTextAlignLast.LEFT

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=350,
    stage_height=170,
    stage_elem_id="stage",
)
multi_line_text: ap.MultiLineText = ap.MultiLineText(
    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
    "Ut enim ad minim veniam",
    width=300,
    font_size=16,
    fill_color=ap.Color("#00aaff"),
    x=25,
    y=25,
)
multi_line_text.text_align = ap.CssTextAlign.JUSTIFY
multi_line_text.text_align_last = ap.CssTextAlignLast.LEFT

ap.save_overall_html(dest_dir_path="./css_text_align_last_left/")
```

<iframe src="static/css_text_align_last_left/index.html" width="350" height="170"></iframe>

## Example of CssTextAlignLast.CENTER

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=350,
    stage_height=170,
    stage_elem_id="stage",
)
multi_line_text: ap.MultiLineText = ap.MultiLineText(
    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
    "Ut enim ad minim veniam",
    width=300,
    font_size=16,
    fill_color=ap.Color("#00aaff"),
    x=25,
    y=25,
)
multi_line_text.text_align = ap.CssTextAlign.JUSTIFY
multi_line_text.text_align_last = ap.CssTextAlignLast.CENTER

ap.save_overall_html(dest_dir_path="./css_text_align_last_center/")
```

<iframe src="static/css_text_align_last_center/index.html" width="350" height="170"></iframe>

## Example of CssTextAlignLast.RIGHT

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=350,
    stage_height=170,
    stage_elem_id="stage",
)
multi_line_text: ap.MultiLineText = ap.MultiLineText(
    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
    "Ut enim ad minim veniam",
    width=300,
    font_size=16,
    fill_color=ap.Color("#00aaff"),
    x=25,
    y=25,
)
multi_line_text.text_align = ap.CssTextAlign.JUSTIFY
multi_line_text.text_align_last = ap.CssTextAlignLast.RIGHT

ap.save_overall_html(dest_dir_path="./css_text_align_last_right/")
```

<iframe src="static/css_text_align_last_right/index.html" width="350" height="170"></iframe>

## Example of CssTextAlignLast.JUSTIFY

Notes: This enum setting justifies the last line text evenly.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=350,
    stage_height=170,
    stage_elem_id="stage",
)
multi_line_text: ap.MultiLineText = ap.MultiLineText(
    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
    "Ut enim ad minim veniam",
    width=300,
    font_size=16,
    fill_color=ap.Color("#00aaff"),
    x=25,
    y=25,
)
multi_line_text.text_align = ap.CssTextAlign.JUSTIFY
multi_line_text.text_align_last = ap.CssTextAlignLast.JUSTIFY

ap.save_overall_html(dest_dir_path="./css_text_align_last_justify/")
```

<iframe src="static/css_text_align_last_justify/index.html" width="350" height="170"></iframe>

## text_align_last property API

<!-- Docstring: apysc._display.text_align_last_css_mixin.TextAlignLastCssMixIn.text_align_last -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a text-align-last value.<hr>

**[Returns]**

- `text_align_last`: CssTextAlignLast
  - A text-align-last value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     background_color=ap.Color("#333"),
...     stage_width=350,
...     stage_height=170,
...     stage_elem_id="stage",
... )
>>> multi_line_text: ap.MultiLineText = ap.MultiLineText(
...     text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
...     "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
...     "Ut enim ad minim veniam",
...     width=300,
...     font_size=16,
...     fill_color=ap.Color("#00aaff"),
...     x=25,
...     y=25,
... )
>>> multi_line_text.text_align = ap.CssTextAlign.JUSTIFY
>>> multi_line_text.text_align_last = ap.CssTextAlignLast.RIGHT
>>> assert multi_line_text.text_align_last == ap.CssTextAlignLast.RIGHT
```