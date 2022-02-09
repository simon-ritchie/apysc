# apysc._geom.path_bezier_3d_continual docstrings

## Module summary

Path data class implementation for the svg's `continual 3D bezier curve` (S).

## PathBezier3DContinual class docstring

Path data class for the svg's `continual 3D bezier curve` (S).

Path data class for the svg's `continual 3D bezier curve` (S).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathBezier3D(
...             control_x1=0, control_y1=0,
...             control_x2=50, control_y2=0,
...             dest_x=50, dest_y=50),
...         ap.PathBezier3DContinual(
...             control_x=100, control_y=100,
...             dest_x=100, dest_y=50),
...     ])
```

### __eq__ method docstring

Equal comparison method.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### __init__ method docstring

Path data class for the svg's `continual 3D bezier curve` (S).<hr>

**[Parameters]**

- `control_x`: int or Int
  - X-coordinate of the bezier's control point.
- `control_y`: int or Int
  - Y-coordinate of the bezier's control point.
- `dest_x`: int or Int
  - X-coordinate of the destination point.
- `dest_y`: int or Int
  - Y-coordinate of the destination point.
- `relative`: bool or Boolean, default False
  - The boolean value indicating whether the path coordinates are relative or not (absolute).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathBezier3D(
...             control_x1=0, control_y1=0,
...             control_x2=50, control_y2=0,
...             dest_x=50, dest_y=50),
...         ap.PathBezier3DContinual(
...             control_x=100, control_y=100,
...             dest_x=100, dest_y=50),
...     ])
```

### __ne__ method docstring

Not equal comparison method.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### _get_svg_str method docstring

Get a path's SVG string created with the current setting.<hr>

**[Returns]**

- `svg_str`: str
  - A path's SVG string created with the current setting.

### update_path_data method docstring

Update the path's data settings.<hr>

**[Parameters]**

- `control_x`: int or Int
  - X-coordinate of the bezier's control point.
- `control_y`: int or Int
  - Y-coordinate of the bezier's control point.
- `dest_x`: int or Int
  - X-coordinate of the destination point.
- `dest_y`: int or Int
  - Y-coordinate of the destination point.
- `relative`: bool or Boolean, default False
  - The boolean value indicating whether the path coordinates are relative or not (absolute).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> bezier_3d_continual = ap.PathBezier3DContinual(
...     control_x=100, control_y=100,
...     dest_x=100, dest_y=50)
>>> bezier_3d_continual.update_path_data(
...     control_x=150, control_y=150,
...     dest_x=150, dest_y=100)
>>> bezier_3d_continual.control_x
Int(150)

>>> bezier_3d_continual.control_y
Int(150)

>>> bezier_3d_continual.dest_x
Int(150)

>>> bezier_3d_continual.dest_y
Int(100)
```