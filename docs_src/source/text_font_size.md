# Text font_size property

This page explains the text-related `font_size` property.

## What property is this?

The `font_size` property updates or gets the instance's font size (text size).

## Basic usage

The getter and setter interfaces' type becomes an `ap.Int` value.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=350,
    stage_height=400,
    stage_elem_id="stage",
)
font_size_16_text: ap.MultiLineText = ap.MultiLineText(
    text="Example of font-size = 16. Lorem ipsum dolor sit amet, "
    "consectetur adipiscing elit, sed do eiusmod tempor incididunt "
    "ut labore et dolore magna aliqua. Ut enim ad minim veniam.",
    width=300,
    fill_color=ap.Color("#00aaff"),
    x=25,
    y=25,
)
font_size_16_text.font_size = ap.Int(16)

font_size_32_text: ap.MultiLineText = ap.MultiLineText(
    text="Example of font-size = 32. Lorem ipsum dolor sit amet, consectetur.",
    width=300,
    fill_color=ap.Color("#00aaff"),
    x=25,
    y=190,
)
font_size_32_text.font_size = ap.Int(32)

ap.save_overall_html(dest_dir_path="./text_font_size_basic_usage/")
```

<iframe src="static/text_font_size_basic_usage/index.html" width="350" height="400"></iframe>

## font_size property API

<!-- Docstring: apysc._display.text_font_size_css_mixin.TextFontSizeCssMixIn.font_size -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a text's font size.<hr>

**[Returns]**

- `font_size`: Int
  - A text font size.