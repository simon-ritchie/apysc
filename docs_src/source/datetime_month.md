# DateTime class month property

This page explains the `DateTime` class's `month` property interface.

## What interface is this?

The `month` property gets or sets a month's value.

## Basic usage

A `DateTime` instance has its property interface.

Its getter interface returns a month's `Int` value.

```py
# runnable
import apysc as ap

datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)
assert datetime_.month == 12
```

Also, its setter interface accepts a month's `Int` value.

```py
# runnable
import apysc as ap

datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)
datetime_.month = ap.Int(1)
assert datetime_.month == 1
```

## month property API

<!-- Docstring: apysc._time.datetime_.DateTime.month -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a current month's value.<hr>

**[Returns]**

- `month`: Int
  - A current month value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)
>>> datetime_.month
Int(12)

>>> datetime_.month = ap.Int(1)
>>> datetime_.month
Int(1)
```