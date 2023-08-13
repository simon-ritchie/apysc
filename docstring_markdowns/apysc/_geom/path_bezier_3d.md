# `apysc._geom.path_bezier_3d` docstrings

## Module summary

This module is for the SVG's `3D bezier curve` (C) path data class implementation.

## `PathBezier3D` class docstring

Path data class for the SVG's `3D bezier curve` (C).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathBezier3D(
...             control_x1=0,
...             control_y1=0,
...             control_x2=50,
...             control_y2=0,
...             dest_x=50,
...             dest_y=50,
...         ),
...         ap.PathBezier3DContinual(
...             control_x=100, control_y=100, dest_x=100, dest_y=50
...         ),
...     ]
... )
```

<hr>

**[References]**

- [Path class](https://simon-ritchie.github.io/apysc/en/path.html)
- [Graphics draw_path interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html)
- [PathBezier3D class](https://simon-ritchie.github.io/apysc/en/path_bezier_3d.html)
- [PathBezier3DContinual class](https://simon-ritchie.github.io/apysc/en/path_bezier_3d_continual.html)

### `__eq__` method docstring

Equal comparison method.<hr>

**[Parameters]**

- `other`: Any
  - The other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### `__init__` method docstring

Path data class for the SVG's `3D bezier curve` (C).<hr>

**[Parameters]**

- `control_x1`: float or Number
  - X-coordinate of the bezier's first control point.
- `control_y1`: float or Number
  - Y-coordinate of the bezier's first control point.
- `control_x2`: float or Number
  - X-coordinate of the bezier's second control point.
- `control_y2`: float or Number
  - Y-coordinate of the bezier's second control point.
- `dest_x`: float or Number
  - X-coordinate of the destination point.
- `dest_y`: float or Number
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
>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathBezier3D(
...             control_x1=0,
...             control_y1=0,
...             control_x2=50,
...             control_y2=0,
...             dest_x=50,
...             dest_y=50,
...         ),
...         ap.PathBezier3DContinual(
...             control_x=100, control_y=100, dest_x=100, dest_y=50
...         ),
...     ]
... )
```

<hr>

**[References]**

- [Path class](https://simon-ritchie.github.io/apysc/en/path.html)
- [Graphics draw_path interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html)
- [PathBezier3D class](https://simon-ritchie.github.io/apysc/en/path_bezier_3d.html)
- [PathBezier3DContinual class](https://simon-ritchie.github.io/apysc/en/path_bezier_3d_continual.html)

### `__ne__` method docstring

Not equal comparison method.<hr>

**[Parameters]**

- `other`: Any
  - The other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### `_get_svg_str` method docstring

Get a path's SVG string created with the current setting.<hr>

**[Returns]**

- `svg_str`: str
  - An SVG path string was created with the current setting.

### `update_path_data` method docstring

Update the path's data settings.<hr>

**[Parameters]**

- `control_x1`: float or Number
  - X-coordinate of the bezier's first control point.
- `control_y1`: float or Number
  - Y-coordinate of the bezier's first control point.
- `control_x2`: float or Number
  - X-coordinate of the bezier's second control point.
- `control_y2`: float or Number
  - Y-coordinate of the bezier's second control point.
- `dest_x`: float or Number
  - X-coordinate of the destination point.
- `dest_y`: float or Number
  - Y-coordinate of the destination point.
- `relative`: bool or Boolean, default False
  - A boolean value indicates whether the path coordinates are relative or not (absolute).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> bezier_3d_continual = ap.PathBezier3D(
...     control_x1=0,
...     control_y1=0,
...     control_x2=50,
...     control_y2=0,
...     dest_x=50,
...     dest_y=50,
... )
>>> bezier_3d_continual.update_path_data(
...     control_x1=100,
...     control_y1=100,
...     control_x2=150,
...     control_y2=100,
...     dest_x=150,
...     dest_y=150,
... )
>>> bezier_3d_continual.control_x1
Number(100.0)

>>> bezier_3d_continual.control_y1
Number(100.0)

>>> bezier_3d_continual.control_x2
Number(150.0)

>>> bezier_3d_continual.control_y2
Number(100.0)

>>> bezier_3d_continual.dest_x
Number(150.0)

>>> bezier_3d_continual.dest_y
Number(150.0)
```