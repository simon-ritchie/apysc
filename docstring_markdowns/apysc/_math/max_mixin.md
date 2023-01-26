# `apysc._math.max_mixin` docstrings

## Module summary

Class implementation for the max-related mix-in.

## `_get_max_float_value` function docstring

Get a maximum float value from a specified array.<hr>

**[Parameters]**

- `values`: Array[Union[Int, Number, int, float]]
  - An array of numbers.

<hr>

**[Returns]**

- `max_value`: float
  - A maximum float value.

## `_get_max_value_variable_name_suffix_from_arr` function docstring

Get a maximum value's variable name suffix from a specified array.<hr>

**[Parameters]**

- `arr`: Array
  - An array of numbers.

<hr>

**[Returns]**

- `suffix`: str
  - An extracted variable name suffix.

## `MaxMixIn` class docstring

### `max` method docstring

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
>>> arr: ap.Array = ap.Array([10, 9.5, ap.Int(8), ap.Number(8.5)])
>>> max_value: ap.Number = ap.Math.max(values=arr)
>>> max_value
Number(10.0)
```

<hr>

**[References]**

- [Math max interface](https://simon-ritchie.github.io/apysc/en/math_max.html)