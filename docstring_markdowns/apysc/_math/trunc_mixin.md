# `apysc._math.trunc_mixin` docstrings

## Module summary

Class implementation for the truncate-related mix-in.

## `TruncMixIn` class docstring

### `trunc` method docstring

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

<hr>

**[References]**

- [Math max interface](https://simon-ritchie.github.io/apysc/en/math_trunc.html)