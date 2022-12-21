# `apysc._time.timedelta_` docstrings

## Module summary

Class implementations for time delta-related interfaces.

## `_get_variable_name_suffix_from_datetimes` function docstring

Get a variable name suffix from specified `DateTime`s instances.<hr>

**[Parameters]**

- `left_datetime`: DateTime
  - Left-side datetime to compare.
- `right_datetime`: DateTime
  - Right-side datetime to compare.

<hr>

**[Returns]**

- `variable_name_suffix`: str
  - A created variable name suffix string.

## `TimeDelta` class docstring

Class implementations for timedelta-related interfaces.

### `__init__` method docstring

Class implementations for timedelta-related interfaces.<hr>

**[Parameters]**

- `left_datetime`: DateTime
  - Left-side datetime to compare.
- `right_datetime`: DateTime
  - Right-side datetime to compare.
- `skip_init_substitution_expression_appending`: bool, default False
  - A boolean indicates whether to skip an initial substitution expression or not. The `DateTime` class uses this option internally.

### `_append_constructor_expression` method docstring

Append a constructor expression.

### `_create_initial_substitution_expression` method docstring

Create an initial value's substitution expression string.<hr>

**[Returns]**

- `expression`: str
  - Created expression string.