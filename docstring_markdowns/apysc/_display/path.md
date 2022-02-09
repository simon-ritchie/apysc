# apysc._display.path docstrings

## Module summary

Implementations of the Path class.

## Path class docstring

The path vector graphics class.

The path vector graphics class.<hr>

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
...     ])
```

### __init__ method docstring

Create a path vector graphics.<hr>

**[Parameters]**

- `parent`: Graphics
  - Graphics instance to link this graphic.
- `path_data_list`: list of PathDataBase
  - Target path data settings, such as the ap.PathData.MoveTo.

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
...     ])
```

### __repr__ method docstring

Get a string representation of this instance (for the sake of debugging).<hr>

**[Returns]**

- `repr_str`: str
  - Type name and variable name will be set (e.g., `Path('<variable_name>')`).

### _append_constructor_expression method docstring

Append a constructor expression.