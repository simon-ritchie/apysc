# `apysc._type.to_fixed_mixin` docstrings

## Module summary

The mix-in class implementation for the `to_fixed` method.

## `ToFixedMixIn` class docstring

### `to_fixed` method docstring

Convert value to fixed floating point string notation.<hr>

**[Parameters]**

- `digits`: int or Int
  - A floating point digit number (0 to 100 value is acceptable).
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `result_str`: String
  - A converted string.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> num: ap.Number = ap.Number(10.789)
>>> fixed_float_str: ap.String = num.to_fixed(digits=2)
>>> fixed_float_str
String("10.79")

>>> fixed_float_str = num.to_fixed(digits=5)
>>> fixed_float_str
String("10.78900")

>>> fixed_float_str = num.to_fixed(digits=0)
>>> fixed_float_str
String("11")
```