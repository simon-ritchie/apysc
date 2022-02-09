# apysc._display.line_style_interface docstrings

## Module summary

Class implementation for line style related interface.

## LineStyleInterface class docstring



### _initialize_line_alpha_if_not_initialized method docstring

Initialize _line_alpha attribute if it is not initialized yet.

### _initialize_line_cap_if_not_initialized method docstring

Initialize _line_cap attribute if it hasn't been initialized yet.

### _initialize_line_color_if_not_initialized method docstring

Initialize _line_color attribute it it is not initialized yet.

### _initialize_line_dash_dot_setting_if_not_initialized method docstring

Initialize _line_dash_dot_setting attribute if it is not initialized yet.

### _initialize_line_dash_setting_if_not_initialized method docstring

Initialize _line_dash_setting attribute if it is not initialized yet.

### _initialize_line_dot_setting_if_not_initialized method docstring

Initialize _line_dot_setting attribute if it is not initialized yet.

### _initialize_line_joints_if_not_initialized method docstring

Initialize _line_joints attribute if it hasn't been initialized yet.

### _initialize_line_round_dot_setting_if_not_initialized method docstring

Initialize _line_round_dot_setting attribute if it is not initialized yet.

### _initialize_line_thickness_if_not_initialized method docstring

Initialize _line_thickness attribute if it is not initialized yet.

### _make_snapshot method docstring

Make values' snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _revert method docstring

Revert values if snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _set_line_cap method docstring

Set line cap setting to attribute.<hr>

**[Parameters]**

- `cap`: LineCaps or None, default None
  - Line cap (edge style) setting.

### _set_line_joints method docstring

Set line joints setting to attribute.<hr>

**[Parameters]**

- `joints`: LineJoints or None, default None
  - Line vertices (joints) style setting.

### line_style method docstring

Set line style values.<hr>

**[Parameters]**

- `color`: String or str
  - Hexadecimal color string. e.g., '#00aaff'
- `thickness`: Int or int, default 1
  - Line thickness (minimum value is 1).
- `alpha`: float or Number, default 1.0
  - Line color opacity (0.0 to 1.0).
- `cap`: LineCaps or None, default None
  - Line cap (edge style) setting. The not line-related graphics (e.g., Rectangle ignores this, conversely used by Polyline) ignore this setting.
- `joints`: LineJoints or None, default None
  - Line vertices (joints) style setting. The not polyline-related graphics (e.g., Rectangle ignores this, conversely used by Polyline) ignore this setting.
- `dot_setting`: LineDotSetting or None, default None
  - Dash setting. If this is specified, it makes a line dashed.
- `dash_setting`: LineDashSetting or None, default None
  - Dash setting. If this is specified, it makes a line dashed.
- `round_dot_setting`: LineRoundDotSetting or None, default None
  - Round dot setting. If this is specified, it makes a line round dotted. Notes: since this style uses a cap setting, it overrides cap and line thickness settings. And it increases the amount of line size. If you want to adjust to the same width of a normal line when using move_to and line_to interfaces, add half-round size to start x-coordinate and subtract from end e-coordinate. e.g., `this.move_to(x + round_size / 2, y)`, `this.line_to(x - round_size / 2, y)`
- `dash_dot_setting`: LineDashDotSetting or None, default None
  - Dash dot (1-dot chain) setting. If this is specified, it makes a line 1-dot chained.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(
...     color='#fff', thickness=5, alpha=0.5,
...     cap=ap.LineCaps.ROUND)
>>> line: ap.Line = sprite.graphics.draw_line(
...     x_start=50, y_start=50, x_end=150, y_end=50)
>>> line.line_color
String('#ffffff')

>>> line.line_thickness
Int(5)

>>> line.line_alpha
Number(0.5)

>>> line.line_cap
String('round')
```

<hr>

**[References]**

- [Graphics line_style interface document](https://simon-ritchie.github.io/apysc/graphics_line_style.html)