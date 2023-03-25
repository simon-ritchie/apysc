# `apysc._type.string_split_mixin` docstrings

## Module summary

Class implementation for the `String` class's `split` mix-in.

## `StringSplitMixIn` class docstring

### `_append_split_expression` method docstring

Append a `split` method's expression string.<hr>

**[Parameters]**

- `splitted_strs`: Array[String]
  - A splitted strings' array.
- `sep`: String
  - A separator string.

### `split` method docstring

Split a current string with a separator string.<hr>

**[Parameters]**

- `sep`: String
  - A separator string.

<hr>

**[Returns]**

- `splitted_strs`: Array[String]
  - A splitted strings' array.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> str_value: ap.String = ap.String("Lorem ipsum dolor sit")
>>> splitted_strs: ap.Array[ap.String] = str_value.split(sep=ap.String(" "))
>>> ap.assert_arrays_equal(splitted_strs, ["Lorem", "ipsum", "dolor", "sit"])
```

<hr>

**[References]**

- [String class split interface](https://simon-ritchie.github.io/apysc/en/string_split.html)