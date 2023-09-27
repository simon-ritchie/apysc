# `apysc._geom.point2d` docstrings

## Module summary

2-dimensional geometry point class implementation.

## `Point2D` class docstring

2-dimensional geometry point class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> point_1: ap.Point2D = ap.Point2D(x=0, y=0)
>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
...     points=[
...         point_1,
...         ap.Point2D(x=0, y=50),
...         ap.Point2D(x=50, y=25),
...     ]
... )
>>> point_1.x
Number(0.0)

>>> point_1.y
Number(0.0)
```

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

2-dimensional geometry point.<hr>

**[Parameters]**

- `x`: Union[float, Number]
  - X-coordinate.
- `y`: Union[float, Number]
  - Y-coordinate.
- `variable_name_suffix`: str, default ""
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
...     points=[
...         ap.Point2D(x=0, y=0),
...         ap.Point2D(x=0, y=50),
...         ap.Point2D(x=50, y=25),
...     ]
... )
```

### `__ne__` method docstring

Not equal comparison method.<hr>

**[Parameters]**

- `other`: Any
  - The other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### `__repr__` method docstring

Get a string representation of this instance (for the sake of debugging).<hr>

**[Returns]**

- `repr_str`: str
  - Type name and coordinates values are set (e.g., `Point2D(Number(50.0), Number(100.0))`).

### `_append_constructor_expression` method docstring

Append constructor expression.

### `_append_x_getter_expression` method docstring

Append x property getter expression.<hr>

**[Parameters]**

- `x`: Number
  - Target x value.

### `_append_x_setter_expression` method docstring

Append x property setter expression.<hr>

**[Parameters]**

- `value`: Number
  - X-coordinate to set.

### `_append_y_getter_expression` method docstring

Append y property getter expression.<hr>

**[Parameters]**

- `y`: Number
  - Target y value.

### `_append_y_setter_expression` method docstring

Append y property setter expression.<hr>

**[Parameters]**

- `value`: Number
  - Y-coordinate to set.

### `_make_snapshot` method docstring

Make values' snapshots.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `_revert` method docstring

Revert values if snapshots exist.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.