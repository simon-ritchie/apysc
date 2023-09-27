# Color class

This page explains the `Color` class.

## What class is this?

The `Color` class handles color settings.

Color settings, such as the `fill_color` or `line_color` arguments or properties, require its value.

## Basic usage

The constructor of the `Color` class requires a hexadecimal color code string, for example, `#00aaff`.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=250,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)

left_rectangle: ap.Rectangle = ap.Rectangle(
    x=50,
    y=50,
    width=50,
    height=50,
    fill_color=ap.Color("#00aaff"),
)

right_rectangle: ap.Rectangle = ap.Rectangle(
    x=150,
    y=50,
    width=50,
    height=50,
    line_color=ap.Color("#ffffff"),
    line_thickness=3,
)

ap.save_overall_html(dest_dir_path="./color_basic_usage/")
```

<iframe src="static/color_basic_usage/index.html" width="250" height="150"></iframe>

## Acceptable hexadecimal color codes

Color code is acceptable like the following list:

- Six characters, e.g., `#00aaff`.
- Three characters, e.g., `#0af` (this becomes `#00aaff`).
- A single character, e.g., `#5` (this becomes `#000005`).
- A skipped `#` symbol string, e.g., `0af` (this becomes `#00aaff`).
- The `COLORLESS` constant (this setting clears a color setting).

## Color constructor API

<!-- Docstring: apysc._color.color.Color.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, value: ~_StrOrString, *, variable_name_suffix: str = '') -> None`<hr>

**[Interface summary]**

The color class implementation.<hr>

**[Parameters]**

- `value`: str or String
  - A hexadecimal color code string (e.g., '#000000').
- `variable_name_suffix`: str, default ""
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.