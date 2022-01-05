# Int and Number

This page explains the `Int` and `Number` classes.

Before reading on, maybe it is helpful to read the following page:

- [Why not using the Python built-in data type in the apysc library?](why_not_using_python_builtin_data_type.md)

## Int class

The `Int` class is the apysc integer type. It can accept numeric values at the constructor, as follows:

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
assert int_1 == 10
```

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
int_2: ap.Int = ap.Int(int_1)
```

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
int_2: ap.Int = ap.Int(int_1)
int_2 += 15
assert int_2 == 25
```

If you specify a float value to the constructor argument, then the `Int` class floor a value:

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10.5)
assert int_1 == 10
```

## Number class

The ``Number`` class is the apysc float type. It can accept numeric values at the constructor, same as `Int`:

```py
# runnable
import apysc as ap

number_1: ap.Number = ap.Number(10.5)
assert number_1 == 10.5

number_2: ap.Number = ap.Number(number_1)
number_2 += 10.5
assert number_2 == 21
```

## Note for the Float class alias

The `Float` class is the alias of the `Number` class. It behaves the same as the `Number` class. Maybe a Python developer is familiar with its name rather than the `Number`\. On the other hand, the `Number` is more common in JavaScript than the `Number`\.

```py
# runnable
import apysc as ap

assert ap.Number == ap.Float
assert ap.Number(10.5) == ap.Float(10.5)
```

## Int and Number classes basic interfaces

The `Int` and `Number` classes have the same interfaces. For more details, please see:

- [Int and Number classes basic arithmetic operations](int_and_number_arithmetic_operations.md)
- [Int and Number classes basic comparison operations](int_and_number_comparison_operations.md)
- [Funcdamental data classes common value interface](fundamental_data_classes_value_interface.md)
