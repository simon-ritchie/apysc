# `apysc._branch._elif` docstrings

## Module summary

Elif (else if) branch instruction implementations.

## `Elif` class docstring

A class to append the `else if` branch instruction expression.<hr>

**[Notes]**

 ・Currently the apysc can not initialize condition value in the constructor. For example, the following raises an exception: <br> ・You can only use this class immediately after the `If` or `Elif` statement.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> any_value: ap.Int = ap.Int(10)
>>> condition_1: ap.Boolean = any_value >= 10
>>> condition_2: ap.Boolean = any_value >= 5
>>> with ap.If(condition_1):
...     # Do something here
...     pass
>>> with ap.Elif(condition_2):
...     # Do something else here
...     pass
```

<hr>

**[References]**

- [Elif document](https://simon-ritchie.github.io/apysc/elif.html)
- [Each branch instruction class's scope variables reverting setting](https://simon-ritchie.github.io/apysc/branch_instruction_variables_reverting_setting.html)

### `__init__` method docstring

A class to append the `else if` branch instruction expression.<hr>

**[Parameters]**

- `condition`: Boolean or None
  - Boolean value to be used for judgment.
- `locals_`: dict or None, default None
  - Current scope's local variables. Set locals() value to this argument. If specified, this interface reverts all local scope VariableNameInterface variables (like Int, Sprite) at the end of an `Elif` scope. This setting is useful when you don't want to update each variable by implementing the `Elif` scope.
- `globals_`: dict or None, default None
  - Current scope's global variables. Set globals() value to this argument. This setting works the same way as the locals_ argument.

<hr>

**[Notes]**

 ・Currently the apysc can not initialize condition value in the constructor. For example, the following raises exception: <br> ・You can only use this class immediately after the `If` or `Elif` statement. ```py import apysc as ap with ap.Elif(any_value >= 10): ... ``` You can avoid this exception by predefining condition value, as follows: >>> import apysc as ap >>> any_value: ap.Int = ap.Int(10) >>> condition_1: ap.Boolean = any_value >= 10 >>> condition_2: ap.Boolean = any_value >= 5 >>> with ap.If(condition_1): ... # Do something here ... pass >>> with ap.Elif(condition_2): ... # Do something else here ... pass<hr>

**[References]**

- [Elif document](https://simon-ritchie.github.io/apysc/elif.html)
- [Each branch instruction class's scope variables reverting setting](https://simon-ritchie.github.io/apysc/branch_instruction_variables_reverting_setting.html)

### `_append_enter_expression` method docstring

Append else if branch instruction starting expression.<hr>

**[Raises]**

- ValueError: If the last scope is not If or Elif.

### `_set_last_scope` method docstring

Set expression last scope value.