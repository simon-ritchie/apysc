# `apysc._loop._for` docstrings

## Module summary

This module is for the `For` loop class implementation.

## `For` class docstring

The class to append for the (loop) expression.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array(range(3))
>>> with ap.For(arr) as i:
...     ap.trace("Loop index is:", i)
...
```

<hr>

**[References]**

- [For](https://simon-ritchie.github.io/apysc/en/for.html)

### `__enter__` method docstring

This class calls this method at the with-statement.<hr>

**[Returns]**

- `i_or_key`: Int or String
  - Loop index or dictionary key.

### `__exit__` method docstring

This class calls this method at the with-statement.

### `__init__` method docstring

The class to append for the (loop) expression.<hr>

**[Parameters]**

- `arr_or_dict`: Array or Dictionary
  - Array or Dictionary instance to iterate.
- `locals_`: dict or None, default None
  - Current scope's local variables. Set locals() value to this argument. If specified, this interface reverts all local scope VariableNameMixIn variables (like Int, Sprite) at the end of a `For` scope. This setting is useful when you don't want to update each variable by implementing the `For` scope.
- `globals_`: dict or None, default None
  - Current scope's global variables. Set globals() value to this argument. This setting works the same way as the locals_ argument.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array(range(3))
>>> with ap.For(arr) as i:
...     ap.trace("Loop index is:", i)
...
```

<hr>

**[References]**

- [For](https://simon-ritchie.github.io/apysc/en/for.html)

### `_append_arr_enter_expression` method docstring

Append for loop start expression (for Array value).<hr>

**[Parameters]**

- `i`: Int
  - Loop index value.

### `_append_dict_enter_expression` method docstring

Append for loop start expression (for Dictionary value).<hr>

**[Parameters]**

- `key`: String
  - Loop (dictionary) key value.

### `_validate_arr_or_dict_val_type` method docstring

Validate loop value type is Array of Dictionary.<hr>

**[Parameters]**

- `arr_or_dict`: Array or Dictionary
  - Value to be checked.

<hr>

**[Raises]**

- TypeError: If a value type is neither Array nor Dictionary.