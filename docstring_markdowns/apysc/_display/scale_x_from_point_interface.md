# `apysc._display.scale_x_from_point_interface` docstrings

## Module summary

Class implementation for the scale_x_from_point interfaces.

## `ScaleXFromPointInterface` class docstring

### `_append_scale_x_from_point_update_expression` method docstring

Append the scale-x from the specified x-coordinate updating expression.<hr>

**[Parameters]**

- `x`: Int
  - X-coordinate.

### `_initialize_scale_x_from_point_if_not_initialized` method docstring

Initialize the `_scale_x_from_point` attribute if it hasn't been initialized yet.

### `_make_snapshot` method docstring

Make a value's snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `_revert` method docstring

Revert a value if snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `get_scale_x_from_point` method docstring

Get a scale-x value from the given x-coordinate.<hr>

**[Parameters]**

- `x`: Int
  - X-coordinate.

<hr>

**[Returns]**

- `scale_x`: Number
  - Scale-x value from the given x-coordinate.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> x: ap.Int = ap.Int(100)
>>> rectangle.set_scale_x_from_point(scale_x=ap.Number(1.5), x=x)
>>> rectangle.get_scale_x_from_point(x=x)
Number(1.5)
```

<hr>

**[References]**

- [GraphicsBase scale_from_point interfaces document](https://simon-ritchie.github.io/apysc/graphics_base_scale_from_point.html)

### `set_scale_x_from_point` method docstring

Update a scale-x value from the given x-coordinate.<hr>

**[Parameters]**

- `scale_x`: Number
  - Scale-x value to set.
- `x`: Int
  - X-coordinate.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> x: ap.Int = ap.Int(100)
>>> rectangle.set_scale_x_from_point(scale_x=ap.Number(1.5), x=x)
>>> rectangle.get_scale_x_from_point(x=x)
Number(1.5)
```

<hr>

**[References]**

- [GraphicsBase scale_from_point interfaces document](https://simon-ritchie.github.io/apysc/graphics_base_scale_from_point.html)