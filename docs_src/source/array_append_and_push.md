# Array class append and push interfaces

This page explains the `Array` class `append` and `push` method interfaces.

## What interfaces are these?

The `append` and `push` method interfaces append any value to the end of an array. These interfaces behave the same (`append` is similar to the Python built-in and the `push` interface is similar to the JavaScript).

## Basic usage

The `append` and `push` methods require the first argument of the `value`\.

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 2])
arr.append(value=3)
assert arr == [1, 2, 3]

arr.push(value=4)
assert arr == [1, 2, 3, 4]
```