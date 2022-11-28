# `apysc._time.millisecond_mixin` docstrings

## Module summary

Class implementations for the millisecond-related mix-in.

## `MillisecondMixIn` class docstring

### `_append_millisecond_getter_expression` method docstring

Append a millisecond's getter expression string.<hr>

**[Parameters]**

- `millisecond_val`: Int
  - A millisecond value to use in an expression.

### `_append_millisecond_setter_expression` method docstring

Append a millisecond's setter expression string.<hr>

**[Parameters]**

- `millisecond_val`: Int
  - A millisecond value to use in an expression.

### `_get_init_millisecond_argument_expression` method docstring

Get an initial millisecond argument expression string.<hr>

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

### `_set_init_millisecond_value` method docstring

Set an initial millisecond value.<hr>

**[Parameters]**

- `millisecond`: Union[int, Int]
  - A millisecond value to set.