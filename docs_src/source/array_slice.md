# Array class slice interface

This page will explain the `Array` class `slice` method interface.

## What interface is this?

The `slice` method interface will extract the specified index range array's values and return a new array.

## Basic usage

The `slice` method requires the `start` and `end` arguments (`int` or `Int` values) and returns a new array.

If you specify 1 to the `start` argument and 3 to the `end` argument, this method will behave like the Python built-in list slice of `[1:3]`.

An original array will not be modified.

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 2, 3, 4])
sliced_arr: ap.Array[int] = arr.slice(start=1, end=3)
assert sliced_arr == [2, 3]
assert arr == [1, 2, 3, 4]
```
