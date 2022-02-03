# If

This page explains the `If` class.

Before reading on, maybe it is helpful to read the following page (the apysc uses the `If` class for the same reason of each apysc data type):

- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)

## What is the If class?

The `If` class is the apysc branch instruction class. It behaves like the Python built-in `if` keyword.

## Basic usage

The `If` class requires the `with` statement, as follows:

```py
# runnable
import apysc as ap

condition: ap.Boolean = ap.Boolean(True)
with ap.If(condition):
    ...
```

The `If` class requires passing the `Boolean` value as the condition.

## See also

- [Elif class](elif.md)
- [Else class](else.md)
- [Each branch instruction class's scope variables reverting setting](branch_instruction_variables_reverting_setting.md)


## If constructor API

<!-- Docstring: apysc._branch._if.If.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, condition:Union[apysc._type.boolean.Boolean, NoneType], *, locals_:Union[Dict[str, Any], NoneType]=None, globals_:Union[Dict[str, Any], NoneType]=None) -> None`<hr>

**[Interface summary]** A class to append if branch instruction expression.<hr>

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

- [Each branch instruction class's scope variables reverting setting](https://simon-ritchie.github.io/apysc/branch_instruction_variables_reverting_setting.html)