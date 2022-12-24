# TimeDelta class days interface

This page explains the `TimeDelta` class's `days` property interface.

## What interface is this?

The `days` property returns the number of days between two `DateTime` instances.

## Basic usage

The `days`' type is the apysc's `Int` and truncates a fraction value.

```py
# runnable
import apysc as ap

datetime_1: ap.DateTime = ap.DateTime(2022, 12, 7)
datetime_2: ap.DateTime = ap.DateTime(2022, 12, 5)
timedelta_: ap.TimeDelta = datetime_1 - datetime_2
days: ap.Int = timedelta_.days
assert days == 2

datetime_3: ap.DateTime = ap.DateTime(2022, 12, 7)
datetime_4: ap.DateTime = ap.DateTime(2022, 12, 5, hour=10)
timedelta_ = datetime_3 - datetime_4
days = timedelta_.days
assert days == 1
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

- [TimeDelta class](https://simon-ritchie.github.io/apysc/en/timedelta.html)