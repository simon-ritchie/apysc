# Array class remove and remove_at interfaces

This page will explain the `Array` class `remove` and `remove_at` method interfaces.

## What interfaces are these?

The `remove` method will remove a specified value from an array, and the `remove_at` method will remove a specified index value from an array.

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
