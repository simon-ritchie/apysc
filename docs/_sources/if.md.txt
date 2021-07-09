# If

This page will explain the `If` class.

Before reading on, maybe it is useful to read the following page (the `If` class will be used for the same reason of each apysc data type):

- [Why not using the Python built-in data type in the apysc library?](why_not_using_python_builtin_data_type.md)

## What is the If class?

The `If` class is the apysc branch instruction class. It will behave like the Python built-in `if` keyword.

## Basic usage

The `If` class will be used at the `with` statement, as follows:

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
- [Each branch instruction class scope variables reverting setting](branch_instruction_variables_reverting_setting.md)
