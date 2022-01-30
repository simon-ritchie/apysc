# Array class insert and insert_at interfaces

This page explains the `Array` class `insert` and `insert_at` method interfaces.

## What interfaces are these?

The `insert` and `insert_at` method interfaces append any value at the specified index. Both interfaces behave the same way (the `insert` is the alias of the `insert_at`).

## Basic usage

The `insert` and `insert_at` have the same argument, the `index` and `value`\. The `index` argument accepts an `int` and `Int` value.

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 4])
arr.insert(index=1, value=2)
assert arr == [1, 2, 4]

index: ap.Int = ap.Int(2)
arr.insert_at(index=index, value=3)
assert arr == [1, 2, 3, 4]
```


## insert API

<!-- Docstring: apysc._type.array.Array.insert -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `insert(self, index:Union[int, apysc._type.int.Int], value:~T) -> None`<hr>

**[Interface summary]** Insert value to this array at a specified index. This interface behaves the same `insert_at` method.<hr>

**[Parameters]**

- `index`: int or Int
  - Index to append value.
- `value`: *
  - Any value to append.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 3])
>>> arr.insert(index=1, value=2)
>>> arr
Array([1, 2, 3])
```

## insert_at API

<!-- Docstring: apysc._type.array.Array.insert_at -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `insert_at(self, index:Union[int, apysc._type.int.Int], value:~T) -> None`<hr>

**[Interface summary]** Insert value to this array at a specified index. This interface behaves the same `insert` method.<hr>

**[Parameters]**

- `index`: int or Int
  - Index to append value.
- `value`: *
  - Any value to append.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 3])
>>> arr.insert_at(index=1, value=2)
>>> arr
Array([1, 2, 3])
```