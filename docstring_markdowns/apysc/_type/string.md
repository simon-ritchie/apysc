# apysc._type.string docstrings

## Module summary

Class implementation for string.

## String class docstring

String class for apysc library.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> string: ap.String = ap.String('Hello')
>>> string
String('Hello')

>>> string += ' World!'
>>> string
String('Hello World!')

>>> string.value = 'World!'
>>> string
String('World!')

>>> string.value = 'Hello!'
>>> string *= 3
>>> string
String('Hello!Hello!Hello!')
```

<hr>

**[References]**

- [String document](https://simon-ritchie.github.io/apysc/string.html)
- [String class comparison operations document](https://simon-ritchie.github.io/apysc/string_comparison_operations.html)
- [String class addition and multiplication operations document](https://simon-ritchie.github.io/apysc/string_addition_and_multiplication.html)

### __add__ method docstring

Method for addition (string concatenation).<hr>

**[Parameters]**

- `other`: str or String
  - Other string value to concatenate.

<hr>

**[Returns]**

- `result`: String
  - Concatenated result string.

### __eq__ method docstring

Method for equal comparison.<hr>

**[Parameters]**

- `other`: *
  - Any value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result. If same value of str or String is specified, True will be returned.

### __float__ method docstring

Method for float conversion.<hr>

**[Returns]**

- `result`: float
  - Converted float value.

### __ge__ method docstring

Method for greater than or equal comparison.<hr>

**[Parameters]**

- `other`: str or String
  - String value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### __gt__ method docstring

Method for greater than comparison.<hr>

**[Parameters]**

- `other`: str or String
  - String value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### __iadd__ method docstring

Method for incremental addition (string concatenation).<hr>

**[Parameters]**

- `other`: str or String
  - Other string value to concatenate.

<hr>

**[Returns]**

- `result`: String
  - Concatenated result string.

### __imul__ method docstring

Method for incremental multiplication (string repetition).<hr>

**[Parameters]**

- `other`: int or Int
  - String repetition number.

<hr>

**[Returns]**

- `result`: String
  - Repetition result string.

### __init__ method docstring

String class for apysc library.<hr>

**[Parameters]**

- `value`: str or String
  - Initial string value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> string: ap.String = ap.String('Hello')
>>> string
String('Hello')

>>> string += ' World!'
>>> string
String('Hello World!')
```

<hr>

**[References]**

- [String document](https://simon-ritchie.github.io/apysc/string.html)
- [String class comparison operations document](https://simon-ritchie.github.io/apysc/string_comparison_operations.html)
- [String class addition and multiplication operations document](https://simon-ritchie.github.io/apysc/string_addition_and_multiplication.html)

### __int__ method docstring

Method for integer conversion.<hr>

**[Returns]**

- `result`: int
  - Converted integer value.

### __le__ method docstring

Method for less than or equal comparison.<hr>

**[Parameters]**

- `other`: str or String
  - String value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### __lt__ method docstring

Method for less than comparison.<hr>

**[Parameters]**

- `other`: str or String
  - String value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### __mul__ method docstring

Method for multiplication (string repetition).<hr>

**[Parameters]**

- `other`: int or Int
  - String repetition number.

<hr>

**[Returns]**

- `result`: String
  - Repeated result string.

### __ne__ method docstring

Method for not equal comparison.<hr>

**[Parameters]**

- `other`: *
  - Any value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result. If not same value of str or String is specified, True will be returned.

### __repr__ method docstring

Get a representation string of this instance.<hr>

**[Returns]**

- `repr_str`: str
  - Representation string of this instance.

### __str__ method docstring

Method for str conversion.<hr>

**[Returns]**

- `result`: str
  - Python builtins str value.

### _append_addition_expression method docstring

Append addition (string concatenation) expression.<hr>

**[Parameters]**

- `result`: String
  - Addition result value.
- `other`: str or String
  - Other string value to concatenate.

### _append_constructor_expression method docstring

Append constructor expression.

### _append_eq_expression method docstring

Append __eq__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameInterface
  - Other value to compare.

### _append_ge_expression method docstring

Append __ge__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameInterface
  - Other value to compare.

### _append_gt_expression method docstring

Append __gt__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameInterface
  - Other value to compare.

### _append_le_expression method docstring

Append __le__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameInterface
  - Other value to compare.

### _append_lt_expression method docstring

Append __lt__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameInterface
  - Other value to compare.

### _append_multiplication_expression method docstring

Append multiplication (string repetition) expression.<hr>

**[Parameters]**

- `result`: String
  - Multiplication result value.
- `other`: int or Int
  - String repetition number.

### _append_ne_expression method docstring

Append __ne__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameInterface
  - Other value to compare.

### _append_value_setter_expression method docstring

Append value's setter expression.<hr>

**[Parameters]**

- `value`: str or String
  - Any string value to set.

### _convert_other_val_to_string method docstring

If comparison other value is string, then convert it to String.<hr>

**[Parameters]**

- `other`: *
  - Other comparison value.

<hr>

**[Returns]**

- `converted_val`: *
  - Converted value. If other value is string, then this will be String instance. Other type will be returned directly (not to be converted).

### _get_str_value method docstring

Get a (Python's) str value from specified value.<hr>

**[Parameters]**

- `value`: str or String
  - Target string value.

<hr>

**[Returns]**

- `value`: str
  - Python's builtin str value.

### _make_snapshot method docstring

Make a value's snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _revert method docstring

Revert a value if snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.