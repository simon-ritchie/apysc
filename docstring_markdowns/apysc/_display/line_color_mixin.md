# `apysc._display.line_color_mixin` docstrings

## Module summary

Class implementation for line color interface.

## `LineColorMixIn` class docstring

### `_append_line_color_update_expression` method docstring

Append line color updating expression.

### `_initialize_line_color_if_not_initialized` method docstring

Initialize the line_color attribute if this interface does not initialize it yet.

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

### `_set_initial_line_color_if_not_colorless` method docstring

Set initial line color value if a specified value is not the `COLORLESS` constant.<hr>

**[Parameters]**

- `line_color`: Color
  - A line color.

### `_update_line_color_and_skip_appending_exp` method docstring

Update line color and skip appending expression.<hr>

**[Parameters]**

- `value`: Color
  - Line color to set.