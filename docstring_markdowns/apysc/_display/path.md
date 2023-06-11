# `apysc._display.path` docstrings

## Module summary

Implementations of the Path class.

## `Path` class docstring

The path vector graphics class.<hr>

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
...     ]
... )
```

<hr>

**[References]**

- [Path class](https://simon-ritchie.github.io/apysc/en/path.html)
- [Graphics draw_path interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html)
- [PathMoveTo class](https://simon-ritchie.github.io/apysc/en/path_move_to.html)
- [PathLineTo class](https://simon-ritchie.github.io/apysc/en/path_line_to.html)
- [PathHorizontal class](https://simon-ritchie.github.io/apysc/en/path_horizontal.html)
- [PathVertical class](https://simon-ritchie.github.io/apysc/en/path_vertical.html)
- [PathClose class](https://simon-ritchie.github.io/apysc/en/path_close.html)
- [PathBezier2D class](https://simon-ritchie.github.io/apysc/en/path_bezier_2d.html)
- [PathBezier2DContinual class](https://simon-ritchie.github.io/apysc/en/path_bezier_2d_continual.html)
- [PathBezier3D class](https://simon-ritchie.github.io/apysc/en/path_bezier_3d.html)
- [PathBezier3DContinual class](https://simon-ritchie.github.io/apysc/en/path_bezier_3d_continual.html)

### `__init__` method docstring

Create a path vector graphic.<hr>

**[Parameters]**

- `path_data_list`: list of PathDataBase
  - Target path data settings, such as the ap.PathData.MoveTo.
- `fill_color`: str or String, default ''
  - A fill-color to set.
- `fill_alpha`: float or Number, default 1.0
  - A fill-alpha to set.
- `line_color`: str or String, default ''
  - A line-color to set.
- `line_alpha`: float or Number, default 1.0
  - A line-alpha to set.
- `line_thickness`: int or Int, default 1
  - A line-thickness (line-width) to set.
- `line_cap`: String or LineCaps or None, default None
  - A line-cap setting to set.
- `line_joints`: String or LineJoints or None, default None
  - A line-joints setting to set.
- `line_dot_setting`: LineDotSetting or None, default None
  - A dot setting to set.
- `line_dash_setting`: LineDashSetting or None, default None
  - A dash setting to set.
- `line_round_dot_setting`: LineRoundDotSetting or None, default None
  - A round-dot setting to set.
- `line_dash_dot_setting`: LineDashDotSetting or None, default None
  - A dash-dot (1-dot chain) setting to set.
- `parent`: ChildMixIn or None, default None
  - A parent instance to add this instance. If a specified value is None, this interface uses a stage instance.
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> path: ap.Path = ap.Path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathBezier2D(control_x=50, control_y=0, dest_x=100, dest_y=50),
...     ],
...     line_color="#ffffff",
...     line_thickness=3,
... )
>>> path.line_color
String("#ffffff")

>>> path.line_thickness
Int(3)
```

<hr>

**[References]**

- [Path class](https://simon-ritchie.github.io/apysc/en/path.html)
- [Graphics draw_path interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html)
- [PathMoveTo class](https://simon-ritchie.github.io/apysc/en/path_move_to.html)
- [PathLineTo class](https://simon-ritchie.github.io/apysc/en/path_line_to.html)
- [PathHorizontal class](https://simon-ritchie.github.io/apysc/en/path_horizontal.html)
- [PathVertical class](https://simon-ritchie.github.io/apysc/en/path_vertical.html)
- [PathClose class](https://simon-ritchie.github.io/apysc/en/path_close.html)
- [PathBezier2D class](https://simon-ritchie.github.io/apysc/en/path_bezier_2d.html)
- [PathBezier2DContinual class](https://simon-ritchie.github.io/apysc/en/path_bezier_2d_continual.html)
- [PathBezier3D class](https://simon-ritchie.github.io/apysc/en/path_bezier_3d.html)
- [PathBezier3DContinual class](https://simon-ritchie.github.io/apysc/en/path_bezier_3d_continual.html)

### `__repr__` method docstring

Get a string representation of this instance (for the sake of debugging).<hr>

**[Returns]**

- `repr_str`: str
  - Type name and variable name will be set (e.g., `Path("<variable_name>")`).

### `_append_constructor_expression` method docstring

Append a constructor expression.

### `_create_with_graphics` method docstring

Create a path instance with the instance of specified graphics.<hr>

**[Parameters]**

- `graphics`: Graphics
  - Graphics instance to link this instance.
- `path_data_list`: list of PathDataBase
  - Target path data settings, such as the ap.PathData.MoveTo.
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `path`: Path
  - A created path instance.

### `_initialize_for_loop_value` method docstring

Initialize this instance for a loop value.<hr>

**[Returns]**

- `path`: Path
  - An initialized path instance.