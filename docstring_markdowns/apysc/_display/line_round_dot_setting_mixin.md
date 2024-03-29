# `apysc._display.line_round_dot_setting_mixin` docstrings

## Module summary

Class implementation for the line round-dot setting interface.

## `LineRoundDotSettingMixIn` class docstring

### `_append_line_round_dot_setting_update_expression` method docstring

Append line round dot setting updating expression.

### `_initialize_line_round_dot_setting_if_not_initialized` method docstring

Initialize _line_round_dot_setting if this interface does not initialize it yet.

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
  - Line round-dot settings to set.

### `delete_line_round_dot_setting` method docstring

Delete a current line-round dot setting.<hr>

**[References]**

- [GraphicsBase line_round_dot interface](https://simon-ritchie.github.io/apysc/en/graphics_base_line_round_dot_setting.html)