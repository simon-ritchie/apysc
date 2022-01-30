# Int and Number

This page explains the `Int` and `Number` classes.

Before reading on, maybe it is helpful to read the following page:

- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)

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

## Int class constructor API

<!-- Docstring: apysc._type.int.Int.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, value:Union[int, float, apysc._type.number_value_interface.NumberValueInterface]) -> None`<hr>

**[Interface summary]** Integer class for apysc library.<hr>

**[Parameters]**

- `value`: int or float or Int or Number
  - Initial integer value. If the `float` or `Number` value is specified, this class casts it to an integer.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> int_val: ap.Int = ap.Int(10)
>>> int_val
Int(10)

>>> int_val == 10
Boolean(True)

>>> int_val == ap.Int(10)
Boolean(True)

>>> int_val >= 10
Boolean(True)

>>> int_val += 10
>>> int_val
Int(20)

>>> int_val = ap.Int(10.5)
>>> int_val
Int(10)
```

<hr>

**[References]**

- [Int and Number common arithmetic operations document](https://simon-ritchie.github.io/apysc/int_and_number_arithmetic_operations.html)
- [Int and Number common comparison operations document](https://simon-ritchie.github.io/apysc/int_and_number_comparison_operations.html)

## Number class constructor API

<!-- Docstring: apysc._type.number.Number.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, value:Union[int, float, apysc._type.number_value_interface.NumberValueInterface]) -> None`<hr>

**[Interface summary]** Floating point number class for apysc library.<hr>

**[Parameters]**

- `value`: int or float or Int or Number
  - Initial floating point number value. This class casts it to float if you specify int or Int value.

<hr>

**[Notes]**

The `Float` class is the alias of the Number, and it behaves the same as the Number class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> number: ap.Number = ap.Number(10.5)
>>> number
Number(10.5)

>>> number == 10.5
Boolean(True)

>>> number == ap.Number(10.5)
Boolean(True)

>>> number >= 10.5
Boolean(True)

>>> number += 10.3
>>> number
Number(20.8)
```

<hr>

**[References]**

- [Int and Number common arithmetic operations document](https://simon-ritchie.github.io/apysc/int_and_number_arithmetic_operations.html)
- [Int and Number common comparison operations document](https://simon-ritchie.github.io/apysc/int_and_number_comparison_operations.html)

## value property API

<!-- Docstring: apysc._type.number_value_interface.NumberValueInterface.value -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]** Get a current number value.<hr>

**[Returns]**

- `value`: int or float
  - Current number value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> int_val: ap.Int = ap.Int(10)
>>> int_val.value
10

>>> int_val.value = 20
>>> int_val.value
20

>>> int_val.value = ap.Int(30)
>>> int_val.value
30
```

<hr>

**[References]**

- [apysc fundamental data classes value interface](https://simon-ritchie.github.io/apysc/fundamental_data_classes_value_interface.html)