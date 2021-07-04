# Boolean

This page will explain the `Boolean` class.

Before reading on, maybe it is useful to read the following page:

- [Why not using the Python built-in data type in the apysc library?](why_not_using_python_builtin_data_type.md)

## What is the Boolean class?

The `Boolean` class is the apysc boolean class. It can accept `bool` or `Boolean` values at the constructor, as follows:

```py
# runnable
from apysc import Boolean

bool_1: Boolean = Boolean(True)
assert bool_1

bool_2: Boolean = Boolean(False)
assert not bool_2

bool_3: Boolean = Boolean(bool_1)
assert bool_3
```

## Boolean comparison

The `Boolean` comparison interface will behave like the Python built-in `bool` value.

You can compare it with the equal comparison operator (`=`), and the `Boolean`, `bool`, `int`, `Int` types are acceptable, as follows:

```py
# runnable
from apysc import Boolean, Int

bool_1: Boolean = Boolean(True)
assert bool_1 == True
assert bool_1 == Boolean(True)
assert bool_1 == 1
assert bool_1 == Int(1)
```

Also, the not equal comparison operator (`!=`) is supported, as follows:

```py
# runnable
from apysc import Boolean, Int

bool_1: Boolean = Boolean(True)
assert bool_1 != False
assert bool_1 != Boolean(False)
assert bool_1 != 0
assert bool_1 != Int(0)
```

You can skip the comparison operator, as follows:

```py
# runnable
from apysc import Boolean

bool_1: Boolean = Boolean(True)
assert bool_1

bool_2: Boolean = Boolean(False)
assert not bool_2
```

## Reverse a Boolean value

The `not_` property will return the reversed `Boolean` value:

```py
# runnable
from apysc import Boolean

bool_1: Boolean = Boolean(True)
bool_2: Boolean = bool_1.not_
assert not bool_2

bool_3: Boolean = bool_2.not_
assert bool_3
```
