# If

This page will explain the `If` class.

Before reading on, maybe it is useful to read the following page (the `If` class will be used for the same reason of each apysc data type):

- [Why not using the Python built-in data type in the apysc library?](why_not_using_python_builtin_data_type.md)

## What is the If class?

The `If` class is the apysc branch instruction class. It will behave like the Python built-in `if` keyword. The `If` class will be used at the `with` statement, as follows:

```py
# runnable
from apysc import Boolean
from apysc import If

condition: Boolean = Boolean(True)
with If(condition):
    ...
```

The `If` class need to pass the `Boolean` value as the condition.
