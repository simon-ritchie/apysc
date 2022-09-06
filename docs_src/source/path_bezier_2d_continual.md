# PathBezier2DContinual class

This page explains the `PathBezier2DContinual` class.

## What class is this?

The `PathBezier2DContinual` class is the class to set a continual 2D bezier curve on a path.

This setting draws a smooth curve by using a line-symmetric control point.

Mainly, the `Path` class constructor or `draw_path` interfaces use this setting.

## Basic usage

The `PathBezier2DContinual` class constructor requires the `x` and `y` arguments.

These coordinates are the destination points of the bezier curve.

The `PathBezier2DContinual` class has the restriction, and you can use this class only after the `PathBezier2D` or `PathBezier2DContinual`.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=400, stage_height=200, stage_elem_id="stage"
)

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=100),
        ap.PathBezier2D(
            control_x=100,
            control_y=25,
            dest_x=150,
            dest_y=100,
        ),
        ap.PathBezier2DContinual(
            x=250,
            y=100,
        ),
        ap.PathBezier2DContinual(
            x=350,
            y=100,
        ),
    ],
    line_color="#0af",
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_bezier_2d_continual_basic_usage/")
```

<iframe src="static/path_bezier_2d_continual_basic_usage/index.html" width="400" height="200"></iframe>

## Relative position setting

The constructor's `relative` optional argument changes its behavior.

For example, if you set True to its argument, coordinates become relative.

The default setting is False, and it becomes absolute.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=400, stage_height=200, stage_elem_id="stage"
)

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=100),
        ap.PathBezier2D(
            control_x=100,
            control_y=25,
            dest_x=150,
            dest_y=100,
        ),
        ap.PathBezier2DContinual(
            x=100,
            y=0,
            relative=True,
        ),
        ap.PathBezier2DContinual(
            x=100,
            y=0,
            relative=True,
        ),
    ],
    line_color="#0af",
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_bezier_2d_continual_relative/")
```

<iframe src="static/path_bezier_2d_continual_relative/index.html" width="400" height="200"></iframe>

## PathBezier2DContinual class constructor API

<!-- Docstring: apysc._geom.path_bezier_2d_continual.PathBezier2DContinual.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, x: Union[int, apysc._type.int.Int], y: Union[int, apysc._type.int.Int], *, relative: Union[bool, apysc._type.boolean.Boolean] = False, variable_name_suffix: str = '') -> None`<hr>

**[Interface summary]** Path data class for the SVG `continual 2D bezier curve` (T).<hr>

**[Parameters]**

- `x`: Int or int
  - X-coordinate of the destination point.
- `y`: Int or int
  - Y-coordinate of the destination point.
- `relative`: bool or Boolean, default False
  - A boolean value indicates whether the path coordinates are relative or not (absolute).
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript's debugging.

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
...         ap.PathBezier2D(control_x=50, control_y=0, dest_x=100, dest_y=50),
...         ap.PathBezier2DContinual(x=150, y=50),
...     ]
... )
```

<hr>

**[References]**

- [Path class](https://simon-ritchie.github.io/apysc/en/path.html)
- [Graphics draw_path interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html)
- [PathBezier2D class](https://simon-ritchie.github.io/apysc/en/path_bezier_2d.html)