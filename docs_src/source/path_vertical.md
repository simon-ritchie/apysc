# PathVertical class

This page explains the `PathVertical` class.

## What class is this?

The `PathVertical` class is the class to set a new vertical line on a path.

It simplifies an implementation if you need to draw a vertical line and not change a horizontal coordinate.

Mainly, the `Path` class constructor or `draw_path` interfaces use this setting.

## Basic usage

The `PathVertical` class constructor requires only one argument, `y`.

The `Path` class constructor or `draw_path` interfaces' `path_data_list` argument requires its instance.

The following example sets the y=150 coordinates and draws the vertical line from the y=50 coordinate:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=100, stage_height=200, stage_elem_id="stage"
)
path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathVertical(y=150),
    ],
    line_color="#0af",
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_vertical_basic_usage/")
```

<iframe src="static/path_vertical_basic_usage/index.html" width="100" height="200"></iframe>

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
        ap.PathVertical(y=50, relative=True),
    ],
    line_color="#0af",
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_vertical_relative/")
```

<iframe src="static/path_vertical_relative/index.html" width="100" height="150"></iframe>

## PathVertical class constructor API

<!-- Docstring: apysc._geom.path_vertical.PathVertical.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, y: Union[int, apysc._type.int.Int], *, relative: Union[bool, apysc._type.boolean.Boolean] = False, variable_name_suffix: str = '') -> None`<hr>

**[Interface summary]**

Path data class for the SVG `vertical line' (V).<hr>

**[Parameters]**

- `y`: Int or int
  - Y-coordinate of the destination point.
- `relative`: bool or Boolean, default False
  - A boolean value indicates whether the path coordinates are relative or not (absolute).
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color="#fff", thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathVertical(y=100),
...     ]
... )
```

<hr>

**[References]**

- [Path class](https://simon-ritchie.github.io/apysc/en/path.html)
- [Graphics draw_path interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html)