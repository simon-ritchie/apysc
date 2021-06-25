# String class comparison operations

This page will explain the `String` class comparison operations, like the `=`, `>=`.

## Comparison return value type

Each `String` class comparison operations will return a `Boolean` value, not a Python built-in `bool` value.

```py
# runnable
from apysc import String, Boolean

string_1: String = String('Hello')
result: Boolean = string_1 == 'Hello'
assert result
assert isinstance(result, Boolean)
```

## Acceptable comparison other value types

The `str` or `String` types of a comparison other value (comparison right-side value) types are acceptable, for instance:

```py
# runnable
from apysc import String, Boolean

string_1: String = String('Hello')
result: Boolean = string_1 == 'Hello'
assert result
```

```py
# runnable
from apysc import String, Boolean

string_1: String = String('Hello')
string_2: String = String('Hello')
result: Boolean = string_1 == string_2
assert result
```

## Equal comparison

You can use the `==` operator for the equal comparison:

```py
# runnable
from apysc import String, Boolean

string_1: String = String('Hello')
result: Boolean = string_1 == 'Hello'
assert result
```

## Not equal comparison

You can use the `!=` operator for the not equal comparison:

```py
# runnable
from apysc import String, Boolean

string_1: String = String('Hello')
result: Boolean = string_1 != 'World'
assert result
```

## Less than or greater than comparison

You can use each less than, less than or equal, greater than, greater than or equal comparison, with the `<`, `<=`, `>`, `>=` operators, like the Python built-in `str` value. Sometimes these operations are useful to compare date (or datetime) string.

```py
# runnable
from apysc import String, Boolean

string_1: String = String('1970-01-05')
result: Boolean = string_1 < '1970-01-06'
assert result
```

```py
# runnable
from apysc import String, Boolean

string_1: String = String('1970-01-05')
result: Boolean = string_1 <= '1970-01-05'
assert result
```

```py
# runnable
from apysc import String, Boolean

string_1: String = String('1970-01-05')
result: Boolean = string_1 > '1970-01-04'
assert result
```

```py
# runnable
from apysc import String, Boolean

string_1: String = String('1970-01-05')
result: Boolean = string_1 >= '1970-01-05'
assert result
```
