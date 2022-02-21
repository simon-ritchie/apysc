# `apysc._geom.path_close` docstrings

## Module summary

This module is for the SVG's `close path` (Z) path data class implementation.

## `PathClose` class docstring

Path data class for the SVG's `close path` (Z).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=00),
...         ap.PathLineTo(x=50, y=0),
...         ap.PathLineTo(x=50, y=50),
...         ap.PathClose(),
...     ])
```

### `__init__` method docstring

Path data class for the SVG's `close path` (Z).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=00),
...         ap.PathLineTo(x=50, y=0),
...         ap.PathLineTo(x=50, y=50),
...         ap.PathClose(),
...     ])
```

### `_get_svg_str` method docstring

Get a path's SVG string created with the current setting.<hr>

**[Returns]**

- `svg_str`: str
  - An SVG path string was created with the current setting.