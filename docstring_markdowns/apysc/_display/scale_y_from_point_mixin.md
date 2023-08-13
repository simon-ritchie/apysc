# `apysc._display.scale_y_from_point_mixin` docstrings

## Module summary

Class implementation for the scale_y_from_point mix-in.

## `ScaleYFromPointMixIn` class docstring

### `_append_scale_y_from_point_update_expression` method docstring

Append the scale-y from the specified y-coordinate updating expression.<hr>

**[Parameters]**

- `y`: Number
  - Y-coordinate.

### `_initialize_scale_y_from_point_if_not_initialized` method docstring

Initialize the `_scale_y_from_point` attribute if this instance does not initialize it yet.

### `_make_snapshot` method docstring

Make a value snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `_revert` method docstring

Revert a value if a snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `get_scale_y_from_point` method docstring

Get a scale-y value from the given y-coordinate.<hr>

**[Parameters]**

- `y`: Number
  - Y-coordinate.

<hr>

**[Returns]**

- `scale_y`: ap.Number
  - Scale-y value from the given y-coordinate.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> y: ap.Number = ap.Number(100)
>>> rectangle.set_scale_y_from_point(scale_y=ap.Number(1.5), y=y)
>>> rectangle.get_scale_y_from_point(y=y)
Number(1.5)
```

<hr>

**[References]**

- [GraphicsBase scale_from_point interfaces](https://simon-ritchie.github.io/apysc/en/graphics_base_scale_from_point.html)

### `set_scale_y_from_point` method docstring

Update a scale-y value from the given y-coordinate.<hr>

**[Parameters]**

- `scale_y`: Number
  - Scale-y value to set.
- `y`: Number
  - Y-coordinate.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> y: ap.Number = ap.Number(100)
>>> rectangle.set_scale_y_from_point(scale_y=ap.Number(1.5), y=y)
>>> rectangle.get_scale_y_from_point(y=y)
Number(1.5)
```

<hr>

**[References]**

- [GraphicsBase scale_from_point interfaces](https://simon-ritchie.github.io/apysc/en/graphics_base_scale_from_point.html)