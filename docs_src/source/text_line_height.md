# Text line_height property

This page explains the text-related `line_height` property.

## What property is this?

The `line_height` property updates or gets the instance's line height (leading) setting.

## Basic usage

The getter and setter interfaces' type becomes an `ap.Number` value.

If you specify a value of 1.5 to this property, the line height becomes 1.5 times the font size.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=300,
    stage_height=250,
    stage_elem_id="stage",
)

multi_line_text: ap.MultiLineText = ap.MultiLineText(
    text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
    "Ut enim ad minim veniam",
    width=250,
    fill_color=ap.Colors.GRAY_AAAAAA,
    x=25,
    y=25,
)
multi_line_text.line_height = ap.Number(2.0)

ap.save_overall_html(dest_dir_path="./text_line_height_basic_usage/")
```

<iframe src="static/text_line_height_basic_usage/index.html" width="300" height="250"></iframe>

## line_height property API

<!-- Docstring: apysc._display.text_line_height_css_mixin.TextLineHeightCssMixIn.line_height -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a line-height value.<hr>

**[Returns]**

- `line_height`: Number
  - A line-height value.