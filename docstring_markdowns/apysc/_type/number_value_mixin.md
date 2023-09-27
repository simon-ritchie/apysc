# `apysc._type.number_value_mixin` docstrings

## Module summary

Class implementation for number value mix-in.

## `NumberValueMixIn` class docstring

### `__add__` method docstring

Method for addition.<hr>

**[Parameters]**

- `other`: NumberValueMixIn or int or float
  - Other value to add.

<hr>

**[Returns]**

- `result`: NumberValueMixIn
  - Addition result value.

### `__eq__` method docstring

Equal comparison method.<hr>

**[Parameters]**

- `other`: *
  - The other value to compare. Builtin types, Int, and Number class instances are acceptable.

<hr>

**[Returns]**

- `result`: Boolean
  - If a specified value is the same amount, this interface returns True.

### `__float__` method docstring

Float conversion method.<hr>

**[Returns]**

- `float_`: float
  - Converted float value.

### `__floordiv__` method docstring

Method for floor division (return integer).<hr>

**[Parameters]**

- `other`: NumberValueMixIn or int or float
  - Other value for floor division.

<hr>

**[Returns]**

- `result`: Int
  - Floor division result value.

### `__ge__` method docstring

Greater than equal comparison method.<hr>

**[Parameters]**

- `other`: *
  - The other value to compare. Builtin types, Int, and Number class instances are acceptable.

<hr>

**[Returns]**

- `result`: Boolean
  - If this value is greater than or equal to a specified value, this interface returns True.

### `__gt__` method docstring

Greater than comparison method.<hr>

**[Parameters]**

- `other`: *
  - The other value to compare. Builtin types, Int, and Number class instances are acceptable.

<hr>

**[Returns]**

- `result`: Boolean
  - If this value is greater than a specified value, this interface returns True.

### `__iadd__` method docstring

Method for incremental addition.<hr>

**[Parameters]**

- `other`: NumberValueMixIn or int or float
  - Other value for` incremental addition.

<hr>

**[Returns]**

- `result`: NumberValueMixIn
  - Incremental addition result value.

### `__imul__` method docstring

Method for incremental multiplication.<hr>

**[Parameters]**

- `other`: NumberValueMixIn or int or float
  - Other value for incremental multiplication.

<hr>

**[Returns]**

- `result`: NumberValueMixIn
  - Incremental multiplication result value.

### `__init__` method docstring

Class for number value interface.<hr>

**[Parameters]**

- `value`: NumberValueMixIn or int or float
  - Initial number value.
- `type_name`: str
  - This instance expression's type name (e.g., int, number).
- `variable_name_suffix`: str, default ""
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

### `__int__` method docstring

Integer conversion method.<hr>

**[Returns]**

- `integer`: int
  - Converted integer value.

### `__isub__` method docstring

Method for incremental subtraction.<hr>

**[Parameters]**

- `other`: NumberValueMixIn or int or float
  - Other value for incremental subtraction.

<hr>

**[Returns]**

- `result`: NumberValueMixIn
  - Incremental subtraction result value.

### `__itruediv__` method docstring

Method for incremental true division.<hr>

**[Parameters]**

- `other`: NumberValueMixIn or int or float
  - Other value for incremental true division.

<hr>

**[Returns]**

- `result`: NumberValueMixIn
  - The other value for incremental-true division.

### `__le__` method docstring

Less than equal comparison method.<hr>

**[Parameters]**

- `other`: *
  - The other value to compare. Builtin types, Int, and Number class instances are acceptable.

<hr>

**[Returns]**

- `result`: Boolean
  - If this value is less than or equal to a specified value, this interface returns True.

### `__lt__` method docstring

Less than comparison method.<hr>

**[Parameters]**

- `other`: *
  - The other value to compare. Builtin types, Int, and Number class instances are acceptable.

<hr>

**[Returns]**

- `result`: Boolean
  - If this value is less than a specified value, this interface returns True.

### `__mod__` method docstring

Method for the modulo operation.<hr>

**[Parameters]**

- `other`: NumberValueMixIn or int or float
  - The other value to use in the modulo operation.

<hr>

**[Returns]**

- `result`: NumberValueMixIn
  - Modulo operation result value.

### `__mul__` method docstring

Method for multiplication.<hr>

**[Parameters]**

- `other`: NumberValueMixIn or int or float
  - Other value to multiply.

<hr>

**[Returns]**

- `result`: NumberValueMixIn
  - Multiplication result value.

### `__ne__` method docstring

Not equal comparison method.<hr>

**[Parameters]**

- `other`: *
  - The other value to compare. Builtin types, Int, and Number class instances are acceptable.

<hr>

**[Returns]**

- `result`: Boolean
  - If a specified value is not the same amount, this interface returns True.

### `__str__` method docstring

String conversion method.<hr>

**[Returns]**

- `string`: str
  - Converted value string.

### `__sub__` method docstring

Method for subtraction.<hr>

**[Parameters]**

- `other`: NumberValueMixIn or int or float
  - The other value to subtract.

<hr>

**[Returns]**

- `result`: NumberValueMixIn
  - Subtraction result value.

### `__truediv__` method docstring

Method for true division (returns floating-point number).<hr>

**[Parameters]**

- `other`: NumberValueMixIn or int or float
  - Other value for true-division.

<hr>

**[Returns]**

- `result`: Number
  - True division result value.

### `_append_addition_expression` method docstring

Append addition expression.<hr>

**[Parameters]**

- `result`: NumberValueMixIn
  - Addition result value.
- `other`: NumberValueMixIn or int or float
  - Other value to add.

### `_append_constructor_expression` method docstring

Append a current value's constructor expression.

### `_append_eq_expression` method docstring

Append __eq__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameMixIn
  - The other value to compare.

### `_append_floor_division_expression` method docstring

Append floor division expression.<hr>

**[Parameters]**

- `result`: NumberValueMixIn
  - Floor division result value.
- `other`: NumberValueMixIn or int or float
  - Other value for floor division.

### `_append_ge_expression` method docstring

Append __ge__ expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameMixIn
  - The other value to compare.

### `_append_gt_expression` method docstring

Append __gt__ expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameMixIn
  - The other value to compare.

### `_append_incremental_calc_substitution_expression` method docstring

Append an incremental calculation's substitution expression. Each interface call this method.

### `_append_le_expression` method docstring

Append __le__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameMixIn
  - The other value to compare.

### `_append_lt_expression` method docstring

Append __lt__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameMixIn
  - The other value to compare.

### `_append_modulo_expression` method docstring

Append a module expression.<hr>

**[Parameters]**

- `result`: NumberValueMixIn
  - Modulo operation result value.
- `other`: NumberValueMixIn or int or float
  - The other value to use in the modulo operation.

### `_append_multiplication_expression` method docstring

Append multiplication expression.<hr>

**[Parameters]**

- `result`: NumberValueMixIn
  - Multiplication result value.
- `other`: NumberValueMixIn or int or float
  - Other value to multiply.

### `_append_ne_expression` method docstring

Append __ne__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: VariableNameMixIn
  - The other value to compare.

### `_append_subtraction_expression` method docstring

Append subtraction expression.<hr>

**[Parameters]**

- `result`: NumberValueMixIn
  - Subtraction result value.
- `other`: NumberValueMixIn or int or float
  - Other value to subtract.

### `_append_true_division_expression` method docstring

Append true division expression.<hr>

**[Parameters]**

- `result`: NumberValueMixIn
  - True division result value.
- `other`: NumberValueMixIn or int or float
  - Other value for true division.

### `_append_value_setter_expression` method docstring

Append value's setter-expresion.<hr>

**[Parameters]**

- `value`: NumberValueMixIn or int or float
  - Any number value to set.

### `_convert_other_val_to_int_or_number` method docstring

Convert a specified other value if comparison its type is an int or float, then convert it to Int or Number.<hr>

**[Parameters]**

- `other`: *
  - Other comparison value.

<hr>

**[Returns]**

- `converted_val`: *
  - Converted value. If an int is specified, this interface converts it to an Int. Similarly, if a float is specified, this interface converts it to a Number value. This interface returns the other type directly (not to be converted).

### `_create_initial_substitution_expression` method docstring

Create an initial value's substitution expression string.<hr>

**[Returns]**

- `expression`: str
  - Created expression string.

### `_make_snapshot` method docstring

Make value's snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `_revert` method docstring

Revert value if snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `_set_value_and_skip_expression_appending` method docstring

Update value attribute and skip expression appending.<hr>

**[Parameters]**

- `value`: NumberValueMixIn or int or float
  - Any number value to set.