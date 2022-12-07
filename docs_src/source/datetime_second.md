# DateTime class second property

This page explains the `DateTime` class's `second` property interface.

## What interface is this?

The `second` property gets or sets a second value.

## Basic usage

A `DateTime` instance has its property interface.

Its getter interface returns a second's `Int` value.

```py
# runnable
import apysc as ap

datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5, second=30)
second: ap.Int = datetime_.second
assert second == 30
```

Also, its setter interface accepts a second's `Int` value.

0-59 integer is acceptable.

```py
# runnable
import apysc as ap

datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5, second=30)
datetime_.second = ap.Int(50)
assert datetime_.second == 50
```

## second property API

<!-- Docstring: apysc._time.datetime_.DateTime.second -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a current second's value.<hr>

**[Returns]**

- `second`: Int
  - A current second value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1, second=30)
>>> datetime_.second
Int(30)

>>> datetime_.second = ap.Int(50)
>>> datetime_.second
Int(50)
```