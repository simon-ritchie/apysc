# `apysc._type.number` docstrings

## Module summary

Class implementation of the floating-point number value.

## `Number` class docstring

Floating point number class for the apysc library.<hr>

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

- [Int and Number](https://simon-ritchie.github.io/apysc/en/int_and_number.html)
- [Int and Number common arithmetic operations](https://simon-ritchie.github.io/apysc/en/int_and_number_arithmetic_operations.html)
- [Int and Number common comparison operations](https://simon-ritchie.github.io/apysc/en/int_and_number_comparison_operations.html)

### `__init__` method docstring

Floating point number class for apysc library.<hr>

**[Parameters]**

- `value`: int or float or Int or Number
  - Initial floating point number value. This class casts it to float if you specify int or Int value.
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.
- `skip_init_substitution_expression_appending`: bool, default False
  - A boolean indicates whether to skip an initial substitution expression or not. This class uses this option internally.

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

- [Int and Number](https://simon-ritchie.github.io/apysc/en/int_and_number.html)
- [Int and Number common arithmetic operations](https://simon-ritchie.github.io/apysc/en/int_and_number_arithmetic_operations.html)
- [Int and Number common comparison operations](https://simon-ritchie.github.io/apysc/en/int_and_number_comparison_operations.html)

### `__repr__` method docstring

Get a representation string of this instance.<hr>

**[Returns]**

- `repr_str`: str
  - Representation string of this instance.

### `_initialize_for_loop_key_or_value` method docstring

Initialize this instance for a loop value.<hr>

**[Returns]**

- `num_value`: Number
  - An initialized number value.

### `_set_value_and_skip_expression_appending` method docstring

Update value attribute and skip expression appending.<hr>

**[Parameters]**

- `value`: int or float or Int or Number
  - Any number value to set. If a float or Number value is specified, this interface casts its value to an integer.