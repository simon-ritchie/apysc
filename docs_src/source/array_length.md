# Array class length interface

This page explains the `Array` class `length` property interface.

## What interface is this?

The `length` attribute interface returns a current array's values length.

## Basic usage

The `length` property has the only getter interface. The return value type is the `Int` type.

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 2, 3, 4])
length: ap.Int = arr.length
assert length == 4
```

## Notes of the len() function

The `Array` class is not supported the Python built-in `len()` function, and its function raises an exception. Please use the `length` property instead.

```py
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 2, 3, 4])
len(arr)
```

```
Exception: Array instance can't apply len function. Please use length property instead.
```