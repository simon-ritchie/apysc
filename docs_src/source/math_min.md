# Math min interface

This page explains the `Math` class's `min` class method interface.

## What interface is this?

The `min` class method interface returns a minimum number from a specified array of numbers.

## Basic usage

The `min` interface requires an `Array` value argument (`values`).

It returns a `Number` value.

Notes: Regardless of the `Array` values' type, this interface returns a `Number` type value.

```py
# runnable
import apysc as ap

ap.Stage()
arr: ap.Array = ap.Array([9, 10, ap.Int(8), ap.Number(9.5), 11])
min_value: ap.Number = ap.Math.min(values=arr)
assert min_value == 8
```

## Math.min API

<!-- Docstring: apysc._math.min_mixin.MinMixIn.min -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `min(values: apysc._type.array.Array) -> apysc._type.number.Number`<hr>

**[Interface summary]**

Get a minimum number from a specified array's values.<hr>

**[Parameters]**

- `values`: Array[Union[Int, Number, int, float]]
  - An array of numbers.

<hr>

**[Returns]**

- `min_value`: Number
  - Minimum number in an array.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> arr: ap.Array = ap.Array([10, 9.5, ap.Int(8), ap.Number(8.5)])
>>> min_value: ap.Number = ap.Math.min(values=arr)
>>> min_value
Number(8.0)
```