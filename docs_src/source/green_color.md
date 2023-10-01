# Color class green_color property

This page explains the `Color` class `green_color` property.

## What property is this?

The `green_color` property returns a green color `ap.Int` value.

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

color: ap.Color = ap.Color("#aa00ff")
green_color: ap.Int = color.green_color
ap.assert_equal(green_color, 0)

color = ap.Color("#00ffaa")
green_color = color.green_color
ap.assert_equal(green_color, 255)

ap.save_overall_html(dest_dir_path="./green_color_basic_usage/")
```

<iframe src="static/green_color_basic_usage/index.html" width="0" height="0"></iframe>

## green_color property API

<!-- Docstring: apysc._color.green_color_mixin.GreenColorMixIn.green_color -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a green color integer value (0 to 255).<hr>

**[Returns]**

- `green_color`: Int
  - Green color integer value (0 to 255).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage(
...     background_color=ap.Color("#333"),
...     stage_elem_id="stage",
... )
>>> color: ap.Color = ap.Color("#aa00ff")
>>> green_color: ap.Int = color.green_color
>>> green_color
Int(0)

>>> color = ap.Color("#00ffaa")
>>> green_color = color.green_color
>>> green_color
Int(255)
```