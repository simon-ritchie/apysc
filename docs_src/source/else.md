# Else

This page explains the `Else` class.

Before reading on, maybe it is helpful to read the following page (the apysc uses the `Else` class for the same reason of each apysc data type):

- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)

## What is the Else class?

The `Else` class is the apysc branch instruction class. It behaves like the Python built-in `else` keyword.

## Basic usage

The `Else` requires using the `with` statement. The `Else` class statement is only acceptable to implement right after the `If` or `Elif` classes statement.

```py
# runnable
import apysc as ap

condition: ap.Boolean = ap.Boolean(False)
int_1: ap.Int = ap.Int(10)

with ap.If(condition):
    int_1 += 10
with ap.Else():
    int_1 += 20
```

## Notes

if you insert the code between the `If` (or `Elif`) and `Else` statements, it raises an exception:

```py
import apysc as ap

condition: ap.Boolean = ap.Boolean(False)
int_1: ap.Int = ap.Int(10)

with ap.If(condition):
    int_1 += 10
# If there is a code implementation between the `If` and `Else`, then
# exceptions will be raised.
int_2: ap.Int = ap.Int(20)
with ap.Else():
    int_1 += 20
```

```
ValueError: Else interface can only use right after If or Elif interfaces.
```

## See also

- [If class](if.md)
- [Elif class](elif.md)
- [Each branch instruction class's scope variables reverting setting](branch_instruction_variables_reverting_setting.md)


## Else API

<!-- Docstring: apysc._branch._else.Else.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, *, locals_:Union[Dict[str, Any], NoneType]=None, globals_:Union[Dict[str, Any], NoneType]=None) -> None`<hr>

**[Interface summary]** A class to append else branch instruction expression.<hr>

**[Parameters]**

- `locals_`: dict or None, default None
  - Current scope's local variables. Set locals() value to this argument. If specified, this interface reverts all local scope VariableNameInterface variables (like Int, Sprite) at the end of an `If` scope. This setting is useful when you don't want to update each variable by implementing the `If` scope.
- `globals_`: dict or None, default None
  - Current scope's global variables. Set globals() value to this argument. This setting works the same way as the locals_ argument.

<hr>

**[Notes]**

- You can only use this class immediately after the `If` or `Elif` statement.<hr>

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

- [Each branch instruction class's scope variables reverting setting](https://simon-ritchie.github.io/apysc/branch_instruction_variables_reverting_setting.html)