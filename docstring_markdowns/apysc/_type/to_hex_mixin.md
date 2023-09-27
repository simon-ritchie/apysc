# `apysc._type.to_hex_mixin` docstrings

## Module summary

The mix-in class for the `to_hex` method.

## `ToHexMixIn` class docstring

### `to_hex` method docstring

Get a hexadecimal string (e.g., "1f").<hr>

**[Parameters]**

- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `hex_str`: String
  - A hexadecimal string (e.g., "1f").

<hr>

**[Notes]**

This method ignores floating point numbers.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> int_value: ap.Int = ap.Int(28)
>>> hex_str: ap.String = int_value.to_hex()
>>> hex_str
String("1c")

>>> number: ap.Number = ap.Number(28.5)
>>> hex_str = int_value.to_hex()
>>> hex_str
String("1c")
```

<hr>

**[References]**

- [Int and Number classes to_hex method](https://simon-ritchie.github.io/apysc/en/int_and_number_to_hex.html)