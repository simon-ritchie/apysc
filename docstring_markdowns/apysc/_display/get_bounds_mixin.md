# `apysc._display.get_bounds_mixin` docstrings

## Module summary

The mix-in class implementation for the `get_bounds` method.

## `GetBoundsMixIn` class docstring

### `_append_get_bounds_expression` method docstring

Append a `get_counds` method expression string.<hr>

**[Parameters]**

- `left_x`: Number
  - The rectangle left x coordinate.
- `center_x`: Number
  - The rectangle center x coordinate.
- `right_x`: Number
  - The rectangle right x coordinate.
- `top_y`: Number
  - The rectangle top y coordinate.
- `center_y`: Number
  - The rectangle center y coordinate.
- `bottom_y`: Number
  - The rectangle bottom y coordinate.
- `width`: Int
  - The rectangle width.
- `height`: Int
  - The Rectangle height.

### `get_bounds` method docstring

Get an instance's bounding-box geometry data.<hr>

**[Returns]**

- `bounding_box`: RectangleGeom
  - An instance's bounding-box geometry data.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     background_color="#333", stage_width=250, stage_height=350
... )
>>> rectangle: ap.Rectangle = ap.Rectangle(
...     x=50,
...     y=100,
...     width=150,
...     height=200,
...     fill_color="#0af",
... )
>>> bounding_box: ap.RectangleGeom = rectangle.get_bounds()
```

<hr>

**[References]**

- [get_bounds interface](https://simon-ritchie.github.io/apysc/en/get_bounds.md)
- [RectangleGeom class](https://simon-ritchie.github.io/apysc/en/rectangle_geom.html)