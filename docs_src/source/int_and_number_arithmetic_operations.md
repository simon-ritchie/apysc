# Int and Number basic arithmetic operations

This page explains basic arithmetic operations of the `Int` and `Number` classes, like addition, multiplication, or incremental addition.

## Common behaviors

You can calculate the `Int` and `Number` values with the Python built-in values, such as `int` or `float`\, as follows:

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
int_1 = int_1 + 20
assert int_1 == 30
```

Also, arithmetic operations with the same types (e.g., `Int` and `Int`) are supported:

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
int_2: ap.Int = ap.Int(20)
int_1 = int_1 + int_2
assert int_1 == 30
```

Arithmetic operations are not supported if the left value is the Python built-in value. For instance, the following code raises an exception:

```py
import apysc as ap

int_1: ap.Int = ap.Int(10)

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
import apysc as ap

int_1: ap.Int = ap.Int(10)
int_1 = int_1 + 20
assert int_1 == 30
```

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
int_2: ap.Int = ap.Int(20)
int_1 = int_1 + int_2
assert int_1 == 30
```

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10) + ap.Int(20)
assert int_1 == 30
```

Also, you can use the `+=` operator.

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
int_1 += 20
assert int_1 == 30
```

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
int_2: ap.Int = ap.Int(20)
int_1 += int_2
assert int_1 == 30
```

## Subtraction

You can subtract values with the `-` operator.

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(30)
int_1 = int_1 - 10
assert int_1 == 20
```

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(30)
int_2: ap.Int = ap.Int(20)
int_1 = int_1 - int_2
assert int_1 == 10
```

Also, you can use the `-=` operator.

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(50)
int_1 -= 30
assert int_1 == 20
```

## Multiplication

You can multiply values with the `*` operator.

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
int_1 = int_1 * 3
assert int_1 == 30
```

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
int_2: ap.Int = ap.Int(5)
int_1 = int_1 * int_2
assert int_1 == 50
```

Also, you can use the `*=` operator.

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
int_1 *= 3
assert int_1 == 30
```

## Division

You can divide values with the `/` operator. A return value becomes a `Number` value, not an `Int`\.

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
number_1: ap.Number = int_1 / 4
assert number_1 == 2.5
```

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
int_2: ap.Int = ap.Int(4)
number_1: ap.Number = int_1 / int_2
assert number_1 == 2.5
```

Also, you can use the `/=` operator.

```py
# runnable
import apysc as ap

number_1: ap.Number = ap.Number(10)
number_1 /= 4
assert number_1 == 2.5
```

## Floor division

You can divide and floor values with the `//` operator. A return value becomes an `Int` value, not a `Number`\.

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
int_1 = int_1 // 4
assert int_1 == 2
```

## Modulo

You can use the modulo operation with the `%` operator.

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
int_2: int = int_1 % 3
assert int_2 == 1
```

```py
# runnable
import apysc as ap

number_1: ap.Number = ap.Number(10.5)
number_2: ap.Number = number_1 % 3
assert number_2 == 1.5
```
