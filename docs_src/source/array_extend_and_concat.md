# Array class extend and concat interfaces

This page explains the `Array` class `extend` and `concat` method interfaces.

## What interfaces are these?

The `extend` and `concat` method interfaces are the two arrays' concatenation interfaces.

The `extend` method updates an original array in place and returns the `None`. The `concat` method returns the concatenated array, and an original one is not updated.

## Basic usage

The `extend` and `concat` methods require other iterable objects, like the `list`\, `tuple`\, or `Array` value at the first argument, as follows:

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 2])
arr.extend([3, 4])
assert arr == [1, 2, 3, 4]

other_arr: ap.Array[int] = arr.concat([5, 6])
assert other_arr == [1, 2, 3, 4, 5, 6]
assert arr == [1, 2, 3, 4]
```
