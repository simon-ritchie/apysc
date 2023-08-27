# COLORLESS constant

This page explains the `COLORLESS` constant.

## What constant is this?

The `COLORLESS` constant is the no-color setting.

If you set this constant to each color-related argument or property, the `apysc` clears its color.

## Basic usage

The `COLORLESS` constant is a subclass of the `Color` class.

So, you can specify its constant to each color-related argument or property.

The `apysc` displays no color since the `fill_color` and `line_color` argument's values are the `COLORLESS` constant in the following example:

```py
# runnable
import apysc as ap

_ = ap.Stage(
    stage_width=150,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
_ = ap.Rectangle(
    x=50,
    y=50,
    width=50,
    height=50,
    fill_color=ap.COLORLESS,
    line_color=ap.COLORLESS,
    line_thickness=3,
)

ap.save_overall_html(dest_dir_path="./colorless_basic_usage/")
```

<iframe src="static/colorless_basic_usage/index.html" width="150" height="150"></iframe>