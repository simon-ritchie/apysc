# `apysc._type.string_slice_mixin` docstrings

## Module summary

The mix-in class implementation for the `slice` method.

## `StringSliceMixIn` class docstring

### `slice` method docstring

Get a sliced string based on the specified arguments range.<hr>

**[Parameters]**

- `start`: Union[int, "Int"]
  - A start index of the slice range.
- `end`: Optional[Union[int, "Int"]], optional
  - An end index of the slice range. If this argument is not specified, this method skips the end position's slicing.
- `variable_name_suffix`: str, default ""
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `result`: String
  - A sliced result string.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     stage_width=0,
...     stage_height=0,
...     background_color=ap.Color("#333"),
...     stage_elem_id="stage",
... )
>>> string: ap.String = ap.String("012345")
>>> result_string: ap.String = string.slice(start=0)
>>> result_string
String("012345")

>>> result_string = string.slice(start=1)
>>> result_string
String("12345")

>>> result_string = string.slice(start=0, end=2)
>>> result_string
String("01")

>>> result_string = string.slice(start=2, end=4)
>>> result_string
String("23")

>>> result_string = string.slice(start=-2)
>>> result_string
String("45")

>>> result_string = string.slice(start=-3, end=-1)
>>> result_string
String("34")
```

<hr>

**[References]**

- [String class slice method](https://simon-ritchie.github.io/apysc/en/string_slice.html)