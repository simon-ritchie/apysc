# `apysc._type.string_apply_max_num_of_decimal_places_mixin` docstrings

## Module summary

The mix-in class implementation for the `String`'s `apply_max_num_of_decimal_places` method.

## `_get_py_str` function docstring

Get a Python value string.<hr>

**[Parameters]**

- `max_num_of_decimal_places`: Int
  - A maximum number of decimal places.
- `self_str`: Any
  - A self `String` instance.

<hr>

**[Returns]**

- `py_str`: str
  - A Python value string.

## `StringApplyMaxNumOfDecimalPlacesMixIn` class docstring

### `apply_max_num_of_decimal_places` method docstring

Apply a maximum number of decimal places limit to this string.<hr>

**[Parameters]**

- `max_num_of_decimal_places`: Union[int, Int]
  - A maximum number of decimal places.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `string`: String
  - An applied string.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> string = ap.String("123.456")
>>> string = string.apply_max_num_of_decimal_places(max_num_of_decimal_places=1)
>>> ap.assert_equal(string, "123.4")
```

<hr>

**[References]**

- [String class apply_max_num_of_decimal_places interface](https://simon-ritchie.github.io/apysc/en/string_apply_max_num_of_decimal_places.html)