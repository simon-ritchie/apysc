# `apysc._time.now_mixin` docstrings

## Module summary

Class implementations for now-related mix-in.

## `_append_now_expression` function docstring

Append a `now` interface expression string.<hr>

**[Parameters]**

- `dt`: DateTime
  - A target `DateTime` instance.

## `NowMixIn` class docstring

### `now` method docstring

Get a `DateTime` instance of the current time.<hr>

**[Parameters]**

- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `dt`: DateTime
  - A created `DateTime` instance.

<hr>

**[Examples]**

```py
>>> from datetime import datetime
>>> import apysc as ap
>>> _ = ap.Stage()
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