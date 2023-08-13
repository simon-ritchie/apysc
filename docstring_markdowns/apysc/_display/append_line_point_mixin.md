# `apysc._display.append_line_point_mixin` docstrings

## Module summary

Class implementation for append line point mix-in.

## `AppendLinePointMixIn` class docstring

### `append_line_point` method docstring

Append line point at the end.<hr>

**[Parameters]**

- `x`: float, Number
  - X-coordinate.
- `y`: float, Number
  - Y-coordinate.

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
...         ap.Point2D(x=50, y=50),
...     ]
... )
>>> polygon.append_line_point(x=50, y=0)
```