# `apysc._loop.for_dict_keys_and_values` docstrings

## Module summary

The loop implementation class for the `ap.Dictionary` keys and values.

## `ForDictKeysAndValues` class docstring

The loop implementation class for the `ap.Dictionary` keys and values.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage(background_color="#333", stage_width=250, stage_height=300)
>>> dict_: ap.Dictionary[ap.Number, ap.Number] = ap.Dictionary(
...     {
...         ap.Number(50): ap.Number(50),
...         ap.Number(100): ap.Number(125),
...         ap.Number(150): ap.Number(200),
...     }
... )
>>> with ap.ForDictKeysAndValues(
...     dict_=dict_,
...     dict_key_type=ap.Number,
...     dict_value_type=ap.Number,
... ) as (key, value):
...     _ = ap.Rectangle(x=key, y=value, width=50, height=50, fill_color="#0af")
```

<hr>

**[References]**

- [ForDictKeysAndValues class](https://simon-ritchie.github.io/apysc/en/for_dict_keys_and_values.html)

### `__enter__` method docstring

The entering method for the beginning of with-statement.<hr>

**[Returns]**

- `dict_key`: _DictKey
  - A dictionary key of iteration.
- `dict_value`: _DictValue
  - A dictionary value of iteration.

### `__init__` method docstring

The loop implementation class for the `ap.Dictionary` keys and values.<hr>

**[Parameters]**

- `dict_`: Dictionary[_DictKey, _DictValue]
  - A dictionary to iterate.
- `dict_key_type`: Type[_DictKey]
  - A dictionary key type. This interface accepts hashable types, such as the `String`, `Int`, `Number`, or `Boolean`.
- `dict_value_type`: Type[_DictValue]
  - A dictionary value type. This interface accepts `InitializeWithBaseValueInterface` subclasses, such as the `Int`, `String`, or `Rectangle`.
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
>>> _ = ap.Stage(background_color="#333", stage_width=250, stage_height=300)
>>> dict_: ap.Dictionary[ap.Number, ap.Number] = ap.Dictionary(
...     {
...         ap.Number(50): ap.Number(50),
...         ap.Number(100): ap.Number(125),
...         ap.Number(150): ap.Number(200),
...     }
... )
>>> with ap.ForDictKeysAndValues(
...     dict_=dict_,
...     dict_key_type=ap.Number,
...     dict_value_type=ap.Number,
... ) as (key, value):
...     _ = ap.Rectangle(x=key, y=value, width=50, height=50, fill_color="#0af")
```

<hr>

**[References]**

- [ForDictKeysAndValues class](https://simon-ritchie.github.io/apysc/en/for_dict_keys_and_values.html)

### `_get_last_scope` method docstring

Get a target last scope value.<hr>

**[Returns]**

- `last_scope`: LastScope
  - A target last scope.