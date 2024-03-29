# True_ and False_ constants

This page explains the `ap.True_` and `ap.False_` constants.

## What constants are these?

The `ap.True_` is the constant that indicates `Boolean`'s `True` value (it is almost the same as `ap.Boolean(True)`).

Conversely, the `ap.False_` is the constant that indicates `Boolean`'s `False` value.

## Basic usage

The `True_` and `False_` constants behave like `ap.Boolean(True)` and `ap.Boolean(False)`.

A function or method that takes a `Boolean` argument can accept these constants.

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=100,
    stage_height=50,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
text: ap.SvgText = ap.SvgText(
    text="Hello!",
    x=10,
    y=31,
    fill_color=ap.Color("#aaa"),
    bold=ap.True_,
    italic=ap.False_,
)

ap.save_overall_html(dest_dir_path="true_and_false_basic_usage/")
```

<iframe src="static/true_and_false_basic_usage/index.html" width="100" height="50"></iframe>