# `apysc._geom.path_bezier_2d_continual` docstrings

## Module summary

This module is for the SVG `continual 2D bezier curve` (T) class implementation.

## `PathBezier2DContinual` class docstring

Path data class for the SVG `continual 2D bezier curve` (T).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=3)
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
- [PathBezier2DContinual class](https://simon-ritchie.github.io/apysc/en/path_bezier_2d_continual.html)

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

Path data class for the SVG `continual 2D bezier curve` (T).<hr>

**[Parameters]**

- `x`: float or Number
  - X-coordinate of the destination point.
- `y`: float or Number
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
- [PathBezier2DContinual class](https://simon-ritchie.github.io/apysc/en/path_bezier_2d_continual.html)

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

Get an SVG path string created with the current setting.<hr>

**[Returns]**

- `svg_str`: str
  - An SVG path string was created with the current setting.

### `update_path_data` method docstring

Update a path data settings.<hr>

**[Parameters]**

- `x`: float or Number
  - X-coordinate of the destination point.
- `y`: float or Number
  - Y-coordinate of the destination point.
- `relative`: bool or Boolean, default False
  - A boolean value indicates whether the path coordinates are relative or not (absolute).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> bezier_2d_continual = ap.PathBezier2DContinual(x=100, y=50)
>>> bezier_2d_continual.update_path_data(x=150, y=100)
>>> bezier_2d_continual.x
Number(150.0)

>>> bezier_2d_continual.y
Number(100.0)
```