# `apysc._display.ellipse` docstrings

## Module summary

Implementation of the Ellipse class.

## `Ellipse` class docstring

The ellipse vector graphics class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(
...     x=100, y=100, width=80, height=50
... )
>>> ellipse.x
Number(100.0)

>>> ellipse.y
Number(100.0)

>>> ellipse.width
Int(80)

>>> ellipse.height
Int(50)

>>> ellipse.fill_color
String("#00aaff")
```

<hr>

**[References]**

- [Ellipse class](https://simon-ritchie.github.io/apysc/en/ellipse.html)
- [Graphics draw_ellipse interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_ellipse.html)

### `__init__` method docstring

Create an ellipse vector graphic.<hr>

**[Parameters]**

- `x`: float or Number
  - X-coordinate of the ellipse center.
- `y`: float or Number
  - Y-coordinate of the ellipse center.
- `width`: Int or int
  - Ellipse width.
- `height`: Int or int
  - Ellipse height.
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
>>> ellipse: ap.Ellipse = ap.Ellipse(
...     x=100, y=100, width=100, height=50, fill_color="#00aaff"
... )
>>> ellipse.x
Number(100.0)

>>> ellipse.y
Number(100.0)

>>> ellipse.width
Int(100)

>>> ellipse.height
Int(50)

>>> ellipse.fill_color
String("#00aaff")
```

<hr>

**[References]**

- [Ellipse class](https://simon-ritchie.github.io/apysc/en/ellipse.html)

### `__repr__` method docstring

Get a string representation of this instance (for the sake of debugging).<hr>

**[Returns]**

- `repr_str`: str
  - Type name and variable name will be set (e.g., `Ellipse("<variable_name>")`).

### `_append_constructor_expression` method docstring

Append a constructor expression.

### `_create_with_graphics` method docstring

Create an ellipse instance with the instance of specified graphics.<hr>

**[Parameters]**

- `graphics`: Graphics
  - Graphics instance to link this instance.
- `x`: float or Number
  - X-coordinate of the ellipse center.
- `y`: float or Number
  - Y-coordinate of the ellipse center.
- `width`: Int or int
  - Ellipse width.
- `height`: Int or int
  - Ellipse height.
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `ellipse`: Ellipse
  - A created ellipse instance.