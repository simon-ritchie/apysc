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


## append API

<!-- Docstring: apysc._type.array.Array.append -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `append(self, value:~T) -> None`<hr>

**[Interface summary]** Add any value to the end of this array. This method behaves the same `push` method.<hr>

**[Parameters]**

- `value`: *
  - Any value to append.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> arr.append(4)
>>> arr
Array([1, 2, 3, 4])
```

## push API

<!-- Docstring: apysc._type.array.Array.push -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `push(self, value:~T) -> None`<hr>

**[Interface summary]** Add any value to the end of this array. This method behaves the same `append` method.<hr>

**[Parameters]**

- `value`: *
  - Any value to append.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> arr.push(4)
>>> arr
Array([1, 2, 3, 4])
```