# `apysc._display.polyline` docstrings

## Module summary

Implementations of Polyline class.

## `Polyline` class docstring

The polyline vector graphics class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color="#fff", thickness=5)
>>> _ = sprite.graphics.move_to(x=50, y=50)
>>> polyline: ap.Polyline = sprite.graphics.line_to(x=150, y=50)
>>> polyline.line_color
String("#ffffff")

>>> polyline.line_thickness
Int(5)
```

<hr>

**[References]**

- [Polyline class](https://simon-ritchie.github.io/apysc/en/polyline.html)
- [Graphics move_to and line_to interfaces](https://simon-ritchie.github.io/apysc/en/graphics_move_to_and_line_to.html)

### `__init__` method docstring

Create a polyline vector graphic.<hr>

**[Parameters]**

- `points`: Array of Point2D or list of Point2D
  - List of line points.
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
>>> polyline: ap.Polyline = ap.Polyline(
...     points=[
...         ap.Point2D(x=50, y=50),
...         ap.Point2D(x=100, y=100),
...         ap.Point2D(x=150, y=50),
...     ],
...     line_color="#ffffff",
...     line_thickness=3,
... )
>>> polyline.line_color
String("#ffffff")

>>> polyline.line_thickness
Int(3)
```

<hr>

**[References]**

- [Polyline class](https://simon-ritchie.github.io/apysc/en/polyline.html)

### `__repr__` method docstring

Get a string representation of this instance (for the sake of debugging).<hr>

**[Returns]**

- `repr_str`: str
  - Type name and variable name will be set (e.g., `Polyline("<variable_name>")`).

### `_append_constructor_expression` method docstring

Append constructor expression.

### `_create_with_graphics` method docstring

Create a polyline instance with the instance of specified graphics.<hr>

**[Parameters]**

- `graphics`: Graphics
  - Graphics instance to link this instance.
- `points`: Array of Point2D or list of Point2D
  - List of line points.
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `polyline`: Polyline
  - A created polyline instance.

### `_initialize_for_loop_key_or_value` method docstring

Initialize this instance for a loop key or value.<hr>

**[Returns]**

- `polyline`: Polyline
  - An initialized polyline instance

### `_set_x_and_y_with_minimum_point` method docstring

Set an x and y properties coordinate with a minimum point.