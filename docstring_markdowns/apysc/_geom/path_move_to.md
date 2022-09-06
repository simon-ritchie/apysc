# `apysc._geom.path_move_to` docstrings

## Module summary

This module is for the SVG `move to` (M) path data class implementation.

## `PathMoveTo` class docstring

Path data class for the SVG `move to` (M).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color="#fff", thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathLineTo(x=50, y=50),
...     ]
... )
```

<hr>

**[References]**

- [Path class](https://simon-ritchie.github.io/apysc/en/path.html)
- [Graphics draw_path interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html)
- [PathMoveTo class](https://simon-ritchie.github.io/apysc/en/path_move_to.html)

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

Path data class for the SVG `move to` (M).<hr>

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
...         ap.PathLineTo(x=50, y=50),
...     ]
... )
```

<hr>

**[References]**

- [Path class](https://simon-ritchie.github.io/apysc/en/path.html)
- [Graphics draw_path interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html)
- [PathMoveTo class](https://simon-ritchie.github.io/apysc/en/path_move_to.html)

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

Update the path data settings.<hr>

**[Parameters]**

- `x`: Int or int
  - X-coordinate of the destination point.
- `y`: Int or int
  - Y-coordinate of the destination point.
- `relative`: bool or Boolean, default False
  - A boolean value indicates whether the path coordinates are relative or not (absolute).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> move_to: ap.PathMoveTo = ap.PathMoveTo(x=50, y=50)
>>> move_to.update_path_data(x=100, y=150)
>>> move_to.x
Int(100)

>>> move_to.y
Int(150)
```