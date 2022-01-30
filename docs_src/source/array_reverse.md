# Array class reverse interface

This page explains the `Array` class `reverse` method interface.

## What interface is this?

The `reverse` method interface reverses an array's values order in place.

## Basic usage

The `reverse` method requires no arguments and returns no value.

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 3, 5])
arr.reverse()
assert arr == [5, 3, 1]
```

## See also

- [Array class sort interface](array_sort.md)


## reverse API

<!-- Docstring: apysc._type.array.Array.reverse -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `reverse(self) -> None`<hr>

**[Interface summary]** Reverse this array in place.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> arr.reverse()
>>> arr
Array([3, 2, 1])
```