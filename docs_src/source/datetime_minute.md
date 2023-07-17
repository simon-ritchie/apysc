# DateTime class minute property

This page explains the `DateTime` class's `minute` property interface.

## What interface is this?

The `minute` property gets or sets a minute value.

## Basic usage

A `DateTime` instance has its property interface.

Its getter interface returns a minute's `Int` value.

```py
# runnable
import apysc as ap

ap.Stage()
datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5, minute=30)
minute: ap.Int = datetime_.minute
assert minute == 30
```

Also, its setter interface accepts a minute's `Int` value.

0-59 integer is acceptable.

```py
# runnable
import apysc as ap

ap.Stage()
datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5, minute=30)
datetime_.minute = ap.Int(50)
assert datetime_.minute == 50
```

## minute property API

<!-- Docstring: apysc._time.datetime_.DateTime.minute -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a current minute's value.<hr>

**[Returns]**

- `minute`: Int
  - A current minute value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1, minute=30)
>>> datetime_.minute
Int(30)

>>> datetime_.minute = ap.Int(50)
>>> datetime_.minute
Int(50)
```