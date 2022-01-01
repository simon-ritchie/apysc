# Array class join interface

This page explains the `Array` class `join` method interface.

## What interface is this?

The `join` method returns a joined `String` with the specified separator string.

## Basic usage

The `join` method requires the `sep` argument as the separator, as follows:

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 2, 3])
joined: ap.String = arr.join(sep=',')
assert joined == '1,2,3'
```
