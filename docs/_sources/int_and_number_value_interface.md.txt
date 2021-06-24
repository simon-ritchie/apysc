# Int and Number common value interface

This page will explain the `Int` and `Number` classes common `value` interface.

## What interface is this?

The `value` getter interface will return the numeric value of the `Int` or `Number` values. And the setter interface will update these numeric values.

A return value of the getter interface will become a Python built-in value, like the `int` or `float`.

## Basic usage of the getter interface

The `value` getter interface will return the Python built-in value.

```py
# runnable
from apysc import Int

int_1: Int = Int(10)
value = int_1.value
assert isinstance(value, int)
```

```py
# runnable
from apysc import Number

number_1: Number = Number(10.5)
value = number_1.value
assert isinstance(value, float)
```

## Basic usage of the setter interface

You can update the `Int` and `Number` numeric values with the `value` setter interface. Python built-in values and `Int` or `Number` values are acceptable:

```py
# runnable
from apysc import Int

int_1: Int = Int(10)
int_1.value = 20
assert int_1 == 20
```

```py
# runnable
from apysc import Int

int_1: Int = Int(10)
int_1.value = Int(20)
assert int_1 == 20
```
