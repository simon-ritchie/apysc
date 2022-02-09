# apysc._type.number docstrings

## Module summary

Class implementation of floating point number.

## Number class docstring

Floating point number class for the apysc library.<hr>

**[Notes]**

Float class is the alias of the Number, and it behaves the same as the Number class.<hr>

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

- [Int and Number document](https://simon-ritchie.github.io/apysc/int_and_number.html)
- [Int and Number common arithmetic operations document](https://simon-ritchie.github.io/apysc/int_and_number_arithmetic_operations.html)
- [Int and Number common comparison operations document](https://simon-ritchie.github.io/apysc/int_and_number_comparison_operations.html)

### __init__ method docstring

Floating point number class for apysc library.<hr>

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

- [Int and Number document](https://simon-ritchie.github.io/apysc/int_and_number.html)
- [Int and Number common arithmetic operations document](https://simon-ritchie.github.io/apysc/int_and_number_arithmetic_operations.html)
- [Int and Number common comparison operations document](https://simon-ritchie.github.io/apysc/int_and_number_comparison_operations.html)

### __repr__ method docstring

Get a representation string of this instance.<hr>

**[Returns]**

- `repr_str`: str
  - Representation string of this instance.

### _set_value_and_skip_expression_appending method docstring

Update value attribute and skip expression appending.<hr>

**[Parameters]**

- `value`: int or float or Int or Number
  - Any number value to set. If float or Number value is specified, that value will be cast to integer.