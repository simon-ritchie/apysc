# Array class pop interface

This page will explain the `Array` class `pop` method interface.

## What interface is this?

The `pop` method interface will remove the last value from an array and return that value.

## Basic usage

The `pop` method accepts no arguments and returns the last value, as follows:

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 2, 3])
last_value: int = arr.pop()
assert last_value == 3
```
