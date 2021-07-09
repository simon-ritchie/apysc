# Each branch instruction class scope variables reverting setting

This page will explain each branch instruction class (like the `If`, `Elif`, and `Else`) scope variables reverting setting.

## With statement code will be executed

Regardless of the condition, the code in each branch instruction will be executed and variables will be updated.

For example, the following code of the condition is the `False` but the value of int will be 20 on the Python:

```py
# runnable
import apysc as ap

condition: ap.Boolean = ap.Boolean(False)
int_1: ap.Int = ap.Int(10)

with ap.If(condition):
    int_1 += 10
assert int_1 == 20
```

In JavaScript (converted code), this condition will be skipped since the condition is not satisfied.

## Scope variables reverting setting

The `If`, `Elif`, and `Else` classes have the arguments of the `locals_` and `globals_` (basically set the `locals()` and `globals` built-in functions return value). If these arguments are specified, then the scope variables will be reverted when each scope (e.g, `If` scope) is ended.

This is occasionally useful when you don't want to update the variables in each branch instruction scope.

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
