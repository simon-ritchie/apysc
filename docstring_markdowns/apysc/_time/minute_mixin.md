# `apysc._time.minute_mixin` docstrings

## Module summary

Class implementations for the minute-related mix-in.

## `MinuteMixIn` class docstring

### `_append_minute_getter_expression` method docstring

Append a minute's getter expression string.<hr>

**[Parameters]**

- `minute_val`: Int
  - A month value to use in an expression.

### `_append_minute_setter_expression` method docstring

Append a minute's setter expression string.<hr>

**[Parameters]**

- `minute_val`: Int
  - A minute value to use in an expression.

### `_get_init_minute_argument_expression` method docstring

Get an initial minute's argument expression string.<hr>

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

### `_set_init_minute_value` method docstring

Set an initial minute value.<hr>

**[Parameters]**

- `minute`: Union[int, Int]
  - A minute value to set.