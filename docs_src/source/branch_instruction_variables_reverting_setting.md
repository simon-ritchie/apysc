# Each branch instruction class's scope variable reverting setting

This page explains each branch instruction class (like the `If`\, `Elif`\, and `Else`) scope variables reverting setting.

## These interfaces execute With statement code

These interfaces execute the code in each branch instruction regardless of the condition, and variables are updated.

For example, the following code of the condition is `False`\, but the value of int is 20 on the Python:

```py
# runnable
import apysc as ap

condition: ap.Boolean = ap.Boolean(False)
int_1: ap.Int = ap.Int(10)

with ap.If(condition):
    int_1 += 10
assert int_1 == 20
```

This condition is skipped in JavaScript (converted code) since the condition is not satisfied.

## Scope variables reverting setting

The `If`, `Elif`, and `Else` classes have the arguments of the `locals_` and `globals_` (basically set the `locals()` and `globals` built-in functions return value). If these arguments are specified, the scope variables are reverted when ended each scope (e.g., `If` scope).

This interface is occasionally helpful when you don't want to update the variables in each branch instruction scope.

```py
# runnable
import apysc as ap

condition: ap.Boolean = ap.Boolean(False)
int_1: ap.Int = ap.Int(10)

with ap.If(condition, locals_=locals(), globals_=globals()):
    int_1 += 10
assert int_1 == 10
```

## See also

- [If class](if.md)
- [Elif class](elif.md)
- [Else class](else.md)