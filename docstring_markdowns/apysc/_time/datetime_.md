# `apysc._time.datetime_` docstrings

## Module summary

Class implementations for datetime-related interfaces.

## `DateTime` class docstring

The class for datetime-related interfaces.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> datetime_: ap.DateTime = ap.DateTime(
...     year=2022,
...     month=12,
...     day=5,
...     hour=10,
...     minute=30,
...     second=50,
...     millisecond=500,
... )
>>> datetime_.year
Int(2022)

>>> datetime_.month
Int(12)

>>> datetime_.day
Int(5)

>>> datetime_.hour
Int(10)

>>> datetime_.minute
Int(30)

>>> datetime_.millisecond
Int(500)

>>> datetime_.weekday_py
Int(0)

>>> datetime_.weekday_js
Int(1)
```

<hr>

**[References]**

- [DateTime class](https://simon-ritchie.github.io/apysc/en/datetime.html)
- [DateTime class year property](https://simon-ritchie.github.io/apysc/en/datetime_year.html)
- [DateTime class month property](https://simon-ritchie.github.io/apysc/en/datetime_month.html)
- [DateTime class day property](https://simon-ritchie.github.io/apysc/en/datetime_day.html)
- [DateTime class hour property](https://simon-ritchie.github.io/apysc/en/datetime_hour.html)
- [DateTime class minute property](https://simon-ritchie.github.io/apysc/en/datetime_minute.html)
- [DateTime class second property](https://simon-ritchie.github.io/apysc/en/datetime_second.html)
- [DateTime class millisecond property](https://simon-ritchie.github.io/apysc/en/datetime_millisecond.html)
- [DateTime class weekday_js and weekday_py properties](https://simon-ritchie.github.io/apysc/en/datetime_weekday_js_and_weekday_py.html)
- [DateTime class now interface](https://simon-ritchie.github.io/apysc/en/datetime_now.html)

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

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> datetime_: ap.DateTime = ap.DateTime(
...     year=2022,
...     month=12,
...     day=5,
...     hour=10,
...     minute=30,
...     second=50,
...     millisecond=500,
... )
>>> datetime_.year
Int(2022)

>>> datetime_.month
Int(12)

>>> datetime_.day
Int(5)

>>> datetime_.hour
Int(10)

>>> datetime_.minute
Int(30)

>>> datetime_.millisecond
Int(500)

>>> datetime_.weekday_py
Int(0)

>>> datetime_.weekday_js
Int(1)
```

<hr>

**[References]**

- [DateTime class](https://simon-ritchie.github.io/apysc/en/datetime.html)
- [DateTime class year property](https://simon-ritchie.github.io/apysc/en/datetime_year.html)
- [DateTime class month property](https://simon-ritchie.github.io/apysc/en/datetime_month.html)
- [DateTime class day property](https://simon-ritchie.github.io/apysc/en/datetime_day.html)
- [DateTime class hour property](https://simon-ritchie.github.io/apysc/en/datetime_hour.html)
- [DateTime class minute property](https://simon-ritchie.github.io/apysc/en/datetime_minute.html)
- [DateTime class second property](https://simon-ritchie.github.io/apysc/en/datetime_second.html)
- [DateTime class millisecond property](https://simon-ritchie.github.io/apysc/en/datetime_millisecond.html)
- [DateTime class weekday_js and weekday_py properties](https://simon-ritchie.github.io/apysc/en/datetime_weekday_js_and_weekday_py.html)
- [DateTime class now interface](https://simon-ritchie.github.io/apysc/en/datetime_now.html)

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

<hr>

**[Examples]**

```py
>>> from datetime import datetime
>>> import apysc as ap
>>> py_now: datetime = datetime.now()
>>> ap_now: ap.DateTime = ap.DateTime.now()
>>> ap_now.year == py_now.year
Boolean(True)

>>> ap_now.month == py_now.month
Boolean(True)

>>> ap_now.day == py_now.day
Boolean(True)
```

<hr>

**[References]**

- [DateTime class now interface](https://simon-ritchie.github.io/apysc/en/datetime_now.html)