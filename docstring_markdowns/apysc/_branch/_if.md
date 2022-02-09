# apysc._branch._if docstrings

## Module summary

If branch instruction implementations.

## If class docstring

A class to append if branch instruction expression.

A class to append if branch instruction expression.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> int_val: ap.Int = ap.Int(10)
>>> condition: ap.Boolean = int_val >= 10
>>> with ap.If(condition):
...     ap.trace('Int value is greater than equal 10!')
```

<hr>

**[References]**

- [If document](https://simon-ritchie.github.io/apysc/if.html)
- [Each branch instruction class's scope variables reverting setting](https://simon-ritchie.github.io/apysc/branch_instruction_variables_reverting_setting.html)

### __init__ method docstring

A class to append if branch instruction expression.<hr>

**[Parameters]**

- `condition`: Boolean or None
  - Boolean value to be used for judgment.
- `locals_`: dict or None, default None
  - Current scope's local variables. Set locals() value to this argument. If specified, this interface reverts all local scope VariableNameInterface variables (like Int, Sprite) at the end of an `If` scope. This setting is useful when you don't want to update each variable by implementing the `If` scope.
- `globals_`: dict or None, default None
  - Current scope's global variables. Set globals() value to this argument. This setting works the same way as the locals_ argument.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> int_val: ap.Int = ap.Int(10)
>>> condition: ap.Boolean = int_val >= 10
>>> with ap.If(condition):
...     ap.trace('Int value is greater than equal 10!')
```

<hr>

**[References]**

- [If document](https://simon-ritchie.github.io/apysc/if.html)
- [Each branch instruction class's scope variables reverting setting](https://simon-ritchie.github.io/apysc/branch_instruction_variables_reverting_setting.html)

### _append_enter_expression method docstring

Append if branch instruction start expression.

### _set_last_scope method docstring

Set expression last scope value.