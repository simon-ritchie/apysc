# Text italic property

This page explains the text-related `italic` property.

## What property is this?

The `italic` property updates or gets the instance's italic style setting.

## Basic usage

The getter and setter interfaces accept an `ap.Boolean` value.

If you specify the `ap.Boolean(True)` (or `ap.True_`) value, a text instance becomes italic style.

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
multi_line_text.italic = ap.True_

ap.save_overall_html(dest_dir_path="./text_italic_basic_usage/")
```

<iframe src="static/text_italic_basic_usage/index.html" width="350" height="170"></iframe>

## italic property API

<!-- Docstring: apysc._display.text_italic_css_mixin.TextItalicCssMixIn.italic -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get an italic (font-style) value.<hr>

**[Returns]**

- `italic`: Boolean
  - An italic (font-style) value.

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
>>> multi_line_text.italic = ap.True_
>>> multi_line_text.italic
Boolean(True)
```