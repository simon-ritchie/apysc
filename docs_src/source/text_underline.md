# Text underline property

This page explains the text-related `underline` property.

## What property is this?

The `underline` property sets or gets the text's underline style setting.

## Basic usage

The getter and setter interfaces' type becomes an `ap.Boolean` value.

If you specify the `ap.Boolean(True)` (or `ap.True_`) value, a text displays an underline.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=300,
    stage_height=195,
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
multi_line_text.underline = ap.True_

ap.save_overall_html(dest_dir_path="./text_underline_basic_usage/")
```

<iframe src="static/text_underline_basic_usage/index.html" width="300" height="195"></iframe>

## underline property API

<!-- Docstring: apysc._display.text_decoration_underline_css_mixin.TextDecorationUnderlineCssMixIn.underline -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a text underline (`text-decoration: underline`) setting.<hr>

**[Returns]**

- `underline`: Boolean
  - A text underline setting.