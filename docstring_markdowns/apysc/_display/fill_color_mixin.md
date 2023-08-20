# `apysc._display.fill_color_mixin` docstrings

## Module summary

Class implementation for fill color mix-in.

## `FillColorMixIn` class docstring

### `_append_fill_color_update_expression` method docstring

Append the fill color updating expression.

### `_initialize_fill_color_if_not_initialized` method docstring

Initialize the fill_color attribute if this interface does not initialize it yet.

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

### `_set_initial_fill_color_if_not_colorless` method docstring

Set the initial fill color if a specified value is not the `COLORLESS` constant.<hr>

**[Parameters]**

- `fill_color`: Color
  - A fill color.

### `_update_fill_color_and_skip_appending_exp` method docstring

Update fill color and skip appending expression.<hr>

**[Parameters]**

- `value`: Color
  - Fill color to set.