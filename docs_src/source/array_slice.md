# Array class slice interface

This page explains the `Array` class `slice` method interface.

## What interface is this?

The `slice` method interface extracts the specified index range array's values and returns a new array.

## Basic usage

The `slice` method requires the `start` and `end` arguments (`int` or `Int` values) and returns a new array.

If you specify 1 to the `start` argument and 3 to the `end` argument, this method behaves like the Python built-in list slice of `[1:3]`.

An original array is not modified.

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 2, 3, 4])
sliced_arr: ap.Array[int] = arr.slice(start=1, end=3)
assert sliced_arr == [2, 3]
assert arr == [1, 2, 3, 4]
```


## slice API

<!-- Docstring: apysc._type.array.Array.slice -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `slice(self, *, start:Union[int, apysc._type.int.Int, NoneType]=None, end:Union[int, apysc._type.int.Int, NoneType]=None) -> 'Array'`<hr>

**[Interface summary]** Slice this array by specified start and end indexes.<hr>

**[Parameters]**

- `start`: Int or int or None, default None
  - Slicing start index.
- `end`: Int or int or None, default None
  - Slicing end index (a result array does not contain this index).

<hr>

**[Returns]**

- `sliced_arr`: Array
  - Sliced array.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3, 4])
>>> arr.slice(start=1, end=3)
Array([2, 3])

>>> arr.slice(start=1)
Array([2, 3, 4])

>>> arr.slice(end=2)
Array([1, 2])
```