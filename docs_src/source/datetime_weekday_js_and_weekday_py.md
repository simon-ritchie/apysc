# DateTime class weekday_js and weekday_py properties

This page explains the `DateTime` class's `weekday_js` and `weekday_py` properties interfaces.

## What interface are these?

The `weekday_js` property gets a JavaScript weekday value (Sunday is 0, and Saturday is 6).

Similarly, the `weekday_py` property gets a Python weekday value (Monday is 0, and Sunday is 6).

These interfaces have only the getter interface (there is no setter interface).

## Basic usage

A `DateTime` instance has these properties interfaces.

These getter interfaces return a weekday's `Int` value.

```py
# runnable
import apysc as ap

ap.Stage()

# 2022-12-11 is Sunday.
datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=11)
weekday_js: ap.Int = datetime_.weekday_js
assert weekday_js == 0

weekday_py: ap.Int = datetime_.weekday_py
assert weekday_py == 6
```

## weekday_js property API

<!-- Docstring: apysc._time.datetime_.DateTime.weekday_js -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a current weekday value. This interface sets the weekday based on the JavaScript value as follows: <br> ・0 -> Sunday <br> ・1 -> Monday <br> ・2 -> Tuesday <br> ・3 -> Wednesday <br> ・4 -> Thursday <br> ・5 -> Friday <br> ・6 -> Saturday<hr>

**[Returns]**

- `weekday`: Int
  - A current weekday value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=4)
>>> datetime_.weekday_js  # Sunday
Int(0)

>>> datetime_ = ap.DateTime(year=2022, month=12, day=10)
>>> datetime_.weekday_js  # Saturday
Int(6)
```

## weekday_py property API

<!-- Docstring: apysc._time.datetime_.DateTime.weekday_py -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a current weekday value. This interface sets the weekday based on the Python value as follows: <br> ・0 -> Monday <br> ・1 -> Thursday <br> ・2 -> Wednesday <br> ・3 -> Thursday <br> ・4 -> Friday <br> ・5 -> Saturday <br> ・6 -> Sunday<hr>

**[Returns]**

- `weekday`: Int
  - A current weekday value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)
>>> datetime_.weekday_py  # Monday
Int(0)

>>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=4)
>>> datetime_.weekday_py  # Sunday
Int(6)
```