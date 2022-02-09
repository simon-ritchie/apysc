# `apysc._display.points_2d_interface` docstrings

## Module summary

Class implementation for 2-dimensional points interface.

### `_append_points_update_expression` method docstring

Append points updating expression.<hr>

**[Parameters]**

- `value`: Array
  - Points value to set.

### `_initialize_points_if_not_initialized` method docstring

Initialize _points attribute if it hasn't been initialized yet.

### `_make_2dim_points_expression` method docstring

Make JavaScript expression string.<hr>

**[Returns]**

- `variable_name`: str
  - Created JavaScript points variable (2-dimensional array) name.
- `expression`: str
  - JavaScript expression string. This expression make 2-dimensional JavaScript array variable, like '[[x_1, y_1], [x_2, y_2], ...]'.

### `_make_snapshot` method docstring

Make values' snapshots.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `_revert` method docstring

Revert values if snapshots exist.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.