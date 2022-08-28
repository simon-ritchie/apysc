# PathLineTo class

This page explains the `PathLineTo` class.

## What class is this?

The `PathLineTo` class is the class to set a new line from the current position on a path.

Mainly, the `Path` class constructor or `draw_path` interfaces use this setting.

## Basic usage

The `PathLineTo` class constructor requires the `x` and `y` arguments.

The `Path` class constructor or `draw_path` interfaces' `path_data_list` argument requires its instance.

The following example sets the line drawing from x=50 and y=50 to x=150 and y=50 with the `PathLineTo` instance:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=100, stage_elem_id="stage"
)
path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=150, y=50),
    ],
    line_color="#0af",
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_line_to_basic_usage/")
```

<iframe src="static/path_line_to_basic_usage/index.html" width="200" height="100"></iframe>

## Relative position setting

The constructor's `relative` optional argument changes its behavior.

For example, if you set True to its argument, coordinates become relative.

The default setting is False, and it becomes absolute.

The following example sets the relative setting and draws the line to the 50px under position from the current position:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=100, stage_height=150, stage_elem_id="stage"
)
path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=0, y=50, relative=True),
    ],
    line_color="#0af",
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_line_to_relative/")
```

<iframe src="static/path_line_to_relative/index.html" width="100" height="150"></iframe>