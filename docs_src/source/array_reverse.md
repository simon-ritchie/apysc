# Array class reverse interface

This page will explain the `Array` class `reverse` method interface.

## What interface is this?

The `reverse` method interface will reverse an array's values order in place.

## Basic usage

The `reverse` method requires no arguments and will return no value.

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 3, 5])
arr.reverse()
assert arr == [5, 3, 1]
```

## See also

- [Array class sort interface](array_sort.md)
