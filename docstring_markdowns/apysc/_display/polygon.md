# `apysc._display.polygon` docstrings

## Module summary

Implementations of Polygon class.

## `Polygon` class docstring

The polygon vector graphics class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
...     points=[
...         ap.Point2D(x=50, y=50),
...         ap.Point2D(x=50, y=100),
...         ap.Point2D(x=100, y=75),
...     ])
>>> polygon.fill_color
String('#00aaff')
```

<hr>

**[References]**

- [Graphics draw_polygon interface document](https://simon-ritchie.github.io/apysc/graphics_draw_polygon.html)

### `__init__` method docstring

Create a polygon vector graphic. This is similar to Polyline class, but unlike that, end point and start point will be connected.<hr>

**[Parameters]**

- `parent`: Graphics
  - Graphics instance to link this graphic.
- `points`: Array of Point2D
  - List of polygon vertex points.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
...     points=[
...         ap.Point2D(x=50, y=50),
...         ap.Point2D(x=50, y=100),
...         ap.Point2D(x=100, y=75),
...     ])
>>> polygon.fill_color
String('#00aaff')
```

<hr>

**[References]**

- [Graphics draw_polygon interface document](https://simon-ritchie.github.io/apysc/graphics_draw_polygon.html)

### `__repr__` method docstring

Get a string representation of this instance (for the sake of debugging).<hr>

**[Returns]**

- `repr_str`: str
  - Type name and variable name will be set (e.g., `Polygon('<variable_name>')`).

### `_append_constructor_expression` method docstring

Append constructor expression.