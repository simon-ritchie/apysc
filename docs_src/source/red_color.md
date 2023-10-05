# Color class red_color property

This page explains the `Color` class `red_color` property.

## What property is this?

The `red_color` property returns or sets a red color `ap.Int` value.

This value takes the range from 0 to 255.

## Basic usage

The following example shows how to use the `red_color` getter and setter interfaces:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)

color: ap.Color = ap.Color("#00aaff")
red_color: ap.Int = color.red_color
ap.assert_equal(red_color, 0)

color = ap.Color("#ff00aa")
red_color = color.red_color
ap.assert_equal(red_color, 255)

color.red_color = ap.Int(0)
red_color = color.red_color
ap.assert_equal(red_color, 0)

color.red_color = ap.Int(255)
red_color = color.red_color
ap.assert_equal(red_color, 255)

ap.save_overall_html(dest_dir_path="./red_color_basic_usage/")
```

<iframe src="static/red_color_basic_usage/index.html" width="0" height="0"></iframe>

## red_color property API

<!-- Docstring: apysc._color.red_color_mixin.RedColorMixIn.red_color -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a red color integer value (0 to 255).<hr>

**[Returns]**

- `red_color`: Int
  - Red color integer value (0 to 255).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> color: ap.Color = ap.Color("#00aaff")
>>> red_color: ap.Int = color.red_color
>>> red_color
Int(0)

>>> color = ap.Color("#ff00aa")
>>> red_color = color.red_color
>>> red_color
Int(255)

>>> color.red_color = ap.Int(0)
>>> red_color = color.red_color
>>> red_color
Int(0)
```