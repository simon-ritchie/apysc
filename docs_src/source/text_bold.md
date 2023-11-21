# Text bold property

This page explains the text-related `bold` property.

## What property is this?

The `bold` property updates or gets the instance's bold setting.

## Basic usage

The getter and setter interfaces' type becomes an `ap.Boolean` value.

If you specify the `ap.Boolean(True)` (or `ap.True_`) value, a text instance becomes bold style.

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
multi_line_text.bold = ap.True_

ap.save_overall_html(dest_dir_path="./text_bold_basic_usage/")
```

<iframe src="static/text_bold_basic_usage/index.html" width="350" height="170"></iframe>

## bold property API

<!-- Docstring: apysc._display.text_bold_css_mixin.TextBoldCssMixIn.bold -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a bold (font-weight) value.<hr>

**[Returns]**

- `bold`: Boolean
  - A bold (font-weight) value.

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
>>> multi_line_text.bold = ap.True_
>>> multi_line_text.bold
Boolean(True)
```