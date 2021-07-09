# apysc basic data classes common value interface

This page will explain the apysc basic data classes (such as the `Int`, `Number`, `String`) common `value` interface.

## What interface is this?

The `value` getter interface will return the value of each data class value. And the setter interface will update these data class values.

A return value of the getter interface will become a Python built-in value, like the `int`, `float`, `str`, `list`.

## Basic usage of the getter interface

The `value` getter interface will return the Python built-in value.

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
value = int_1.value
assert isinstance(value, int)
```

```py
# runnable
import apysc as ap

number_1: ap.Number = ap.Number(10.5)
value = number_1.value
assert isinstance(value, float)
```

## Basic usage of the setter interface

You can update the apysc basic data class values with the `value` setter interface. Python built-in values and the same type value is acceptable:

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
int_1.value = 20
assert int_1 == 20
```

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
int_1.value = ap.Int(20)
assert int_1 == 20
```
