# `apysc._display.line_dash_dot_setting_interface` docstrings

## Module summary

Class implementation for line dash dot setting interface.

## `LineDashDotSetting` class docstring

Dash dot (1-dot chain) setting for a line.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=10)
>>> line: ap.Line = sprite.graphics.draw_line(
...     x_start=50, y_start=50, x_end=150, y_end=50)
>>> line.line_dash_dot_setting = ap.LineDashDotSetting(
...     dot_size=2, dash_size=5, space_size=3)
>>> line.line_dash_dot_setting.dot_size
Int(2)

>>> line.line_dash_dot_setting.dash_size
Int(5)

>>> line.line_dash_dot_setting.space_size
Int(3)
```

<hr>

**[References]**

- [Graphics line_style interface document](https://simon-ritchie.github.io/apysc/graphics_line_style.html)

### `_make_snapshot` method docstring

Make values' snapthot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `_revert` method docstring

Revert values if snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

## `LineDashDotSettingInterface` class docstring

### `_append_line_dash_dot_setting_update_expression` method docstring

Append line dash dot setting updating expression.

### `_initialize_line_dash_dot_setting_if_not_initialized` method docstring

Initialize _line_dash_dot_setting attribute if it is not initialized yet.

### `_make_snapshot` method docstring

Make value's snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `_revert` method docstring

Revert value if snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `_update_line_dash_dot_setting_and_skip_appending_exp` method docstring

Update line dash dot (1-dot chain) setting and skip appending expression.<hr>

**[Parameters]**

- `value`: LineDashDotSetting or None
  - Line dash dot (1-dot chain) setting to set.