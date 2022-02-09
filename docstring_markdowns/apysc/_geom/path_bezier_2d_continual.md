# apysc._geom.path_bezier_2d_continual docstrings

## Module summary

Path data class implementation for the svg's `continual 2D bezier curve` (T).

## PathBezier2DContinual class docstring

Path data class for the svg's `continual 2D bezier curve` (T).

Path data class for the svg's `continual 2D bezier curve` (T).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathBezier2D(
...             control_x=50, control_y=0,
...             dest_x=100, dest_y=50),
...         ap.PathBezier2DContinual(x=150, y=50),
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

Path data class for the svg's `continual 2D bezier curve` (T).<hr>

**[Parameters]**

- `x`: int or Int
  - X-coordinate of the destination point.
- `y`: int or Int
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
...         ap.PathBezier2D(
...             control_x=50, control_y=0,
...             dest_x=100, dest_y=50),
...         ap.PathBezier2DContinual(x=150, y=50),
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

- `x`: int or Int
  - X-coordinate of the destination point.
- `y`: int or Int
  - Y-coordinate of the destination point.
- `relative`: bool or Boolean, default False
  - The boolean value indicating whether the path coordinates are relative or not (absolute).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> bezier_2d_continual = ap.PathBezier2DContinual(x=100, y=50)
>>> bezier_2d_continual.update_path_data(x=150, y=100)
>>> bezier_2d_continual.x
Int(150)

>>> bezier_2d_continual.y
Int(100)
```