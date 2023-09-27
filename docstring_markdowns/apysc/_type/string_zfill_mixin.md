# `apysc._type.string_zfill_mixin` docstrings

## Module summary

The mix-in class for the String's `zfill` method.

## `StringZfillMixIn` class docstring

### `zfill` method docstring

Return a copy of the string left filled with 0.<hr>

**[Parameters]**

- `width`: Union[int, "Int"]
  - A width (length) of the string.

<hr>

**[Returns]**

- `result`: String
  - A result string.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _: ap.Stage = ap.Stage()
>>> string: ap.String = ap.String("1")
>>> string = string.zfill(width=1)
>>> string
String("1")

>>> string = string.zfill(width=3)
>>> string
String("001")

>>> string = string.zfill(width=5)
>>> string
String("00001")
```

<hr>

**[References]**

- [String class zfill method](https://simon-ritchie.github.io/apysc/en/string_zfill.html)