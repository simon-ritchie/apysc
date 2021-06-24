# Int and Number common comparison operations

This page will explain the `Int` and `Number` classes common comparison operations, like the `>=`, `<`.

## Common behaviors

Each comparison operation will return a `Boolean` value, not a Python built-in `bool` value:

```py
# runnable
from apysc import Boolean, Int

int_1: Int = Int(10)
result: Boolean = int_1 == 10
assert isinstance(result, Boolean)
```

You can compare the `Int` or `Number` values with the Python built-in values, like the `int` or `float`:

```py
# runnable
from apysc import Boolean, Int

int_1: Int = Int(20)
result: Boolean = int_1 == 20
assert result
```

```py
# runnable
from apysc import Boolean, Number

number_1: Number = Number(10.5)
result: Boolean = number_1 == 10.5
assert result
```

Also, the comparison between the `Int` and `Int`, `Number` and `Number`, `Int` and `Number` are supported:

```py
# runnable
from apysc import Boolean, Int

int_1: Int = Int(10)
int_2: Int = Int(10)
result: Boolean = int_1 == int_2
assert result
```

```py
# runnable
from apysc import Boolean, Number

number_1: Number = Number(10.5)
number_2: Number = Number(10.5)
result: Boolean = number_1 == number_2
assert result
```

```py
# runnable
from apysc import Boolean, Int, Number

int_1: Int = Int(10)
number_1: Number = Number(10)
result: Boolean = int_1 == number_1
assert result
```

## Equal comparison operator

You can use the `==` operator for the equal comparison:

```py
# runnable
from apysc import Boolean, Int

int_1: Int = Int(10)
result: Boolean = int_1 == 10
assert result
```

## Not equal comparison operator

You can use the `!=` operator for the not equal comparison:

```py
# runnable
from apysc import Boolean, Int

int_1: Int = Int(10)
result: Boolean = int_1 != 15
assert result
```

## Less than comparison operator

You can use the `<` operator for the less than comparison:

```py
# runnable
from apysc import Boolean, Int

int_1: Int = Int(10)
result: Boolean = int_1 < 11
assert result
```

## Less than or equal comparison operator

You can use the `<=` operator for the less than or equal comparison:

```py
# runnable
from apysc import Boolean, Int

int_1: Int = Int(10)
result: Boolean = int_1 <= 10
assert result
```

## Greater than comparison operator

You can use the `>` operator for the greater than comparison:

```py
# runnable
from apysc import Boolean, Int

int_1: Int = Int(10)
result: Boolean = int_1 > 9
assert result
```

## Greater than or equal comparison operator

You can use the `>=` operator for the greater than or equal comparison:

```py
# runnable
from apysc import Boolean, Int

int_1: Int = Int(10)
result: Boolean = int_1 >= 10
assert result
```
