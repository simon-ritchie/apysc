# apysc fundamental data classes value interface

This page explains the apysc fundamental data classes (such as the `Int`\, `Number`\, `String`) `value` interface.

## What interface is this?

The `value` getter interface returns each data class value. And the setter interface updates these data class values.

A return value of the getter interface becomes a Python built-in value, like the `int`\, `float`\, `str`\, `list`\.

## Basic usage of the getter interface

The `value` getter interface returns the Python built-in value.

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

You can update the apysc fundamental data class values with the `value` setter interface. Python built-in values and the same type value is acceptable:

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