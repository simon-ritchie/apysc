# String class addition and multiplication operations

This page explains the `String` class addition and multiplication operations.

## Addition

The `String` class addition operation (`+`) returns the concatenated `String` value:

```py
# runnable
import apysc as ap

string_1: ap.String = ap.String('Hello')
string_2: ap.String = string_1 + ' World!'
assert string_2 == 'Hello World!'
assert isinstance(string_2, ap.String)
```

Also, the `+=` operator is supported:

```py
# runnable
import apysc as ap

string_1: ap.String = ap.String('Hello')
string_1 += ' World!'
assert string_1 == 'Hello World!'
```

A `String` value + Python built-in `str` operation is supported. Similarly, a `String` value + `String` value operation is also supported:

```py
# runnable
import apysc as ap

string_1: ap.String = ap.String('Hello')
string_2: ap.String = ap.String(' World!')
string_3: ap.String = string_1 + string_2
assert string_3 == 'Hello World!'
```

But a Python built-in `str` + `String` value is not supported; for instance, the following code raises an error:

```py
import apysc as ap

string_1: ap.String = ap.String(' World!')
string_2: ap.String = 'Hello' + string_1
```

```
TypeError: must be str, not String
```

## Multiplication

The `String` class multiplication operation (`*`) returns the repeated `String` value, same behaviors as the Python built-in `str` value:

```py
# runnable
import apysc as ap

string_1: ap.String = ap.String('Hello')
string_2: ap.String = string_1 * 3
assert string_2 == 'HelloHelloHello'
```

The `int` or `Int` values are acceptable at the operation's right-side value:

```py
# runnable
import apysc as ap

string_1: ap.String = ap.String('Hello')
int_1: ap.Int = ap.Int(3)
string_2: ap.String = string_1 * int_1
assert string_2 == 'HelloHelloHello'
```