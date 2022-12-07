# DateTime class year property

This page explains the `DateTime` class's `year` property interface.

## What interface is this?

The `year` property gets or sets a year value.

## Basic usage

A `DateTime` instance has its property interface.

Its getter interface returns a year's `Int` value.

```py
# runnable
import apysc as ap

datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)
year: ap.Int = datetime_.year
assert year == 2022
```

Also, its setter interface accepts a year's `Int` value.

A for-digits number is acceptable (e.g., 2023).

```py
# runnable
import apysc as ap

datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)
datetime_.year = ap.Int(2023)
assert datetime_.year == 2023
```

## year property API

<!-- Docstring: apysc._time.datetime_.DateTime.year -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a current year's value.<hr>

**[Returns]**

- `year`: Int
  - A current year value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)
>>> datetime_.year
Int(2022)

>>> datetime_.year = ap.Int(2023)
>>> datetime_.year
Int(2023)
```