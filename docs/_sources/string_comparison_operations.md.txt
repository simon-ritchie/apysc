# String class comparison operations

This page will explain the `String` class comparison operations, like the `=`, `>=`.

## Comparison return value type

Each `String` class comparison operation will return a `Boolean` value, not a Python built-in `bool` value.

```py
# runnable
import apysc as ap

string_1: ap.String = ap.String('Hello')
result: ap.Boolean = string_1 == 'Hello'
assert result
assert isinstance(result, ap.Boolean)
```

## Acceptable comparison right-side value types

The `str` or `String` types of comparison other value (comparison right-side value) types are acceptable, for instance:

```py
# runnable
import apysc as ap

string_1: ap.String = ap.String('Hello')
result: ap.Boolean = string_1 == 'Hello'
assert result
```

```py
# runnable
import apysc as ap

string_1: ap.String = ap.String('Hello')
string_2: ap.String = ap.String('Hello')
result: ap.Boolean = string_1 == string_2
assert result
```

## Equal comparison

You can use the `==` operator for the equal comparison:

```py
# runnable
import apysc as ap

string_1: ap.String = ap.String('Hello')
result: ap.Boolean = string_1 == 'Hello'
assert result
```

## Not equal comparison

You can use the `!=` operator for the not equal comparison:

```py
# runnable
import apysc as ap

string_1: ap.String = ap.String('Hello')
result: ap.Boolean = string_1 != 'World'
assert result
```

## Less than or greater than comparison

You can use each less than, less than or equal, greater than, greater than or equal comparison, with the `<`, `<=`, `>`, `>=` operators, like the Python built-in `str` value. Sometimes these operations are useful to compare with the date (or date-time) string.

```py
# runnable
import apysc as ap

string_1: ap.String = ap.String('1970-01-05')
result: ap.Boolean = string_1 < '1970-01-06'
assert result
```

```py
# runnable
import apysc as ap

string_1: ap.String = ap.String('1970-01-05')
result: ap.Boolean = string_1 <= '1970-01-05'
assert result
```

```py
# runnable
import apysc as ap

string_1: ap.String = ap.String('1970-01-05')
result: ap.Boolean = string_1 > '1970-01-04'
assert result
```

```py
# runnable
import apysc as ap

string_1: ap.String = ap.String('1970-01-05')
result: ap.Boolean = string_1 >= '1970-01-05'
assert result
```
