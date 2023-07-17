# Math trunc interface

This page explains the `Math` class's `trunc` class method interface.


## What interface is this?

The `trunc` class method interface truncates a fraction value and returns an integer value.

## Basic usage

The `trunc` interface requires `Int`, `Number`, `String`, or `Boolean` value argument.

If an argument is a `Number` or `String` value, this interface truncates a fraction value and converts it to the `Int` type.

If an argument is a `Boolean` value, this interface returns 0 or 1 `Int` value.

```py
# runnable
import apysc as ap

ap.Stage()
result_int: ap.Int = ap.Math.trunc(value=ap.Int(10))
assert result_int == 10

result_int = ap.Math.trunc(value=ap.Number(8.5))
assert result_int == 8

result_int = ap.Math.trunc(value=ap.String("7.6"))
assert result_int == 7

result_int = ap.Math.trunc(value=ap.Boolean(True))
assert result_int == 1
```

## Math.trunc API

<!-- Docstring: apysc._math.trunc_mixin.TruncMixIn.trunc -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `trunc(value: Union[apysc._type.int.Int, apysc._type.number.Number, apysc._type.string.String, apysc._type.boolean.Boolean]) -> apysc._type.int.Int`<hr>

**[Interface summary]**

Truncate a fraction value from a specified value.<hr>

**[Parameters]**

- `value`: Union[Int, Number, String, Boolean]
  - A value to truncate a fraction value. If a specified value is the `Number`'s, `String`'s, or `Boolean`'s type, the return value becomes an `Int`'s value.

<hr>

**[Returns]**

- `result`: Int
  - Truncated and converted to `Int`'s value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> result_int: ap.Int = ap.Math.trunc(value=ap.Int(10))
>>> result_int
Int(10)

>>> result_int = ap.Math.trunc(value=ap.Number(8.5))
>>> result_int
Int(8)

>>> result_int = ap.Math.trunc(value=ap.String("7.6"))
>>> result_int
Int(7)

>>> result_int = ap.Math.trunc(value=ap.Boolean(True))
>>> result_int
Int(1)

>>> result_int = ap.Math.trunc(value=ap.Boolean(False))
>>> result_int
Int(0)
```