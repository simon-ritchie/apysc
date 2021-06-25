# Int and Number

This page will explain the `Int` and `Number` classes.

Before reading on, maybe it is useful to read the following page:

- [Why not using the Python built-in data type in the apysc library?](why_not_using_python_builtin_data_type.md)

## Int class

The `Int` class is the apysc integer type. It can accept numeric values at the constructor, as follows:

```py
# runnable
from apysc import Int

int_1: Int = Int(10)
assert int_1 == 10
```

```py
# runnable
from apysc import Int

int_1: Int = Int(10)
int_2: Int = Int(int_1)
```

```py
# runnable
from apysc import Int

int_1: Int = Int(10)
int_2: Int = Int(int_1)
int_2 += 15
assert int_2 == 25
```

If you specify a float value to the constructor argument, then a value will be floored:

```py
# runnable
from apysc import Int

int_1: Int = Int(10.5)
assert int_1 == 10
```

## Number class

The ``Number`` class is the apysc float type. It can accept numeric values at the constructor, same as `Int`:

```py
# runnable
from apysc import Number

number_1: Number = Number(10.5)
assert number_1 == 10.5

number_2: Number = Number(number_1)
number_2 += 10.5
assert number_2 == 21
```

## Int and Number classes common interfaces

The `Int` and `Number` classes have the same interfaces. For more details, please see:

- [Int and Number classes common arithmetic operations](int_and_number_arithmetic_operations.md)
- [Int and Number classes common comparison operations](int_and_number_comparison_operations.md)
- [apysc basic data classes common value interface](basic_data_classes_value_interface.md)
