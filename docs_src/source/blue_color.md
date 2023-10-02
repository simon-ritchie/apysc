# Color class blue_color property

This page explains the `Color` class `blue_color` property.

## What property is this?

The `blue_color` property returns a blue clor `ap.Int` value.

This value takes the range from 0 to 255.

## Basic usage

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=0,
    stage_height=0,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)

color: ap.Color = ap.Color("#ffaa00")
blue_color: ap.Int = color.blue_color
ap.assert_equal(blue_color, 0)

color = ap.Color("#00aaff")
blue_color = color.blue_color
ap.assert_equal(blue_color, 255)

ap.save_overall_html(dest_dir_path="./blue_color_basic_usage/")
```

<iframe src="static/blue_color_basic_usage/index.html" width="0" height="0"></iframe>

## blue_color property API

<!-- Docstring: apysc._color.blue_color_mixin.BlueColorMixIn.blue_color -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a blue color integer value (0 to 255).<hr>

**[Returns]**

- `blue_color`: Int
  - Blue color integer value (0 to 255).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     background_color=ap.Color("#333"),
...     stage_elem_id="stage",
... )
>>> color: ap.Color = ap.Color("#aaff00")
>>> blue_color: ap.Int = color.blue_color
>>> blue_color
Int(0)

>>> color = ap.Color("#00aaff")
>>> blue_color = color.blue_color
>>> blue_color
Int(255)
```