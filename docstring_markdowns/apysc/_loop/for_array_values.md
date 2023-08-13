# `apysc._loop.for_array_values` docstrings

## Module summary

The loop implementation class for the `ap.Array` values.

## `ForArrayValues` class docstring

The loop implementation class for the `ap.Array` values.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> x_arr: ap.Array[ap.Number] = ap.Array(
...     [ap.Number(75), ap.Number(175), ap.Number(275)]
... )
>>> with ap.ForArrayValues(arr=x_arr, arr_value_type=ap.Number) as value:
...     circle: ap.Circle = ap.Circle(
...         x=value,
...         y=75,
...         radius=25,
...         fill_color=ap.Color("#0af"),
...     )
...
```

<hr>

**[References]**

- [ForArrayValues class](https://simon-ritchie.github.io/apysc/en/for_array_values.html)

### `__enter__` method docstring

The entering method for the beginning of with-statement.<hr>

**[Returns]**

- `arr_value`: _ArrayValue
  - A value of iteration.

### `__init__` method docstring

The loop implementation class for the `ap.Array` values.<hr>

**[Parameters]**

- `arr`: Array[_ArrayValue]
  - An array to iterate.
- `arr_value_type`: Type[_ArrayValue]
  - An array value type. This interface accepts apysc types, such as the `Int`, `String`, `Rectangle`.
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
>>> _ = ap.Stage()
>>> x_arr: ap.Array[ap.Number] = ap.Array(
...     [ap.Number(75), ap.Number(175), ap.Number(275)]
... )
>>> with ap.ForArrayValues(arr=x_arr, arr_value_type=ap.Number) as value:
...     circle: ap.Circle = ap.Circle(
...         x=value,
...         y=75,
...         radius=25,
...         fill_color=ap.Color("#0af"),
...     )
...
```

<hr>

**[References]**

- [ForArrayValues class](https://simon-ritchie.github.io/apysc/en/for_array_values.html)

### `_get_last_scope` method docstring

Get a target last scope value.<hr>

**[Returns]**

- `last_scope`: LastScope
  - A target last scope.