# `apysc._time.total_seconds_mixin` docstrings

## Module summary

Class implementations for the total seconds-related mix-in.

## `TotalSecondsMixIn` class docstring

### `_append_total_seconds_expression` method docstring

Append a total seconds' expression string.<hr>

**[Parameters]**

- `total_seconds`: Number
  - Total seconds value.

### `_set_init_total_seconds_value_for_python` method docstring

Set an initial total seconds value for Python.<hr>

**[Parameters]**

- `left_datetime`: DateTime
  - A left-side `DateTime` instance to compare.
- `right_datetime`: DateTime
  - A right-side `DateTime` instance to compare.

### `total_seconds` method docstring

Get the total seconds in the duration.<hr>

**[Returns]**

- `total_seconds`: Number
  - Total seconds in the duration.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> datetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)
>>> datetime_2: ap.DateTime = ap.DateTime(2022, 12, 6)
>>> timedelta_: ap.TimeDelta = datetime_1 - datetime_2
>>> timedelta_.total_seconds()
Number(86400.0)
```

<hr>

**[References]**

- [TimeDelta class](https://simon-ritchie.github.io/apysc/en/timedelta.html)
- [TimeDelta class total_seconds interface](https://simon-ritchie.github.io/apysc/en/timedelta_total_seconds.html)