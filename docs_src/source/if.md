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
- [Each branch instruction class scope variables reverting setting](branch_instruction_variables_reverting_setting.md)
