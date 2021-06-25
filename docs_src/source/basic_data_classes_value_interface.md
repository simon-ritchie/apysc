# apysc basic data classes common value interface

This page will explain the apysc basic data classes (such as the `Int`, `Number`, `String`) common `value` interface.

## What interface is this?

The `value` getter interface will return the value of each data class value. And the setter interface will update these data class values.

A return value of the getter interface will become a Python built-in value, like the `int`, `float`, `str`, `list`.

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

You can update the apysc basic data class values with the `value` setter interface. Python built-in values and the same type value is acceptable:

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
