# Elif

This page explains the `Elif` class.

Before reading on, maybe it is helpful to read the following page (the apysc uses the `Elif` class for the same reason of each other data type):

- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)

## What is the Elif class?

The `Elif` class is the apysc branch instruction class. It behaves like the Python built-in `elif` keyword.

## Basic usage

The `Elif` class requires using the `with` statement. Also, The `Elif` class statement is only acceptable to implement right after the `If` or `Elif` classes statement.

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)

condition_1: ap.Boolean = ap.Boolean(False)
condition_2: ap.Boolean = ap.Boolean(True)
with ap.If(condition_1):
    int_1 += 20
with ap.Elif(condition_2):
    int_1 += 30
```

## Notes

If you insert the code between the `If` (or `Elif`) and `Elif` statements, then it raises exceptions:

```py
import apysc as ap

int_1: ap.Int = ap.Int(10)

condition_1: ap.Boolean = ap.Boolean(False)
condition_2: ap.Boolean = ap.Boolean(True)
with ap.If(condition_1):
    int_1 += 20
# Code inserting between the `If` and `Elif` will raise an exception.
int_2: ap.Int = ap.Int(30)
with ap.Elif(condition_2):
    int_1 += 30
```

```
ValueError: Elif interface can only use right after If or Elif interfaces.
```

Also, you can't create the condition (`Boolean` value) at the `Elif` constructor position (the same goes for the comparison operators), for instance:

```py
import apysc as ap

int_1: ap.Int = ap.Int(10)

condition_1: ap.Boolean = ap.Boolean(False)
condition_2: ap.Boolean = ap.Boolean(True)
with ap.If(condition_1):
    int_1 += 20
with ap.Elif(int_1 == 10):
    int_1 += 30
```

```
ValueError: Elif interface can only use right after If or Elif interfaces.

Maybe you are using Int or String, or anything else comparison expression at Elif constructor (e.g., `with Elif(any_value == 10, ...):`).
Currently, that specifying expression directly is not supported so please define condition separately as follows:
condition: Boolean = any_value == 10
...
with Elif(condition, ....):
```

## See also

- [If class](if.md)
- [Else class](else.md)
- [Each branch instruction class's scope variables reverting setting](branch_instruction_variables_reverting_setting.md)


## Elif constructor API

<!-- Docstring: apysc._branch._elif.Elif.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, condition:Union[apysc._type.boolean.Boolean, NoneType], *, locals_:Union[Dict[str, Any], NoneType]=None, globals_:Union[Dict[str, Any], NoneType]=None) -> None`<hr>

**[Interface summary]** A class to append the `else if` branch instruction expression.<hr>

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

- [Each branch instruction class's scope variables reverting setting](https://simon-ritchie.github.io/apysc/branch_instruction_variables_reverting_setting.html)