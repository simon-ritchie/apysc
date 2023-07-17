# DateTime class millisecond property

This page explains the `DateTime` class's `millisecond` property interface.

## What interface is this?

The `millisecond` property gets or sets a millisecond value.

## Basic usage

A `DateTime` instance has its property interface.

Its getter interface returns a millisecond's `Int` value.

```py
# runnable
import apysc as ap

ap.Stage()
datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5, millisecond=500)
millisecond: ap.Int = datetime_.millisecond
assert millisecond == 500
```

Also, its setter interface accepts a millisecond's `Int` value.

```py
# runnable
import apysc as ap

ap.Stage()
datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5, millisecond=500)
datetime_.millisecond = ap.Int(300)
assert datetime_.millisecond == 300
```

## millisecond property API

<!-- Docstring: apysc._time.datetime_.DateTime.millisecond -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a current millisecond value.<hr>

**[Returns]**

- `millisecond`: Int
  - A current millisecond value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> datetime_: ap.DateTime = ap.DateTime(
...     year=2022, month=12, day=1, millisecond=500
... )
>>> datetime_.millisecond
Int(500)

>>> datetime_.millisecond = ap.Int(300)
>>> datetime_.millisecond
Int(300)
```