# `apysc._loop.for_array_indices` docstrings

## Module summary

The loop implementation class for the `ap.Array` indices.

## `ForArrayIndices` class docstring

The loop implementation class for the `ap.Array` indices.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array[ap.Number] = ap.Array(
...     [ap.Number(50), ap.Number(150), ap.Number(250)]
... )
>>> indices: ap.Array[ap.Int] = ap.Array([])
>>> with ap.ForArrayIndices(arr=arr) as i:
...     indices.append(i)
...
>>> _ = ap.assert_arrays_equal(indices, [0, 1, 2])
```

<hr>

**[References]**

- [ForArrayIndices class](https://simon-ritchie.github.io/apysc/en/for_array_indices.html)
- [Why the apysc library doesn’t use the Python built-in data type](https://simon-ritchie.github.io/apysc/en/why_apysc_doesnt_use_python_builtin_data_type.html)
- [Each branch instruction class’s scope variable reverting setting](https://simon-ritchie.github.io/apysc/en/branch_instruction_variables_reverting_setting.html)

### `__enter__` method docstring

The entering method for the beginning of with-statement.<hr>

**[Returns]**

- `i`: Int
  - An index of iteration.

### `__init__` method docstring

The loop implementation class for the `ap.Array` indices.<hr>

**[Parameters]**

- `arr`: Array
  - An array to iterate.
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
>>> arr: ap.Array[ap.Number] = ap.Array(
...     [ap.Number(50), ap.Number(150), ap.Number(250)]
... )
>>> indices: ap.Array[ap.Int] = ap.Array([])
>>> with ap.ForArrayIndices(arr=arr) as i:
...     indices.append(i)
...
>>> _ = ap.assert_arrays_equal(indices, [0, 1, 2])
```

<hr>

**[References]**

- [ForArrayIndices class](https://simon-ritchie.github.io/apysc/en/for_array_indices.html)
- [Why the apysc library doesn’t use the Python built-in data type](https://simon-ritchie.github.io/apysc/en/why_apysc_doesnt_use_python_builtin_data_type.html)
- [Each branch instruction class’s scope variable reverting setting](https://simon-ritchie.github.io/apysc/en/branch_instruction_variables_reverting_setting.html)

### `_append_enter_expression` method docstring

Append a for-loop start expression.<hr>

**[Parameters]**

- `i`: Int
  - Loop index value.

### `_get_last_scope` method docstring

Get a target last scope value.<hr>

**[Returns]**

- `last_scope`: LastScope
  - A target last scope.