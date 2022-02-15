# `apysc._display.line_color_interface` docstrings

## Module summary

Class implementation for line color interface.

## `LineColorInterface` class docstring

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

### `_set_initial_line_color_if_not_blank` method docstring

Set initial line color value if a specified value is not a blank string.<hr>

**[Parameters]**

- `line_color`: str or String
  - Line color (hexadecimal string, e.g., '#00aaff').

### `_update_line_color_and_skip_appending_exp` method docstring

Update line color and skip appending expression.<hr>

**[Parameters]**

- `value`: String
  - Line color to set.