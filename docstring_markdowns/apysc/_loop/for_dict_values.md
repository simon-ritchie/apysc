# `apysc._loop.for_dict_values` docstrings

## Module summary

The loop implementation class for the `ap.Dictionary` values.

## `ForDictValues` class docstring

The loop implementation class for the `ap.Dictionary` values.<hr>

**[References]**

- [ForDictValues class](https://simon-ritchie.github.io/apysc/en/for_dict_values.html)

### `__enter__` method docstring

The entering method for the beginning of with-statement.<hr>

**[Returns]**

- `dict_value`: _DictValue
  - A dictionary value of iteration.

### `__init__` method docstring

The loop implementation class for the `ap.Dictionary` values.<hr>

**[Parameters]**

- `dict_`: Dictionary[Any, _DictValue]
  - A dictionary to iterate.
- `dict_value_type`: Type[_DictValue]
  - A dictionary value type. This interface accepts `InitializeWithBaseValueInterface` subclasses, such as the `Int`, `String`, or `Rectangle`.
- `locals_`: Optional[Dict[str, Any]], optional
  - Current scope's local variables. Set locals() value to this argument. If specified, this interface reverts all local scope VariableNameMixIn variables (like Int, Sprite) at the end of a with-statement scope. This setting is useful when you don't want to update each variable.
- `globals_`: Optional[Dict[str, Any]], optional
  - Current scope's global variables. Set globals() value to this argument. This setting works the same way as the locals_ argument.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[References]**

- [ForDictValues class](https://simon-ritchie.github.io/apysc/en/for_dict_values.html)

### `_get_last_scope` method docstring

Get a target last scope value.<hr>

**[Returns]**

- `last_scope`: LastScope
  - A target last scope.