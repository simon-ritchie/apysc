# `apysc._display.rotation_around_point_mixin` docstrings

## Module summary

Class implementation for the rotation_around_point mix-in.

## `RotationAroundPointMixIn` class docstring

### `_append_rotation_around_point_update_expression` method docstring

Append a rotation value around the given coordinates updating expression.<hr>

**[Parameters]**

- `rotation`: Int
  - Rotation value to set.
- `x`: Number
  - X-coordinate.
- `y`: Number
  - Y-coordinate.

### `_get_rotation_around_point_updating_expression` method docstring

Get a rotation value around the given coordinates' updating expression string.<hr>

**[Parameters]**

- `rotation`: Int
  - Rotation value to set.
- `x`: Number
  - X-coordinate.
- `y`: Number
  - Y-coordinate.

<hr>

**[Returns]**

- `expression`: str
  - A rotation value around the given coordinates' updating expression string.

### `_initialize_rotation_around_point_if_not_initialized` method docstring

Initialize the `_rotation_around_point` attribute if this interface does not initialize it yet.

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

### `get_rotation_around_point` method docstring

Get a rotation value around the given coordinates.<hr>

**[Parameters]**

- `x`: Number
  - X-coordinate.
- `y`: Number
  - Y-coordinate.

<hr>

**[Returns]**

- `rotation`: Int
  - Rotation value around the given coordinates.

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
>>> x: ap.Number = ap.Number(100)
>>> y: ap.Number = ap.Number(100)
>>> rectangle.set_rotation_around_point(rotation=ap.Int(45), x=x, y=y)
>>> rectangle.get_rotation_around_point(x=x, y=y)
Int(45)
```

<hr>

**[References]**

- [GraphicsBase rotate_around_point interfaces](https://simon-ritchie.github.io/apysc/en/graphics_base_rotation_around_point.html)

### `set_rotation_around_point` method docstring

Update a rotation value around the given coordinates.<hr>

**[Parameters]**

- `rotation`: Int
  - Rotation value to set.
- `x`: Number
  - X-coordinate.
- `y`: Number
  - Y-coordinate.

<hr>

**[References]**

- [GraphicsBase rotate_around_point interfaces](https://simon-ritchie.github.io/apysc/en/graphics_base_rotation_around_point.html)