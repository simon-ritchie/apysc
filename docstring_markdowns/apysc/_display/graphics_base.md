# `apysc._display.graphics_base` docstrings

## Module summary

Class implementation for graphic's base class.

## `GraphicsBase` class docstring

### `__init__` method docstring

Vector graphic base class.<hr>

**[Parameters]**

- `variable_name`: str
  - Variable name of this instance. This will be used to js expression.

### `__repr__` method docstring

Get a string representation of this instance (for the sake of debugging).

### `_add_to_parent` method docstring

Add this instance to a specified parent instance.<hr>

**[Parameters]**

- `parent`: Optional[ChildMixIn]
  - A parent instance. If a specified value is None, this interface uses a stage instance.

### `_set_initial_basic_values` method docstring

Set initial fundamental values (such as the fill color or line thickness).<hr>

**[Parameters]**

- `fill_color`: str or String
  - A fill-color value to set.
- `fill_alpha`: float or Number
  - A fill-alpha value to set.
- `line_color`: str or String
  - A line-color value to set.
- `line_thickness`: int or Int
  - A line-thickness value to set.
- `line_alpha`: float or Number
  - A line-alpha value to set.
- `line_cap`: String or LineCaps or None
  - A line-cap value to set.
- `line_joints`: String or LineJoints or None
  - A line-joints value to set.

### `_set_line_setting_if_not_none_value_exists` method docstring

If a line setting (dot, dash, or something else) with a value other than None exists, set that value to the attribute.<hr>

**[Parameters]**

- `line_dot_setting`: Optional[LineDotSetting]
  - A dot setting to set.
- `line_dash_setting`: Optional[LineDashSetting]
  - A dash setting to set.
- `line_round_dot_setting`: Optional[LineRoundDotSetting]
  - A round-dot setting to set.
- `line_dash_dot_setting`: Optional[LineDashDotSetting]
  - A dash-dot (1-dot chain) setting to set.