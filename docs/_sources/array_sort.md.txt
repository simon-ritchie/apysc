# Array class sort interface

This page will explain the `Array` class `sort` method interface.

## What interface is this?

The `sort` method interface will sort an array's values (ascending order).

## Basic usage

The `sort` method requires no arguments and sorts values in place (no return value).

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([5, 1, 3])
arr.sort()
assert arr == [1, 3, 5]
```
