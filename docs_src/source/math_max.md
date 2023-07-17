# Math max interface

This page explains the `Math` class's `max` class method interface.

## What interface is this?

The `max` class method interface returns a maximum number from a specified array of numbers.

## Basic usage

The `max` interface requires an `Array` value argument (`values`).

It returns a `Number` value.

Notes: Regardless of the `Array` values' type, this interface returns a `Number` type value.

```py
# runnable
import apysc as ap

ap.Stage()
arr: ap.Array = ap.Array([9, 10, ap.Int(8), ap.Number(9.5), 11])
max_value: ap.Number = ap.Math.max(values=arr)
assert max_value == 11
```

## Math.max API

<!-- Docstring: apysc._math.max_mixin.MaxMixIn.max -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `max(values: apysc._type.array.Array) -> apysc._type.number.Number`<hr>

**[Interface summary]**

Get a maximum number from a specified array's values.<hr>

**[Parameters]**

- `values`: Array[Union[Int, Number, int, float]]
  - An array of numbers.

<hr>

**[Returns]**

- `max_value`: Number
  - Maximum number in an array.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> arr: ap.Array = ap.Array([10, 9.5, ap.Int(8), ap.Number(8.5)])
>>> max_value: ap.Number = ap.Math.max(values=arr)
>>> max_value
Number(10.0)
```