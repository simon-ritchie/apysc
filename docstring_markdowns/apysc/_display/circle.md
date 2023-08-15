# `apysc._display.circle` docstrings

## Module summary

Implementations of Circle class.

## `Circle` class docstring

The circle vector graphics class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> circle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=50)
>>> circle.x
Number(100.0)

>>> circle.y
Number(100.0)

>>> circle.radius
Int(50)

>>> circle.fill_color
Color("#00aaff")
```

<hr>

**[References]**

- [Circle class](https://simon-ritchie.github.io/apysc/en/circle.html)
- [Graphics draw_circle interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_circle.html)

### `__init__` method docstring

Create a circle vector graphic.<hr>

**[Parameters]**

- `x`: float or Number
  - X-coordinate of the circle center.
- `y`: float or Number
  - Y-coordinate of the circle center.
- `radius`: Int or int
  - Circle radius.
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
>>> circle: ap.Circle = ap.Circle(x=100, y=100, radius=50, fill_color=ap.Color("#00aaff"))
>>> circle.x
Number(100.0)

>>> circle.y
Number(100.0)

>>> circle.radius
Int(50)

>>> circle.fill_color
Color("#00aaff")

>>> circle = ap.Circle(
...     x=100,
...     y=100,
...     radius=50,
...     line_color=ap.Color("#ffffff"),
...     line_thickness=3,
...     line_dot_setting=ap.LineDotSetting(dot_size=10),
... )
>>> circle.line_color
Color("#ffffff")

>>> circle.line_thickness
Int(3)
```

<hr>

**[References]**

- [Circle class](https://simon-ritchie.github.io/apysc/en/circle.html)

### `__repr__` method docstring

Get a string representation of this instance (for the sake of debugging).<hr>

**[Returns]**

- `repr_str`: str
  - Type name and variable name will be set (e.g., `Circle("<variable_name>")`).

### `_append_constructor_expression` method docstring

Append a constructor expression.

### `_create_with_graphics` method docstring

Create a rectangle instance with the instance of specified graphics.<hr>

**[Parameters]**

- `graphics`: graphics.Graphics
  - Graphics instance to link this instance.
- `x`: float or Number
  - X-coordinate of the circle center.
- `y`: float or Number
  - Y-coordinate of the circle center.
- `radius`: Int or int
  - Circle radius.
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `circle`: Circle
  - A created circle instance.

### `_initialize_with_base_value` method docstring

Initialize this class with a base value(s).<hr>

**[Returns]**

- `circle`: Circle
  - An initialized circle instance.

### `_set_center_coordinates` method docstring

Set a center x-coordinate and a center y-coordinate.<hr>

**[Parameters]**

- `x`: float or Number
  - X-coordinate of the circle center.
- `y`: float or Number
  - Y-coordinate of the circle center.