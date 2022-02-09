# apysc._display.line_dot_setting_interface docstrings

## Module summary

Class implementation for line dot setting interface.

## LineDotSetting class docstring

Dot setting class for a line.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=10)
>>> line: ap.Line = sprite.graphics.draw_line(
...     x_start=50, y_start=50, x_end=150, y_end=50)
>>> line.line_dot_setting = ap.LineDotSetting(dot_size=5)
>>> line.line_dot_setting.dot_size
Int(5)
```

<hr>

**[References]**

- [Graphics line_style interface document](https://simon-ritchie.github.io/apysc/graphics_line_style.html)

### _make_snapshot method docstring

Make values' snapthot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _revert method docstring

Revert values if snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _append_line_dot_setting_update_expression method docstring

Append line dot setting updating expression.

### _initialize_line_dot_setting_if_not_initialized method docstring

Initialize _line_dot_setting attribute if it is not initialized yet.

### _make_snapshot method docstring

Make value's snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _revert method docstring

Revert value if snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _update_line_dot_setting_and_skip_appending_exp method docstring

Update line dot setting and skip appending expression.<hr>

**[Parameters]**

- `value`: LineDotSetting or None
  - Line dot setting to set.