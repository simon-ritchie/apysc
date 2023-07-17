# `apysc._type.string_lstrip_mixin` docstrings

## Module summary

The mix-in class implementation for the `lstrip` method.

## `_create_string_none_case_expression` function docstring

Create an expression for the string's `None` case.<hr>

**[Parameters]**

- `result_string`: String
  - A result string.
- `self_variable_name`: str
  - An instance's self-variable name.

<hr>

**[Returns]**

- `expression`: str
  - A created expression.

## `_create_string_not_none_case_expression` function docstring

Create an expression for the string's not `None` case.<hr>

**[Parameters]**

- `result_string`: String
  - A result string.
- `removing_string`: Union[str, "String"]
  - A removing target string.
- `self_variable_name`: str
  - An instance's self-variable name.
- `variable_name_suffix`: str
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `expression`: str
  - A created expression.

## `_get_py_str_from_current_value` function docstring

Get a Python string from a current string value.<hr>

**[Parameters]**

- `self_str`: Any
  - A self-string.
- `removing_string`: Optional[Union[str, String]]
  - A removing target string.

<hr>

**[Returns]**

- `py_str`: str
  - A Python string.

## `StringLStripMixIn` class docstring

### `lstrip` method docstring

Remove a specified character or string from the beginning of this value.<hr>

**[Parameters]**

- `string`: Optional[Union[str, "String"]], optional
  - A character or string to remove from the beginning of this value. If this argument is `None` (default), this method removes spaces and line breaks.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `result`: String
  - A stripped result string.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> string: ap.String = ap.String("   aabbcc  ")
>>> string = string.lstrip()
>>> string
String("aabbcc  ")

>>> string = ap.String("aabbccaa")
>>> string = string.lstrip(string="a")
>>> string
String("bbccaa")
```

<hr>

**[References]**

- [String class lstrip interface](https://simon-ritchie.github.io/apysc/en/string_lstrip.html)