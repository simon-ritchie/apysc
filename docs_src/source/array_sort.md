# Array class sort interface

This page explains the `Array` class `sort` method interface.

## What interface is this?

The `sort` method interface sorts an array's values (ascending order).

## Basic usage

The `sort` method requires no arguments and sorts values in place (no return value).

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([5, 1, 3])
arr.sort()
assert arr == [1, 3, 5]
```

## Sort values by descending order

If you need to sort values by descending order, then use the `reverse` method also:

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 3, 2])
arr.sort()
arr.reverse()
assert arr == [3, 2, 1]
```

## See also

- [Array class reverse interface](array_reverse.md)


## sort API

<!-- Docstring: apysc._type.array.Array.sort -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `sort(self, *, ascending:bool=True) -> None`<hr>

**[Interface summary]** Sort this array in place.<hr>

**[Parameters]**

- `ascending`: bool, default True
  - Sort by ascending or not. If False is specified, this interface sorts values descending.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([3, 5, 1, 4, 2])
>>> arr.sort()
>>> arr
Array([1, 2, 3, 4, 5])

>>> arr.sort(ascending=False)
>>> arr
Array([5, 4, 3, 2, 1])
```