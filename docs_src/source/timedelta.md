# TimeDelta class

This page explains the `TimeDelta` class.

## What class is this?

The `TimeDelta` class treats a time delta between two `DateTime` instances.

## Basic usage

Subtraction between two `DateTime` instances returns this class's instance.

```py
# runnable
import apysc as ap

datetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)
datetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)
timedelta_: ap.TimeDelta = datetime_1 - datetime_2
```

A `TimeDelta` instance has each interface, such as the `days`' property or `total_seconds`' method, as follows:

```
# runnable
import apysc as ap

datetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)
datetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)
timedelta_: ap.TimeDelta = datetime_1 - datetime_2
days: ap.Int = timedelta_.days
assert days == 2
total_seconds: ap.Number = timedelta_.total_seconds()
assert total_seconds == 60 * 60 * 24 * 2
```