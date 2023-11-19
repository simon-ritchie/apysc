# text_align property

This page explains the text-related `text_align` property.

## What property is this?

The `text_align` property updates or gets the instance's text alignment setting.

## Basic usage

The getter and setter interfaces accept a `CssTextAlign` enum value.

The acceptable enum values are as follows:

- `CssTextAlign.LEFT`
- `CssTextAlign.CENTER`
- `CssTextAlign.RIGHT`
- `CssTextAlign.JUSTIFY`

## Example of CssTextAlign.LEFT

Notes: This setting is a default setting.

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
multi_line_text.text_align = ap.CssTextAlign.LEFT

ap.save_overall_html(dest_dir_path="./css_text_align_left/")
```

<iframe src="static/css_text_align_left/index.html" width="350" height="170"></iframe>

## Example of CssTextAlign.CENTER

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

ap.save_overall_html(dest_dir_path="./css_text_align_center/")
```

<iframe src="static/css_text_align_center/index.html" width="350" height="170"></iframe>

## Example of CssTextAlign.RIGHT

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
multi_line_text.text_align = ap.CssTextAlign.RIGHT

ap.save_overall_html(dest_dir_path="./css_text_align_right/")
```

<iframe src="static/css_text_align_right/index.html" width="350" height="170"></iframe>

## Example of CSSTextAlign.JUSTIFY

Notes: This enum setting justifies a text evenly.

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

ap.save_overall_html(dest_dir_path="./css_text_align_justify/")
```

## text_align property API

<!-- Docstring: apysc._display.text_align_css_mixin.TextAlignCssMixIn.text_align -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a text-align value.<hr>

**[Returns]**

- `text_align`: CssTextAlign
  - A text-align value.