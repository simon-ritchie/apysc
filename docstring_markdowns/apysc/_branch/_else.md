# `apysc._branch._else` docstrings

## Module summary

Else branch instruction implementation.

## `Else` class docstring

A class to append else branch instruction expression.<hr>

**[Notes]**

 ・You can only use this class immediately after the `If` or `Elif` statement.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> int_val: ap.Int = ap.Int(10)
>>> with ap.If(int_val >= 11):
...     ap.trace('Value is greater than equal 11.')
>>> with ap.Else():
...     ap.trace('Value is less than 11.')
```

<hr>

**[References]**

- [Else document](https://simon-ritchie.github.io/apysc/else.html)
- [Each branch instruction class's scope variables reverting setting](https://simon-ritchie.github.io/apysc/branch_instruction_variables_reverting_setting.html)

### `__init__` method docstring

A class to append else branch instruction expression.<hr>

**[Parameters]**

- `locals_`: dict or None, default None
  - Current scope's local variables. Set locals() value to this argument. If specified, this interface reverts all local scope VariableNameInterface variables (like Int, Sprite) at the end of an `Else` scope. This setting is useful when you don't want to update each variable by implementing the `Else` scope.
- `globals_`: dict or None, default None
  - Current scope's global variables. Set globals() value to this argument. This setting works the same way as the locals_ argument.

<hr>

**[Notes]**

 ・You can only use this class immediately after the `If` or `Elif` statement.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> int_val: ap.Int = ap.Int(10)
>>> with ap.If(int_val >= 11):
...     ap.trace('Value is greater than equal 11.')
>>> with ap.Else():
...     ap.trace('Value is less than 11.')
```

<hr>

**[References]**

- [Else document](https://simon-ritchie.github.io/apysc/else.html)
- [Each branch instruction class's scope variables reverting setting](https://simon-ritchie.github.io/apysc/branch_instruction_variables_reverting_setting.html)

### `_append_enter_expression` method docstring

Append else branch instruction start expression.<hr>

**[Raises]**

- ValueError: If the last scope is not If or Elif.

### `_set_last_scope` method docstring

Set expression last scope value.