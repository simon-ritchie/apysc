# Text fill_color property

This page explains the text-related `fill_color` property.

## What property is this?

The `fill_color` property interface updates or gets the instance's fill color.

## Basic usage

The getter interface becomes a `Color` value, and the setter one also requires a `Color` value.

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
    x=25,
    y=25,
)
multi_line_text.fill_color = ap.Colors.CYAN_00AAFF
ap.assert_equal(multi_line_text.fill_color, ap.Colors.CYAN_00AAFF)
ap.save_overall_html(dest_dir_path="text_fill_color_basic_usage/")
```

<iframe src="static/text_fill_color_basic_usage/index.html" width="300" height="200"></iframe>

## fill_color property API

<!-- Docstring: apysc._display.text_fill_color_css_mixin.TextFillColorCssMixIn.fill_color -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a text's fill color.<hr>

**[Returns]**

- `color`: Color
  - A text color.