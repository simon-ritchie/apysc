# `apysc._time.datetime_` docstrings

## Module summary

Class implementations for datetime-related interfaces.

## `DateTime` class docstring

### `__init__` method docstring

The class for datetime-related interfaces.<hr>

**[Parameters]**

- `year`: Union[int, Int]
  - Four-digit year.
- `month`: Union[int, Int]
  - Two-digit month (1 to 12).
- `day`: Union[int, Int]
  - Two-digit day (1 to 31).
- `hour`: Optional[Union[int, Int]], optional
  - Two-digit hour (0 to 23).
- `minute`: Optional[Union[int, Int]], optional
  - Two-digit minute (0 to 59).
- `second`: Optional[Union[int, Int]], optional
  - Two-digit second (0 to 59).
- `millisecond`: Optional[Union[int, Int]], optional
  - Millisecond (0 to 999).
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript's debugging.
- `skip_init_substitution_expression_appending`: bool, default False
  - A boolean indicates whether to skip an initial substitution expression or not. The `DateTime` class uses this option internally.

### `_append_constructor_expression` method docstring

Append a constructor expression.

### `_append_now_expression` method docstring

Append a `now` interface expression string.<hr>

**[Parameters]**

- `dt`: DateTime
  - A target `DateTime` instance.

### `_create_initial_substitution_expression` method docstring

Create an initial value's substitution expression string.<hr>

**[Returns]**

- `expression`: str
  - Created expression string.

### `now` method docstring

Get a `DateTime` instance of the current time.<hr>

**[Returns]**

- `dt`: DateTime
  - A created `DateTime` instance.