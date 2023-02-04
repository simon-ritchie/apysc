# `apysc._display.rectangle` docstrings

## Module summary

Implementations of the Rectangle class.

## `Rectangle` class docstring

The rectangle vector graphics class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=100, height=75
... )
>>> rectangle.x
Int(50)

>>> rectangle.y
Int(50)

>>> rectangle.width
Int(100)

>>> rectangle.height
Int(75)

>>> rectangle.fill_color
String('#00aaff')
```

<hr>

**[References]**

- [Rectangle class](https://simon-ritchie.github.io/apysc/en/rectangle.html)
- [Graphics draw_rect interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_rect.html)

### `__init__` method docstring

Create a rectangle vector graphic.<hr>

**[Parameters]**

- `x`: Int or int
  - X-coordinate to start drawing.
- `y`: Int or int
  - Y-coordinate to start drawing.
- `width`: Int or int
  - Rectangle width.
- `height`: Int or int
  - Rectangle height.
- `ellipse_width`: int or Int
  - Ellipse width.
- `ellipse_height`: int or Int
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
>>> rectangle: ap.Rectangle = ap.Rectangle(
...     x=50, y=50, width=100, height=100, fill_color="#00aaff"
... )
>>> rectangle.x
Int(50)

>>> rectangle.y
Int(50)

>>> rectangle.width
Int(100)

>>> rectangle.height
Int(100)

>>> rectangle.fill_color
String('#00aaff')
```

<hr>

**[References]**

- [Rectangle class](https://simon-ritchie.github.io/apysc/en/rectangle.html)

### `__repr__` method docstring

Get a string representation of this instance (for the sake of debugging).<hr>

**[Returns]**

- `repr_str`: str
  - Type name and variable name will be set (e.g., `Rectangle('<variable_name>')`).

### `_append_constructor_expression` method docstring

Append constructor expression.

### `_create_with_graphics` method docstring

Create a rectangle instance with the instance of specified graphics..<hr>

**[Parameters]**

- `graphics`: Graphics
  - Graphics instance to link this instance.
- `x`: Int or int
  - X-coordinate to start drawing.
- `y`: Int or int
  - Y-coordinate to start drawing.
- `width`: Int or int
  - Rectangle width.
- `height`: Int or int
  - Rectangle height.
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `rectangle`: Rectangle
  - A created rectangle instance.

### `_set_ellipse_settings_if_values_are_not_zero` method docstring

Set ellipse-related settings if values are not zero.<hr>

**[Parameters]**

- `ellipse_width`: Union[int, Int]
  - Ellipse width to set.
- `ellipse_height`: Union[int, Int]
  - Ellipse height to set.