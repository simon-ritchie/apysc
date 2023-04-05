# `apysc._type.to_string_mixin` docstrings

## Module summary

The mix-in class implementation for the `to_string` method.

## `ToStringMixIn` class docstring

### `to_string` method docstring

Convert this instance to a string.<hr>

**[Returns]**

- `string`: String
  - A converted string.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     background_color="#333", stage_width=200, stage_height=200
... )
>>> int_value: ap.Int = ap.Int(value=100)
>>> string: ap.String = int_value.to_string()
>>> ap.assert_equal(string, "100")
```