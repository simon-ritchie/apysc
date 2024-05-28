# `apysc._math.clamp_mixin` docstrings

## Module summary

Class implementation for the clamp-related mix-in.

## `ClampMixIn` class docstring

### `clamp` method docstring

Sets the value within a specified minimum and maximum range. If the value is less than the minimum, this method returns the minimum value. If the value is greater than the maximum, this method returns the maximum value.<hr>

**[Parameters]**

- `value`: _ValueType
  - Target `Int` or `Number` value.
- `min_`: _ValueType
  - Minimum value.
- `max_`: _ValueType
  - Maximum value.

<hr>

**[Returns]**

- `result`: _ValueType
  - Clamped value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> value: ap.Int = ap.Int(5)
>>> value = ap.Math.clamp(value=value, min_=ap.Int(10), max_=ap.Int(20))
>>> value
Int(10)

>>> value = ap.Int(25)
>>> value = ap.Math.clamp(value=value, min_=ap.Int(10), max_=ap.Int(20))
>>> value
Int(20)
```