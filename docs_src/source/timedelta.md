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

## days property API

<!-- Docstring: apysc._time.timedelta_.TimeDelta.days -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get days in the duration.<hr>

**[Returns]**

- `days`: Int
  - Days value. This interface ignores a fraction.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> datetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)
>>> datetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)
>>> timedelta_: ap.TimeDelta = datetime_1 - datetime_2
>>> timedelta_.days
Int(2)
```

<hr>

**[References]**

- [TimeDelta class days interface](https://simon-ritchie.github.io/apysc/en/timedelta_days.html)

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

<hr>

**[References]**

- [TimeDelta class total_seconds interface](https://simon-ritchie.github.io/apysc/en/timedelta_total_seconds.html)