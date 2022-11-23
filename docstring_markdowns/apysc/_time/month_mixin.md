# `apysc._time.month_mixin` docstrings

## Module summary

Class implementations for the month-related mix-in.

## `MonthMixIn` class docstring

### `_get_init_month_argument_expression` method docstring

Get an initial month's argument expression string.<hr>

**[Returns]**

- `expression`: str
  - A created expression string.

### `_make_snapshot` method docstring

Make a value snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `_revert` method docstring

Revert a value if a snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `_set_init_month_value` method docstring

Set an initial month value.<hr>

**[Parameters]**

- `month`: Union[int, Int]
  - A month value to set.