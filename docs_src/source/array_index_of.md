# Array class index_of interface

This page explains the `Array` class `index_of` method interface.

## What interface is this?

The `index_of` method returns the specified value's index in the array.

## Basic usage

The `index_of` method requires the `value` argument and returns the found value's index in the array.

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 3, 5])
index: ap.Int = arr.index_of(value=3)
assert index == 1
```

If there is no found value, the return index becomes `-1`.

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 3, 5])
index: ap.Int = arr.index_of(value=2)
assert index == -1
```


## index_of API

<!-- Docstring: apysc._type.array.Array.index_of -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `index_of(self, value:~T) -> apysc._type.int.Int`<hr>

**[Interface summary]** Search specified value's index and return it.<hr>

**[Parameters]**

- `value`: *
  - Any value to search.

<hr>

**[Returns]**

- `index`: Int
  - Found position of index. If this array does not contain a value, this interface returns -1.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 3, 5])
>>> arr.index_of(3)
Int(1)
```