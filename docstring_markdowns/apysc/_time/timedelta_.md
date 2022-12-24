# `apysc._time.timedelta_` docstrings

## Module summary

Class implementations for time delta-related interfaces.

## `_get_variable_name_suffix_from_datetimes` function docstring

Get a variable name suffix from specified `DateTime`s instances.<hr>

**[Parameters]**

- `left_datetime`: DateTime
  - Left-side `DateTime` to compare.
- `right_datetime`: DateTime
  - Right-side `DateTime` to compare.

<hr>

**[Returns]**

- `variable_name_suffix`: str
  - A created variable name suffix string.

## `TimeDelta` class docstring

Class implementations for time delta-related interfaces. Subtraction between two `DateTime` instances returns this class's instance.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> datetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)
>>> datetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)
>>> timedelta_: ap.TimeDelta = datetime_1 - datetime_2
>>> timedelta_.days
Int(2)

>>> timedelta_.total_seconds()
Number(172800.0)
```

<hr>

**[References]**

- [TimeDelta class](https://simon-ritchie.github.io/apysc/en/timedelta.html)
- [TimeDelta class days interface](https://simon-ritchie.github.io/apysc/en/timedelta_days.html)
- [TimeDelta class total_seconds interface](https://simon-ritchie.github.io/apysc/en/timedelta_total_seconds.html)

### `__init__` method docstring

Class implementations for time delta-related interfaces.<hr>

**[Parameters]**

- `left_datetime`: DateTime
  - Left-side `DateTime` to compare.
- `right_datetime`: DateTime
  - Right-side `DateTime` to compare.
- `skip_init_substitution_expression_appending`: bool, default False
  - A boolean indicates whether to skip an initial substitution expression or not. The `DateTime` class uses this option internally.

### `_append_constructor_expression` method docstring

Append a constructor expression.

### `_create_initial_substitution_expression` method docstring

Create an initial value's substitution expression string.<hr>

**[Returns]**

- `expression`: str
  - Created expression string.