# Boolean

This page explains the `Boolean` class.

Before reading on, maybe it is helpful to read the following page:

- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)

## What is the Boolean class?

The `Boolean` class is the apysc boolean class. It can accept `bool` or `Boolean` values at the constructor, as follows:

```py
# runnable
import apysc as ap

bool_1: ap.Boolean = ap.Boolean(True)
assert bool_1

bool_2: ap.Boolean = ap.Boolean(False)
assert not bool_2

bool_3: ap.Boolean = ap.Boolean(bool_1)
assert bool_3
```

## Boolean comparison

The `Boolean` comparison interface behaves like the Python built-in `bool` value.

You can compare it with the equal comparison operator (`=`), and the `Boolean`\, `bool`\, `int`\, `Int` types are acceptable, as follows:

```py
# runnable
import apysc as ap

bool_1: ap.Boolean = ap.Boolean(True)
assert bool_1 == True  # noqa
assert bool_1 == ap.Boolean(True)
assert bool_1 == 1
assert bool_1 == ap.Int(1)
```

Also, the not equal comparison operator (`!=`) is supported, as follows:

```py
# runnable
import apysc as ap

bool_1: ap.Boolean = ap.Boolean(True)
assert bool_1 != False  # noqa
assert bool_1 != ap.Boolean(False)
assert bool_1 != 0
assert bool_1 != ap.Int(0)
```

You can skip the comparison operator, as follows:

```py
# runnable
import apysc as ap

bool_1: ap.Boolean = ap.Boolean(True)
assert bool_1

bool_2: ap.Boolean = ap.Boolean(False)
assert not bool_2
```

## Reverse a Boolean value

The `not_` property returns the reversed `Boolean` value:

```py
# runnable
import apysc as ap

bool_1: ap.Boolean = ap.Boolean(True)
bool_2: ap.Boolean = bool_1.not_
assert not bool_2

bool_3: ap.Boolean = bool_2.not_
assert bool_3
```
