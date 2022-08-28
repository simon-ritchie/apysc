# Path class

This page explains the `Path` class.

## What class is this?

The `Path` class creates a path vector graphics object.

## Basic usage

The `Path` class constructor requires the `path_data_list` argument.

The constructor also accepts each style's argument, such as the `fill_color` and `line_color`.

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
    line_color="0af",
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_basic_usage/")
```

<iframe src="static/path_basic_usage/index.html" width="200" height="100"></iframe>