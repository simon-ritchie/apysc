# `apysc._type.dictionary` docstrings

## Module summary

Class implementation for the dictionary value.

## `Dictionary` class docstring

Dictionary class for the apysc library.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> dictionary: ap.Dictionary = ap.Dictionary({'a': 10})
>>> dictionary
Dictionary({'a': 10})

>>> dictionary['a']
10

>>> dictionary['b'] = 20
>>> dictionary['b']
20

>>> dictionary.length
Int(2)

>>> value_1: int = dictionary.get('c', default=0)
>>> value_1
0
```

<hr>

**[References]**

- [Dictionary document](https://simon-ritchie.github.io/apysc/dictionary.html)
- [Dictionary class generic type settings document](https://simon-ritchie.github.io/apysc/dictionary_generic.html)

### `__delitem__` method docstring

Delete specified key's value from a dictionary.<hr>

**[Parameters]**

- `key`: _K
  - Dictionary key to delete.

### `__eq__` method docstring

Equal comparison method.<hr>

**[Parameters]**

- `other`: *
  - The other value to compare. dict or Dictionary types are acceptable.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### `__getitem__` method docstring

Get a specified key's single value.<hr>

**[Parameters]**

- `key`: _K
  - Dictionary key.

<hr>

**[Returns]**

- `value`: *
  - Specified key's value.

### `__init__` method docstring

Dictionary class for the apysc library.<hr>

**[Parameters]**

- `value`: dict or Dictionary
  - Initial dictionary value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> dictionary: ap.Dictionary = ap.Dictionary({'a': 10})
>>> dictionary
Dictionary({'a': 10})

>>> dictionary['a']
10

>>> dictionary['b'] = 20
>>> dictionary['b']
20
```

<hr>

**[References]**

- [Dictionary document](https://simon-ritchie.github.io/apysc/dictionary.html)
- [Dictionary class generic type settings document](https://simon-ritchie.github.io/apysc/dictionary_generic.html)

### `__len__` method docstring

This method is disabled and can't use from a Dictionary instance.

### `__ne__` method docstring

Noe equal comparison method.<hr>

**[Parameters]**

- `other`: *
  - The other value to compare. dict or Dictionary types are acceptable.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### `__repr__` method docstring

Get a representation string of this instance.<hr>

**[Returns]**

- `repr_str`: str
  - Representation string of this instance.

### `__setitem__` method docstring

Set value to a specified key position.<hr>

**[Parameters]**

- `key`: _K
  - Dictionary key to set value.
- `value`: *
  - Any value to set.

### `__str__` method docstring

String conversion method.<hr>

**[Returns]**

- `string`: str
  - Converted value string.

### `_append_constructor_expression` method docstring

Append constructor expression.

### `_append_delitem_expression` method docstring

Append __delitem__ method expression.<hr>

**[Parameters]**

- `key`: _K
  - Dictionary key to delete.

### `_append_eq_expression` method docstring

Append an __eq__ expression.<hr>

**[Parameters]**

- `result`: Boolean
  - A result boolean value.
- `other`: Dictionary
  - The Dictionary's other value to compare.

### `_append_get_expression` method docstring

Append the `get` method expression.<hr>

**[Parameters]**

- `key`: _K
  - Target key.
- `result_value`: Any
  - Extracted value or a default value.
- `default`: Any
  - Any default value. Basic apysc types (e.g., Int, Number, String, and so on) are necessary.

### `_append_getitem_expression` method docstring

Append __getitem__ expression.<hr>

**[Parameters]**

- `key`: _K
  - Dictionary key.
- `value`: *
  - Specified key's value.

### `_append_length_expression` method docstring

Append length method expression.<hr>

**[Parameters]**

- `length`: Int
  - Created length Int variable.

### `_append_ne_expression` method docstring

Append a __ne__ expression.<hr>

**[Parameters]**

- `result`: Boolean
  - A result boolean value.
- `other`: Dictionary
  - The Dictionary's other value to compare.

### `_append_setitem_expression` method docstring

Append __setitem__ method expression.<hr>

**[Parameters]**

- `key`: _K
  - Dictionary key to check.
- `value`: *
  - Any value to set.

### `_append_value_setter_expression` method docstring

Append value's setter expression.<hr>

**[Parameters]**

- `value`: dict or Dictionary.
  - Dictionary value to set.

### `_get_builtin_type_key` method docstring

Get a built-in type's key (str, int, or float) from a specified key.<hr>

**[Parameters]**

- `key`: _K
  - Target key value (including String, Int, and Number).

<hr>

**[Returns]**

- `key`: str or int or float
  - Built-in type's key.

### `_get_dict_value` method docstring

Get a dict value from a specified value.<hr>

**[Parameters]**

- `value`: dict or Dictionary
  - Specified dictionary value.

<hr>

**[Returns]**

- `dict_val`: dict
  - Converted dict value.

### `_make_snapshot` method docstring

Make values' snapthot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `_revert` method docstring

Revert values if snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `_validate_acceptable_value_type` method docstring

Validate whether a specified value is an acceptable type or not.<hr>

**[Parameters]**

- `value`: dict or Dictionary
  - Dictionary value to check.

<hr>

**[Raises]**

- TypeError: If specified value's type is not a Dictionary or dict value.

### `_validate_key_type_is_str_or_numeric` method docstring

Validate whether a key's value type is acceptable (str or int or float) or not.<hr>

**[Parameters]**

- `key`: _K
  - Dictionary key to check.

<hr>

**[Raises]**

- ValueError: If a key's type is not String, Int, Number, str, int, or float.

### `get` method docstring

Get a specified key dictionary value. If this dictionary hasn't a specified key, this interface returns a default value.<hr>

**[Parameters]**

- `key`: _K
  - Target key.
- `default`: DefaultType or None, optional
  - Any default value.

<hr>

**[Returns]**

- `result_value`: Any
  - Extracted value or a default value.

<hr>

**[Examples]**

```py
>>> from typing import Optional
>>> import apysc as ap
>>> dictionary: ap.Dictionary = ap.Dictionary({'a': 10})
>>> value_1: Optional[int] = dictionary.get('a')
>>> value_1
10

>>> value_2: Optional[int] = dictionary.get('b')
>>> print(value_2)
None

>>> value_3: int = dictionary.get('c', default=0)
>>> value_3
0
```

<hr>

**[References]**

- [Dictionary get interface document](https://simon-ritchie.github.io/apysc/dictionary_get.html)