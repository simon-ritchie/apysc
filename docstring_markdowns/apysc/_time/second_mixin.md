# `apysc._time.second_mixin` docstrings

## Module summary

Class implementations for the second-related mix-in.

## `SecondMixIn` class docstring

### `_append_second_getter_expression` method docstring

Append a second's getter expression string.<hr>

**[Parameters]**

- `second_val`: Int
  - A second value to use in an expression.

### `_append_second_setter_expression` method docstring

Append a second's setter expression string.<hr>

**[Parameters]**

- `second_val`: Int
  - A second value to use in an expression.

### `_get_init_second_argument_expression` method docstring

Get an initial second argument expression string.<hr>

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

### `_set_init_second_value` method docstring

Set an initial second value.<hr>

**[Parameters]**

- `second`: Union[int, Int]
  - A second value to set.