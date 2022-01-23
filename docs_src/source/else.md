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
- [Each branch instruction class scope variables reverting setting](branch_instruction_variables_reverting_setting.md)