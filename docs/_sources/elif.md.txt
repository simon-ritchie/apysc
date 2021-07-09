# Elif

This page will explain the `Elif` class.

Before reading on, maybe it is useful to read the following page (the `Elif` class will be used for the same reason of each apysc data type):

- [Why not using the Python built-in data type in the apysc library?](why_not_using_python_builtin_data_type.md)

## What is the Elif class?

The `Elif` class is the apysc branch instruction class. It will behave like the Python built-in `elif` keyword.

## Basic usage

The `Elif` class will be used at the `with` statement. The `Elif` class statement is only acceptable to implement right after the `If` or `Elif` classes statement.

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

If you insert the code between the `If` (or `Elif`) and `Elif` statements, then exceptions will be raised:

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

Also, the condition (`Boolean` value) can not be created at the `Elif` constructor position (the same goes for the comparison operators), for instance:

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
- [Each branch instruction class scope variables reverting setting](branch_instruction_variables_reverting_setting.md)
