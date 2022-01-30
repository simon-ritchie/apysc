# Array class remove and remove_at interfaces

This page explains the `Array` class `remove` and `remove_at` method interfaces.

## What interfaces are these?

The `remove` method removes a specified value from an array, and the `remove_at` method removes a specified index value.

## Basic usage

The `remove` method requires target value at the first argument, as follows:

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 2, 3])
arr.remove(value=2)
assert arr == [1, 3]
```

The `remove_at` method requires index (`int` or `Int` value) at the first argument, as follows:

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 2, 3])
arr.remove_at(index=1)
assert arr == [1, 3]
```


## remove API

<!-- Docstring: apysc._type.array.Array.remove -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `remove(self, value:~T) -> None`<hr>

**[Interface summary]** Remove specified value from this array.<hr>

**[Parameters]**

- `value`: Any
  - Value to remove.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 3, 5])
>>> arr.remove(3)
>>> arr
Array([1, 5])
```

## remove_at API

<!-- Docstring: apysc._type.array.Array.remove_at -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `remove_at(self, index:Union[int, apysc._type.int.Int]) -> None`<hr>

**[Interface summary]** Remove specified index value from this array.<hr>

**[Parameters]**

- `index`: Int or int
  - Index to remove value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> arr.remove_at(1)
>>> arr
Array([1, 3])
```