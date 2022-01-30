# Array class pop interface

This page explains the `Array` class `pop` method interface.

## What interface is this?

The `pop` method interface removes the last value from an array and returns that value.

## Basic usage

The `pop` method accepts no arguments and returns the last value, as follows:

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 2, 3])
last_value: int = arr.pop()
assert last_value == 3
```

## pop API

<!-- Docstring: apysc._type.array.Array.pop -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `pop(self) -> ~T`<hr>

**[Interface summary]** Remove this array's last value and return it.<hr>

**[Returns]**

- `value`: *
  - Removed value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> popped_val: int = arr.pop()
>>> popped_val
3

>>> arr
Array([1, 2])
```