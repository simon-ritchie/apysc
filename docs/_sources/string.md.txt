# String

This page will explain the `String` class.

Before reading on, maybe it is useful to read the following page:

- [Why not using the Python built-in data type in the apysc library?](why_not_using_python_builtin_data_type.md)

## What is the String class?

The `String` class is the apysc string class. It can accept `str` or `String` values at the constructor, as follows:

```py
# runnable
from apysc import String

string_1: String = String('Hello')
assert string_1 == 'Hello'

string_2: String = String(string_1)
assert string_2 == 'Hello'
```

## String class interfaces

For more details about the `String` class each interface, please see the following:

- [String class comparison operations](string_comparison_operations.md)
- [String class addition and multiplication operations](string_addition_and_multiplication.md)
