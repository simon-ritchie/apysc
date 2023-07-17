# DateTime class

This page explains the `DateTime` class.

## What class is this?

The `DateTime` class is a class to handle each date- and time-related interface.

## Basic usage

The constructor requires the `year`, `month`, and `day` arguments, as follows:

```py
# runnable
import apysc as ap

ap.Stage()
dt: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)
```

Also, it has the optional `hour`, `minute`, `second`, and `millisecond` arguments:

```py
# runnable
import apysc as ap

ap.Stage()
dt: ap.DateTime = ap.DateTime(
    year=2022, month=12, day=5, hour=10, minute=30, second=50, millisecond=500
)
```

Each value has a getter and setter interface.

For instance, the `month` value can get or set via the properties:

```py
# runnable
import apysc as ap

ap.Stage()
dt: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)
assert dt.month == 12
dt.month = ap.Int(10)
assert dt.month == 10
```

Notes: the `weekday_py` and `weekday_js` properties only have a getter interface.

For more information about the other properties, please see the followings:

- [DateTime class year property](datetime_year.md)
- [DateTime class month property](datetime_month.md)
- [DateTime class day property](datetime_day.md)
- [DateTime class hour property](datetime_hour.md)
- [DateTime class minute property](datetime_minute.md)
- [DateTime class second property](datetime_second.md)
- [DateTime class millisecond property](datetime_millisecond.md)
- [DateTime class weekday_js and weekday_py properties](datetime_weekday_js_and_weekday_py.md)

Also, the `DateTime` class has each method interface, such as the `now` class method.

For more information about the methods interfaces, please see the following:

- [DateTime class now interface](datetime_now.md)

## DateTime class constructor API

<!-- Docstring: apysc._time.datetime_.DateTime.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, year: Union[int, apysc._type.int.Int], month: Union[int, apysc._type.int.Int], day: Union[int, apysc._type.int.Int], *, hour: Union[int, apysc._type.int.Int] = 0, minute: Union[int, apysc._type.int.Int] = 0, second: Union[int, apysc._type.int.Int] = 0, millisecond: Union[int, apysc._type.int.Int] = 0, variable_name_suffix: str = '', skip_init_substitution_expression_appending: bool = False) -> None`<hr>

**[Interface summary]**

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
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.
- `skip_init_substitution_expression_appending`: bool, default False
  - A boolean indicates whether to skip an initial substitution expression or not. The `DateTime` class uses this option internally.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
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

- [DateTime class year property](https://simon-ritchie.github.io/apysc/en/datetime_year.html)
- [DateTime class month property](https://simon-ritchie.github.io/apysc/en/datetime_month.html)
- [DateTime class day property](https://simon-ritchie.github.io/apysc/en/datetime_day.html)
- [DateTime class hour property](https://simon-ritchie.github.io/apysc/en/datetime_hour.html)
- [DateTime class minute property](https://simon-ritchie.github.io/apysc/en/datetime_minute.html)
- [DateTime class second property](https://simon-ritchie.github.io/apysc/en/datetime_second.html)
- [DateTime class millisecond property](https://simon-ritchie.github.io/apysc/en/datetime_millisecond.html)
- [DateTime class weekday_js and weekday_py properties](https://simon-ritchie.github.io/apysc/en/datetime_weekday_js_and_weekday_py.html)
- [DateTime class now interface](https://simon-ritchie.github.io/apysc/en/datetime_now.html)