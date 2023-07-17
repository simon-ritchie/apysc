# DateTime class hour property

This page explains the `DateTime` class's `hour` property interface.

## What interface is this?

The `hour` property gets or sets an hour value.

## Basic usage

A `DateTime` instance has its property interface.

Its getter interface returns an hour's `Int` value.

```py
# runnable
import apysc as ap

ap.Stage()
datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5, hour=10)
hour: ap.Int = datetime_.hour
assert hour == 10
```

Also, its setter interface accepts an hour's `Int` value.

0-23 integer is acceptable.

```py
# runnable
import apysc as ap

ap.Stage()
datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5, hour=10)
datetime_.hour = ap.Int(15)
assert datetime_.hour == 15
```

## hour property API

<!-- Docstring: apysc._time.datetime_.DateTime.hour -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a current hour's value.<hr>

**[Returns]**

- `hour`: Int
  - A current hour value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1, hour=5)
>>> datetime_.hour
Int(5)

>>> datetime_.hour = ap.Int(10)
>>> datetime_.hour
Int(10)
```