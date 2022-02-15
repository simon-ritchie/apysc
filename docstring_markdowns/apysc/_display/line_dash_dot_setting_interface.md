# `apysc._display.line_dash_dot_setting_interface` docstrings

## Module summary

Class implementation for line dash-dot setting interface.

## `LineDashDotSettingInterface` class docstring

### `_append_line_dash_dot_setting_update_expression` method docstring

Append line dash-dot setting updating expression.

### `_initialize_line_dash_dot_setting_if_not_initialized` method docstring

Initialize _line_dash_dot_setting attribute if this interface does not initialize it yet.

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

Update line dash-dot (1-dot chain) setting and skip appending expression.<hr>

**[Parameters]**

- `value`: LineDashDotSetting or None
  - Line dash dot (1-dot chain) setting to set.