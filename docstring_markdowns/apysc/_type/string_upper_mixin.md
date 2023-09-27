# `apysc._type.string_upper_mixin` docstrings

## Module summary

The mix-in class implementation for the `String`'s `upper` method.

## `StringUpperMixIn` class docstring

### `upper` method docstring

Get a copied upper case string.<hr>

**[Returns]**

- `string`: String
  - A copied upper case string.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> string: ap.String = ap.String("Hello")
>>> string = string.upper()
>>> string
String("HELLO")
```

<hr>

**[References]**

- [String class upper method](https://simon-ritchie.github.io/apysc/en/string_upper.html)