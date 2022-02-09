# `apysc._display.line_round_dot_setting_interface` docstrings

## Module summary

Class implementation for line round dot setting interface.

## `LineRoundDotSetting` class docstring

Round dot setting class for a line.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=10)
>>> line: ap.Line = sprite.graphics.draw_line(
...     x_start=50, y_start=50, x_end=150, y_end=50)
>>> line.line_round_dot_setting = ap.LineRoundDotSetting(
...     round_size=10, space_size=5)
>>> line.line_round_dot_setting.round_size
Int(10)

>>> line.line_round_dot_setting.space_size
Int(5)
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

### `_append_line_round_dot_setting_update_expression` method docstring

Append line round dot setting updating expression.

### `_initialize_line_round_dot_setting_if_not_initialized` method docstring

Initialize _line_round_dot_setting if it is not initialized yet.

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

### `_update_line_round_dot_setting_and_skip_appending_exp` method docstring

Update line round setting and skip appending expression.<hr>

**[Parameters]**

- `value`: LineRoundSetting or None
  - Line round dot setting to set.