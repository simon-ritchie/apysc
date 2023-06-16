# `apysc._display.triangle` docstrings

## Module summary

Implementations of Triangle class.

## `Triangle` class docstring

The triangle vector graphics class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> triangle: ap.Triangle = ap.Triangle(
...     x1=75,
...     y1=50,
...     x2=50,
...     y2=100,
...     x3=100,
...     y3=100,
...     fill_color="#0af",
...     line_color="#fff",
...     line_thickness=3,
... )
>>> triangle.x2
Number(50.0)

>>> triangle.y1 = ap.Number(30)
>>> triangle.y1
Number(30.0)
```

<hr>

**[References]**

- [Triangle class](https://simon-ritchie.github.io/apysc/en/triangle.html)

### `__init__` method docstring

Create a triangle vector graphics instance.<hr>

**[Parameters]**

- `x1`: Union[float, Number]
  - First vertex's x coordinate.
- `y1`: Union[float, Number]
  - First vertex's y coordinate.
- `x2`: Union[float, Number]
  - Second vertex's x coordinate.
- `y2`: Union[float, Number]
  - Second vertex's y coordinate.
- `x3`: Union[float, Number]
  - Third vertex's x coordinate.
- `y3`: Union[float, Number]
  - Third vertex's y coordinate.
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
>>> _ = ap.Stage()
>>> triangle: ap.Triangle = ap.Triangle(
...     x1=75,
...     y1=50,
...     x2=50,
...     y2=100,
...     x3=100,
...     y3=100,
...     fill_color="#0af",
...     line_color="#fff",
...     line_thickness=3,
... )
>>> triangle.x2
Number(50.0)

>>> triangle.y1 = ap.Number(30.0)
>>> triangle.y1
Number(30.0)
```

<hr>

**[References]**

- [Triangle class](https://simon-ritchie.github.io/apysc/en/triangle.html)

### `__repr__` method docstring

Get a string representation of this instance (for the sake of debugging).<hr>

**[Returns]**

- `repr_str`: str
  - Type name and variable name will be set (e.g., `Triangle("<variable_name>")`).

### `_create_with_graphics` method docstring

Create a triangle instance with the instance of specified graphics.<hr>

**[Parameters]**

- `graphics`: graphics.Graphics
  - Graphics instance to link this instance.
- `x1`: Union[float, Number]
  - First vertex's y coordinate.
- `y1`: Union[float, Number]
  - First vertex's y coordinate.
- `x2`: Union[float, Number]
  - Second vertex's x coordinate.
- `y2`: Union[float, Number]
  - Second vertex's y coordinate.
- `x3`: Union[float, Number]
  - Third vertex's x coordinate.
- `y3`: Union[float, Number]
  - Third vertex's y coordinate.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `triangle`: Triangle
  - A created triangle instance.

### `_initialize_for_loop_key_or_value` method docstring

Initialize this instance for a loop value.<hr>

**[Returns]**

- `triangle`: Triangle
  - An initialized triangle instance.

### `_set_points_with_each_coordinate` method docstring

Set the `_points`' attribute value with each coordinate.

### `_set_x_and_y_with_minimum_point` method docstring

Set an x and y properties coordinate with a minimum point.