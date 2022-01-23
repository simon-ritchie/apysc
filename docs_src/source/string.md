# String

This page explains the `String` class.

Before reading on, maybe it is helpful to read the following page:

- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)

## What is the String class?

The `String` class is the apysc string class. It can accept `str` or `String` values at the constructor, as follows:

```py
# runnable
import apysc as ap

string_1: ap.String = ap.String('Hello')
assert string_1 == 'Hello'

string_2: ap.String = ap.String(string_1)
assert string_2 == 'Hello'
```

## String class interfaces

For more details about the `String` class each interface, please see the following:

- [String class comparison operations](string_comparison_operations.md)
- [String class addition and multiplication operations](string_addition_and_multiplication.md)