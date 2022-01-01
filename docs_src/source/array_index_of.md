# Array class index_of interface

This page explains the `Array` class `index_of` method interface.

## What interface is this?

The `index_of` method returns the specified value's index in the array.

## Basic usage

The `index_of` method requires the `value` argument and returns the found value's index in the array.

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 3, 5])
index: ap.Int = arr.index_of(value=3)
assert index == 1
```

If there is no found value, the return index becomes `-1`.

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 3, 5])
index: ap.Int = arr.index_of(value=2)
assert index == -1
```
