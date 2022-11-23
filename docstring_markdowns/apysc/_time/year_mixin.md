# `apysc._time.year_mixin` docstrings

## Module summary

Class implementations for the year-related mix-in.

## `YearMixIn` class docstring

### `_append_year_getter_expression` method docstring

Append a year-getter's expression string.<hr>

**[Parameters]**

- `year_val`: Int
  - A year value to use in an expression.

### `_get_init_year_argument_expression` method docstring

Get an initial year's argument expression string.<hr>

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

### `_set_init_year_value` method docstring

Set an initial year value.<hr>

**[Parameters]**

- `year`: Union[int, Int]
  - A year value to set.