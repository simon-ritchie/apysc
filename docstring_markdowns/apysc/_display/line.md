# `apysc._display.line` docstrings

## Module summary

Implementations of the Line class.

## `Line` class docstring

The line vector graphics class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color="#fff", thickness=5)
>>> line: ap.Line = sprite.graphics.draw_line(
...     x_start=50, y_start=50, x_end=150, y_end=50
... )
>>> line.line_color
String('#ffffff')

>>> line.line_thickness
Int(5)
```

<hr>

**[References]**

- [Line class](https://simon-ritchie.github.io/apysc/en/line.html)
- [Graphics draw_line interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_line.html)
- [Graphics draw_dotted_line interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_dotted_line.html)
- [Graphics draw_dashed_line interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_dashed_line.html)
- [Graphics draw_round_dotted_line interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_round_dotted_line.html)
- [Graphics draw_dash_dotted_line interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_dash_dotted_line.html)

### `__init__` method docstring

Create a line vector graphic.<hr>

**[Parameters]**

- `start_point`: Points2D
  - Line start point.
- `end_point`: Points2D
  - Line end point.
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
  - A dash dot (1-dot chain) setting to set.
- `parent`: ChildMixIn or None, default None
  - A parent instance to add this instance. If a specified value is None, this interface uses a stage instance.
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> line: ap.Line = ap.Line(
...     start_point=ap.Point2D(x=50, y=50),
...     end_point=ap.Point2D(x=150, y=50),
...     line_color="#ffffff",
...     line_thickness=3,
... )
>>> line.line_color
String('#ffffff')

>>> line.line_thickness
Int(3)
```

<hr>

**[References]**

- [Line class](https://simon-ritchie.github.io/apysc/en/line.html)

### `__repr__` method docstring

Get a string representation of this instance (for the sake of debugging).<hr>

**[Returns]**

- `repr_str`: str
  - Type name and variable name will be set (e.g., `Line('<variable_name>')`).

### `_append_constructor_expression` method docstring

Append a constructor expression.

### `_create_with_graphics` method docstring

Create a line instance with the instance of specified graphics.<hr>

**[Parameters]**

- `graphics`: Graphics
  - Graphics instance to link this instance.
- `start_point`: Points2D
  - Line start point.
- `end_point`: Points2D
  - Line end point.
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `line`: Line
  - A created line instance.

### `_make_points_expression` method docstring

Make line start and end expression str.<hr>

**[Returns]**

- `expression`: str
  - Each point expression.

### `_set_initial_x_and_y_with_minimum_point` method docstring

Set initial x and y properties coordinate with a minimum point.