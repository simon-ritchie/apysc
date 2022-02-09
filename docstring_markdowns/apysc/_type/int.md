# apysc._type.int docstrings

## Module summary

Class implementation of integer.

## Int class docstring

Integer class for the apysc library.<hr>

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

- [Int and Number document](https://simon-ritchie.github.io/apysc/int_and_number.html)
- [Int and Number common arithmetic operations document](https://simon-ritchie.github.io/apysc/int_and_number_arithmetic_operations.html)
- [Int and Number common comparison operations document](https://simon-ritchie.github.io/apysc/int_and_number_comparison_operations.html)

### __init__ method docstring

Integer class for apysc library.<hr>

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

- [Int and Number document](https://simon-ritchie.github.io/apysc/int_and_number.html)
- [Int and Number common arithmetic operations document](https://simon-ritchie.github.io/apysc/int_and_number_arithmetic_operations.html)
- [Int and Number common comparison operations document](https://simon-ritchie.github.io/apysc/int_and_number_comparison_operations.html)

### __repr__ method docstring

Get a representation string of this instance.<hr>

**[Returns]**

- `repr_str`: str
  - Representation string of this instance.

### _append_cast_expression method docstring

Append integer cast (parseInt) expression.<hr>

**[Parameters]**

- `is_number_specified`: bool
  - Boolean value whether a specified value is Number instance or not.

### _set_value_and_skip_expression_appending method docstring

Update value attribute and skip expression appending.<hr>

**[Parameters]**

- `value`: int or float or Int or Number
  - Any number value to set. If float or Number value is specified, that value will be cast to integer.