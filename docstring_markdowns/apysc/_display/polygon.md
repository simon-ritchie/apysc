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
>>> sprite.graphics.begin_fill(color="#0af")
>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
...     points=[
...         ap.Point2D(x=50, y=50),
...         ap.Point2D(x=50, y=100),
...         ap.Point2D(x=100, y=75),
...     ]
... )
>>> polygon.fill_color
String("#00aaff")
```

<hr>

**[References]**

- [Polygon class](https://simon-ritchie.github.io/apysc/en/polygon.html)
- [Graphics draw_polygon interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_polygon.html)

### `__init__` method docstring

Create a polygon vector graphic. This class is similar to the Polyline class, but unlike that, this class connects an end-point and start-point.<hr>

**[Parameters]**

- `points`: Array of Point2D or list of Point2D
  - List of polygon vertex points.
- `fill_color`: str or String, default ''
  - A fill-color to set.
- `fill_alpha`: float or Number, default 1.0
  - A fill-alpha to set.
- `line_color`: str or String, default ''
  - A line-color to set.
- `line_alpha`: float or Number, default 1.0
  - A line-alpha to set.
- `line_thickness`: int or Int, default 1
  - A line-thickness (line-width) to set.
- `line_cap`: String or LineCaps or None, default None
  - A line-cap setting to set.
- `line_joints`: String or LineJoints or None, default None
  - A line-joints setting to set.
- `line_dot_setting`: LineDotSetting or None, default None
  - A dot setting to set.
- `line_dash_setting`: LineDashSetting or None, default None
  - A dash setting to set.
- `line_round_dot_setting`: LineRoundDotSetting or None, default None
  - A round-dot setting to set.
- `line_dash_dot_setting`: LineDashDotSetting or None, default None
  - A dash-dot (1-dot chain) setting to set.
- `parent`: ChildMixIn or None, default None
  - A parent instance to add this instance. If a specified value is None, this interface uses a stage instance.
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> polygon: ap.Polygon = ap.Polygon(
...     points=[
...         ap.Point2D(x=50, y=50),
...         ap.Point2D(x=50, y=100),
...         ap.Point2D(x=100, y=75),
...     ],
...     fill_color="#00aaff",
... )
>>> polygon.fill_color
String("#00aaff")
```

<hr>

**[References]**

- [Polygon class](https://simon-ritchie.github.io/apysc/en/polygon.html)

### `__repr__` method docstring

Get a string representation of this instance (for the sake of debugging).<hr>

**[Returns]**

- `repr_str`: str
  - Type name and variable name will be set (e.g., `Polygon("<variable_name>")`).

### `_create_with_graphics` method docstring

Create a polygon instance with the instance of specified graphics.<hr>

**[Parameters]**

- `graphics`: Graphics
  - Graphics instance to link this instance.
- `points`: Array[Point2D]
  - List of polygon vertex points.
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `polygon`: Polygon
  - A created polygon instance.

### `_initialize_for_loop_key_or_value` method docstring

Initialize this instance for a loop value.<hr>

**[Returns]**

- `polygon`: Polygon
  - An initialized polygon instance.

### `_set_x_and_y_with_minimum_point` method docstring

Set an x and y properties coordinate with a minimum point.