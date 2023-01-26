# `apysc._math.min_mixin` docstrings

## Module summary

Class implementation for the min-related mix-in.

## `_get_min_float_value` function docstring

Get a minimum float value from a specified array.<hr>

**[Parameters]**

- `values`: Array[Union[Int, Number, int, float]]
  - An array of numbers.

<hr>

**[Returns]**

- `min_value`: float
  - A minimum float value.

## `_get_min_value_variable_name_suffix_from_arr` function docstring

Get a minimum value's variable name suffix from a specified array.<hr>

**[Parameters]**

- `arr`: Array
  - An array of numbers.

<hr>

**[Returns]**

- `suffix`: str
  - An extracted variable name suffix.

## `MinMixIn` class docstring

### `min` method docstring

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
>>> arr: ap.Array = ap.Array([10, 9.5, ap.Int(8), ap.Number(8.5)])
>>> min_value: ap.Number = ap.Math.min(values=arr)
>>> min_value
Number(8.0)
```

<hr>

**[References]**

- [Math min interface](https://simon-ritchie.github.io/apysc/en/math_min.html)