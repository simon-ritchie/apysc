# TimeDelta class total_seconds interface

This page explains the `TimeDelta` class's `total_seconds` method interface.

## What interface is this?

The `total_seconds` method returns the number of total seconds between two `DateTime` instances.

## Basic usage

The `total_seconds` method returns the apysc's `Number` value.

If any `DateTime` instances have a `millisecond` value, this interface sets a fraction value.

```py
# runnable
import apysc as ap

datetime_1: ap.DateTime = ap.DateTime(2022, 12, 7, millisecond=100)
datetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)
timedelta_: ap.TimeDelta = datetime_1 - datetime_2
total_seconds: ap.Number = timedelta_.total_seconds()
assert total_seconds == 60 * 60 * 24 * 2 + 0.1
```

## total_seconds method API

<!-- Docstring: apysc._time.timedelta_.TimeDelta.total_seconds -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `total_seconds(self) -> apysc._type.number.Number`<hr>

**[Interface summary]**

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