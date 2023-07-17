# DateTime class set_month_end interface

This page explains the `DateTime` class's `set_month_end` method interface.

## What interface is this?

The `set_month_end` method interface sets the current month's end date.

For instance, if the current date is 05/12/2022, this method sets 31/12/2022.

## Basic usage

This method interface requires no arguments.

```py
# runnable
import apysc as ap

ap.Stage()
datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)
datetime_.set_month_end()
assert datetime_.day == 31
```