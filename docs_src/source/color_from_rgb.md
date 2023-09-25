# Color class from_rgb class method

This pace explains the `Color` class `from_rgb` class method.

## What class method is this?

The `from_rgb` class method creates a new color instance from red, green and blue integer (0 to 255, 8bit unsigned integer range).

## Basic usage

The `from_rgb` class method requires the `red`, `green`, and `blue` arguments (`int` or `ap.Int` type value).

Its class method returns a new color instance.

```py
# runnable

import apysc as ap

ap.Stage(
    stage_width=350,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)

black_color: ap.Color = ap.Color.from_rgb(red=0, green=0, blue=0)
black_rectangle: ap.Rectangle = ap.Rectangle(
    x=50,
    y=50,
    width=50,
    height=50,
    fill_color=black_color,
)

white_color: ap.Color = ap.Color.from_rgb(red=255, green=255, blue=255)
white_rectangle: ap.Rectangle = ap.Rectangle(
    x=150,
    y=50,
    width=50,
    height=50,
    fill_color=white_color,
)

cyan_color: ap.Color = ap.Color.from_rgb(red=0, green=128, blue=255)
cyan_rectangle: ap.Rectangle = ap.Rectangle(
    x=250,
    y=50,
    width=50,
    height=50,
    fill_color=cyan_color,
)

ap.save_overall_html(dest_dir_path="color_from_rgb_basic_usage/")
```

<iframe src="static/color_from_rgb_basic_usage/index.html" width="350" height="150"></iframe>

## from_rgb class method API

<!-- Docstring: apysc._color.from_rgb_mixin.FromRgbMixIn.from_rgb -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `from_rgb(*, red: Union[int, apysc._type.int.Int], green: Union[int, apysc._type.int.Int], blue: Union[int, apysc._type.int.Int], variable_name_suffix: str = '') -> 'Color'`<hr>

**[Interface summary]**

Create a color instance from RGB (red, green, and blue) values.<hr>

**[Parameters]**

- `red`: Union[int, Int]
  - A red color value (0 to 255).
- `green`: Union[int, Int]
  - A green color value (0 to 255).
- `blue`: Union[int, Int]
  - A blue color value (0 to 255).
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `color`: Color
  - A created color instance.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> color: ap.Color = ap.Color.from_rgb(red=0, green=255, blue=0)
>>> color
Color("#00FF00")
```

<hr>

**[References]**

- [Color class](https://simon-ritchie.github.io/apysc/en/color.html)