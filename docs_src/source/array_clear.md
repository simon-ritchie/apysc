# Array class clear interface

This page explains the `Array` class `clear` method interface.

## What interface is this?

The `clear` method clears an Array's value. This interface makes an Array's value empty.

## Basic usage

The `clear` method requires no arguments.

```py
# runnable
import apysc as ap

ap.Stage()
arr: ap.Array = ap.Array([10, 20, 30])
arr.clear()
assert arr == []
```