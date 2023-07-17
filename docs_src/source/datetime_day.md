# DateTime class day property

This page explains the `DateTime` class's `day` property interface.

## What interface is this?

The `day` property gets or sets a day value.

## Basic usage

A `DateTime` instance has its property interface.

Its getter interface returns a day's `Int` value.

```py
# runnable
import apysc as ap

ap.Stage()
datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)
day: ap.Int = datetime_.day
assert day == 5
```

Also, its setter interface accepts a day's `Int` value.

1-31 integer is acceptable.

```py
# runnable
import apysc as ap

ap.Stage()
datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)
datetime_.day = ap.Int(10)
assert datetime_.day == 10
```

## day property API

<!-- Docstring: apysc._time.datetime_.DateTime.day -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a current day's value.<hr>

**[Returns]**

- `day`: Int
  - A current-day value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)
>>> datetime_.day
Int(1)

>>> datetime_.day = ap.Int(2)
>>> datetime_.day
Int(2)
```