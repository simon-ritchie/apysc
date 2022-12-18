# `apysc._time.month_end_mixin` docstrings

## Module summary

Class implementations for the month-end related mix-in.

## `MonthEndMixin` class docstring

### `set_month_end` method docstring

Set a month-end day.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)
>>> datetime_.set_month_end()
>>> datetime_.day
Int(31)
```

<hr>

**[References]**

- [DateTime class set_month_end interface](https://simon-ritchie.github.io/apysc/en/datetime_set_month_end.html)