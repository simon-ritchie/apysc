# `apysc._type.string_lower_mixin` docstrings

## Module summary

The mix-in class implementation for the `String`'s `lower` method.

## `StringLowerMixIn` class docstring

### `lower` method docstring

Get a copied lower case string.<hr>

**[Returns]**

- `string`: String
  - A copied lower case string.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> string: ap.String = ap.String("HELLO")
>>> string = string.lower()
>>> string
String("hello")
```

<hr>

**[References]**

- [String class lower method](https://simon-ritchie.github.io/apysc/en/string_lower.html)