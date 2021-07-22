# Array class insert and insert_at interfaces

This page will explain the `Array` class `insert` and `insert_at` method interfaces.

## What interfaces are these?

The `insert` and `insert_at` method interfaces will append any value at the specified index. Both interfaces behave the same way (the `insert` is the alias of the `insert_at`).

## Basic usage

The `insert` and `insert_at` have the same argument, the `index` and `value`. The `index` argument accepts an `int` and `Int` value.

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 4])
arr.insert(index=1, value=2)
assert arr == [1, 2, 4]

index: ap.Int = ap.Int(2)
arr.insert_at(index=index, value=3)
assert arr == [1, 2, 3, 4]
```
