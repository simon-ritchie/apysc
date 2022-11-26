# `apysc._time.hour_mixin` docstrings

## Module summary

Class implementations for the hour-related mix-in.

## `HourMixIn` class docstring

### `_append_hour_getter_expression` method docstring

Append an hour's getter expression string.<hr>

**[Parameters]**

- `hour_val`: Int
  - An hour value to use in an expression.

### `_append_hour_setter_expression` method docstring

Append an hour's setter expression string.<hr>

**[Parameters]**

- `hour_val`: Int
  - An hour value to use in an expression.

### `_get_init_hour_argument_expression` method docstring

Get an initial hour's argument expression string.<hr>

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

### `_set_init_hour_value` method docstring

Set an initial hour value.<hr>

**[Parameters]**

- `hour`: Union[int, Int]
  - An hour value to set.