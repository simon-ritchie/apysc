# Text fill_alpha property

This page explains the text-related `fill_alpha` property.

## What property is this?

The `fill_alpha` property interface updates or gets the instance's fill alpha (opacity).

## Basic usage

The getter or setter interface value becomes (or requires) the `Number` value (0.0 to 1.0).

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
multi_line_text.fill_alpha = ap.Number(0.5)
ap.assert_equal(multi_line_text.fill_alpha, 0.5)

ap.save_overall_html(dest_dir_path="./text_fill_alpha_basic_usage/")
```

<iframe src="static/text_fill_alpha_basic_usage/index.html" width="350" height="170"></iframe>

## fill_alpha property API

<!-- Docstring: apysc._display.opacity_css_mixin.OpacityCssMixIn.fill_alpha -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a fill-alpha (opacity) value.<hr>

**[Returns]**

- `alpha`: Number
  - A fill-alpha (opacity) value.