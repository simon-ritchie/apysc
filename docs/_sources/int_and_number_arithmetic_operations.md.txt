# Int and Number common arithmetic operations

This page will explain the `Int` and `Number` classes common arithmetic operations, like addition, multiplication, or incremental addition.

## Common behaviors

You can calculate the `Int` and `Number` values with the Python built-in values, such as `int` or `float`, as follows:

```py
# runnable
from apysc import Int

int_1: Int = Int(10)
int_1 = int_1 + 20
assert int_1 == 30
```

Also, arithmetic operations with the same types (e.g., `Int` and `Int`) are supported:

```py
# runnable
from apysc import Int

int_1: Int = Int(10)
int_2: Int = Int(20)
int_1 = int_1 + int_2
assert int_1 == 30
```

Arithmetic operations are not supported if the left value is the Python built-in value. For instance, the following code will raise the exception:

```py
from apysc import Int

int_1: Int = Int(10)

# This will raise the error!
int_1 = 20 + int_1
```

```
TypeError: unsupported operand type(s) for +: 'int' and 'Int'
```

## Addition

You can add values with the `+` operator.

```py
# runnable
from apysc import Int

int_1: Int = Int(10)
int_1 = int_1 + 20
assert int_1 == 30
```

```py
# runnable
from apysc import Int

int_1: Int = Int(10)
int_2: Int = Int(20)
int_1 = int_1 + int_2
assert int_1 == 30
```

```py
# runnable
from apysc import Int

int_1: Int = Int(10) + Int(20)
assert int_1 == 30
```

Also, you can use the `+=` operator.

```py
# runnable
from apysc import Int

int_1: Int = Int(10)
int_1 += 20
assert int_1 == 30
```

```py
# runnable
from apysc import Int

int_1: Int = Int(10)
int_2: Int = Int(20)
int_1 += int_2
assert int_1 == 30
```

## Subtraction

You can subtract values with the `-` operator.

```py
# runnable
from apysc import Int

int_1: Int = Int(30)
int_1 = int_1 - 10
assert int_1 == 20
```

```py
# runnable
from apysc import Int

int_1: Int = Int(30)
int_2: Int = Int(20)
int_1 = int_1 - int_2
assert int_1 == 10
```

Also, you can use the `-=` operator.

```py
# runnable
from apysc import Int

int_1: Int = Int(50)
int_1 -= 30
assert int_1 == 20
```

## Multiplication

You can multiply values with the `*` operator.

```py
# runnable
from apysc import Int

int_1: Int = Int(10)
int_1 = int_1 * 3
assert int_1 == 30
```

```py
# runnable
from apysc import Int

int_1: Int = Int(10)
int_2: Int = Int(5)
int_1 = int_1 * int_2
assert int_1 == 50
```

Also, you can use the `*=` operator.

```py
# runnable
from apysc import Int

int_1: Int = Int(10)
int_1 *= 3
assert int_1 == 30
```

## Division

You can divide values with the `/` operator. A return value will be a `Number` value, not an `Int` one.

```py
# runnable
from apysc import Int, Number

int_1: Int = Int(10)
number_1: Number = int_1 / 4
assert number_1 == 2.5
```

```py
# runnable
from apysc import Int, Number

int_1: Int = Int(10)
int_2: Int = Int(4)
number_1: Number = int_1 / int_2
assert number_1 == 2.5
```

Also, you can use the `/=` operator.

```py
# runnable
from apysc import Number

number_1: Number = Number(10)
number_1 /= 4
assert number_1 == 2.5
```

## Floor division

You can divide and floor values with the `//` operator. A return value will be an `Int` value, not a `Number` one.

```py
# runnable
from apysc import Int

int_1: Int = Int(10)
int_1 = int_1 // 4
assert int_1 == 2
```
