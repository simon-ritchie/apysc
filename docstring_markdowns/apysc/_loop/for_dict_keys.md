# `apysc._loop.for_dict_keys` docstrings

## Module summary

The loop implementation class for the `ap.Dictionary` keys.

## `ForDictKeys` class docstring

The loop implementation class for the `ap.Dictionary` keys.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> dict_: ap.Dictionary[ap.String, ap.Boolean] = ap.Dictionary(
...     {
...         ap.String("apple"): ap.Boolean(True),
...         ap.String("orange"): ap.Boolean(False),
...     }
... )
>>> keys: ap.Array[ap.String] = ap.Array([])
>>> with ap.ForDictKeys(dict_=dict_, dict_key_type=ap.String) as key:
...     keys.append(key)
...
>>> ap.assert_arrays_equal(
...     keys,
...     ["apple", "orange"],
... )
```

<hr>

**[References]**

- [ForDictKeys class](https://simon-ritchie.github.io/apysc/en/for_dict_keys.html)

### `__enter__` method docstring

The entering method for the beginning of with-statement.<hr>

**[Returns]**

- `dict_key`: _DictKey
  - A dictionary key of iteration.

### `__init__` method docstring

The loop implementation class for the `ap.Dictionary` keys.<hr>

**[Parameters]**

- `dict_`: Dictionary[_DictKey, Any]
  - A dictionary to iterate.
- `dict_key_type`: Type[_DictKey]
  - A dictionary key type. This interface accepts hashable types, such as the `String`, `Int`, `Number`, or `Boolean`.
- `locals_`: Optional[Dict[str, Any]], optional
  - Current scope's local variables. Set locals() value to this argument. If specified, this interface reverts all local scope VariableNameMixIn variables (like Int, Sprite) at the end of a with-statement scope. This setting is useful when you don't want to update each variable.
- `globals_`: Optional[Dict[str, Any]], optional
  - Current scope's global variables. Set globals() value to this argument. This setting works the same way as the locals_ argument.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> dict_: ap.Dictionary[ap.String, ap.Boolean] = ap.Dictionary(
...     {
...         ap.String("apple"): ap.Boolean(True),
...         ap.String("orange"): ap.Boolean(False),
...     }
... )
>>> keys: ap.Array[ap.String] = ap.Array([])
>>> with ap.ForDictKeys(dict_=dict_, dict_key_type=ap.String) as key:
...     keys.append(key)
...
>>> ap.assert_arrays_equal(
...     keys,
...     ["apple", "orange"],
... )
```

<hr>

**[References]**

- [ForDictKeys class](https://simon-ritchie.github.io/apysc/en/for_dict_keys.html)

### `_get_last_scope` method docstring

Get a target last scope value.<hr>

**[Returns]**

- `last_scope`: LastScope
  - A target last scope.