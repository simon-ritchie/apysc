# Array class remove and remove_at interfaces

This page explains the `Array` class `remove` and `remove_at` method interfaces.

## What interfaces are these?

The `remove` method removes a specified value from an array, and the `remove_at` method removes a specified index value.

## Basic usage

The `remove` method requires target value at the first argument, as follows:

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 2, 3])
arr.remove(value=2)
assert arr == [1, 3]
```

The `remove_at` method requires index (`int` or `Int` value) at the first argument, as follows:

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 2, 3])
arr.remove_at(index=1)
assert arr == [1, 3]
```