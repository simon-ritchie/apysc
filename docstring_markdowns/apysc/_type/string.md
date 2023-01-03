# `apysc._type.string` docstrings

## Module summary

Class implementation for the string class.

## `String` class docstring

String class for apysc library.<hr>

**[Notes]**

The `Str` class is the alias of `String`.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> string: ap.String = ap.String("Hello")
>>> string
String('Hello')

>>> string += " World!"
>>> string
String('Hello World!')

>>> string.value = "World!"
>>> string
String('World!')

>>> string.value = "Hello!"
>>> string *= 3
>>> string
String('Hello!Hello!Hello!')
```

<hr>

**[References]**

- [String](https://simon-ritchie.github.io/apysc/en/string.html)
- [String class comparison operations](https://simon-ritchie.github.io/apysc/en/string_comparison_operations.html)
- [String class addition and multiplication operations](https://simon-ritchie.github.io/apysc/en/string_addition_and_multiplication.html)

### `__add__` method docstring

Method for addition (string concatenation).<hr>

**[Parameters]**

- `other`: String or str
  - The other string value to concatenate.

<hr>

**[Returns]**

- `result`: String
  - Concatenated result string.

### `__eq__` method docstring

Method for equal comparison.<hr>

**[Parameters]**

- `other`: *
  - Any value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result. If the equal value of a String or str is specified, this interface returns True.

### `__float__` method docstring

Method for float conversion.<hr>

**[Returns]**

- `result`: float
  - Converted float value.

### `__ge__` method docstring

Method for greater than or equal comparison.<hr>

**[Parameters]**

- `other`: String or str
  - String value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### `__gt__` method docstring

Method for greater than comparison.<hr>

**[Parameters]**

- `other`: String or str
  - String value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### `__iadd__` method docstring

Method for incremental addition (string concatenation).<hr>

**[Parameters]**

- `other`: String or str
  - The other string value to concatenate.

<hr>

**[Returns]**

- `result`: String
  - Concatenated result string.

### `__imul__` method docstring

Method for incremental multiplication (string repetition).<hr>

**[Parameters]**

- `other`: Int or int
  - String repetition number.

<hr>

**[Returns]**

- `result`: String
  - Repetition result string.

### `__init__` method docstring

String class for apysc library.<hr>

**[Parameters]**

- `value`: String or str
  - Initial string value.
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript's debugging.
- `skip_init_substitution_expression_appending`: bool, default False
  - A boolean indicates whether to skip an initial substitution expression or not. This class uses this option internally.

<hr>

**[Notes]**

The `Str` class is the alias of `String`.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> string: ap.String = ap.String("Hello")
>>> string
String('Hello')

>>> string += " World!"
>>> string
String('Hello World!')
```

<hr>

**[References]**

- [String](https://simon-ritchie.github.io/apysc/en/string.html)
- [String class comparison operations](https://simon-ritchie.github.io/apysc/en/string_comparison_operations.html)
- [String class addition and multiplication operations](https://simon-ritchie.github.io/apysc/en/string_addition_and_multiplication.html)

### `__int__` method docstring

Method for integer conversion.<hr>

**[Returns]**

- `result`: int
  - Converted integer value.

### `__le__` method docstring

Method for less than or equal comparison.<hr>

**[Parameters]**

- `other`: String or str
  - String value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### `__lt__` method docstring

Method for less than comparison.<hr>

**[Parameters]**

- `other`: String or str
  - String value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### `__mul__` method docstring

Method for multiplication (string repetition).<hr>

**[Parameters]**

- `other`: Int or int
  - String repetition number.

<hr>

**[Returns]**

- `result`: String
  - Repeated result string.

### `__ne__` method docstring

Method for not equal comparison.<hr>

**[Parameters]**

- `other`: *
  - Any value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result. If a specified value is not the equal value of a String or str, this interface returns True.

### `__repr__` method docstring

Get a representation string of this instance.<hr>

**[Returns]**

- `repr_str`: str
  - Representation string of this instance.

### `__str__` method docstring

Method for str conversion.<hr>

**[Returns]**

- `result`: str
  - Python builtins str value.

### `_append_addition_expression` method docstring

Append addition (string concatenation) expression.<hr>

**[Parameters]**

- `result`: String
  - Addition result value.
- `other`: String or str
  - The other string value to concatenate.

### `_append_constructor_expression` method docstring

Append a constructor expression.

### `_append_eq_expression` method docstring

Append __eq__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameMixIn
  - Other value to compare.

### `_append_ge_expression` method docstring

Append __ge__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameMixIn
  - Other value to compare.

### `_append_gt_expression` method docstring

Append __gt__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameMixIn
  - Other value to compare.

### `_append_le_expression` method docstring

Append __le__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameMixIn
  - Other value to compare.

### `_append_lt_expression` method docstring

Append __lt__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameMixIn
  - Other value to compare.

### `_append_multiplication_expression` method docstring

Append multiplication (string repetition) expression.<hr>

**[Parameters]**

- `result`: String
  - Multiplication result value.
- `other`: Int or int
  - String repetition number.

### `_append_ne_expression` method docstring

Append __ne__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameMixIn
  - Other value to compare.

### `_append_value_setter_expression` method docstring

Append value's setter expression.<hr>

**[Parameters]**

- `value`: String or str
  - Any string value to set.

### `_convert_other_val_to_string` method docstring

Convert a comparison other value to a String if it is a string value.<hr>

**[Parameters]**

- `other`: *
  - Other comparison value.

<hr>

**[Returns]**

- `converted_val`: *
  - Converted value. If the other value is a string, this interface converts it to a String value. This interface returns the other type value directly (not to be converted).

### `_create_initial_substitution_expression` method docstring

Create an initial value's substitution expression string.<hr>

**[Returns]**

- `expression`: str
  - Created expression string.

### `_get_str_value` method docstring

Get a (Python's) str value from a specified value.<hr>

**[Parameters]**

- `value`: String or str
  - Target string value.

<hr>

**[Returns]**

- `value`: str
  - Python's built-in str value.

### `_make_snapshot` method docstring

Make a value snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `_revert` method docstring

Revert a value if a snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.