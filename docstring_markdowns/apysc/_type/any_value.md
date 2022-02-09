# apysc._type.any_value docstrings

## Module summary

Class implementation of any value.

## AnyValue class docstring

Class implementation of any value (value that can't determine type).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> any_value: ap.AnyValue = ap.AnyValue(10)
>>> any_value.value
10

>>> any_value.value = 20
>>> any_value.value
20
```

### __add__ method docstring

Method for addition.<hr>

**[Parameters]**

- `other`: Any
  - Other value to add.

<hr>

**[Returns]**

- `result`: AnyValue
  - Addition result value.

### __eq__ method docstring

Equal comparison method.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result. This will always be False on Python since correct comparison is not possible.

### __floordiv__ method docstring

Method for floor division.<hr>

**[Parameters]**

- `other`: Any
  - Other value for floor division.

<hr>

**[Returns]**

- `result`: AnyValue
  - Floor division result value.

### __ge__ method docstring

Greater than equal comparison method.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result. This will always be False on Python since correct comparison is not possible.

### __gt__ method docstring

Greater than comparison method.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result. This will always be False on Python since correct comparison is not possible.

### __iadd__ method docstring

Method for incremental addition.<hr>

**[Parameters]**

- `other`: Any
  - Other value for incremental addition.

<hr>

**[Returns]**

- `result`: AnyValue
  - Incremental addition result value.

### __imul__ method docstring

Method for incremental multiplication.<hr>

**[Parameters]**

- `other`: Any
  - Other value for incremental multiplication.

<hr>

**[Returns]**

- `result`: AnyValue
  - Incremental multiplication result value.

### __init__ method docstring

Class implementation of any value (value that can't determine type).<hr>

**[Parameters]**

- `value`: *
  - Initial any value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> any_value: ap.AnyValue = ap.AnyValue(10)
>>> any_value.value
10
```

### __isub__ method docstring

Method for incremental subtraction.<hr>

**[Parameters]**

- `other`: Any
  - Other value for incremental subtraction.

<hr>

**[Returns]**

- `result`: AnyValue
  - Incremental subtraction result value.

### __itruediv__ method docstring

Method for incremental true division.<hr>

**[Parameters]**

- `other`: Any
  - Other value for incremental division.

<hr>

**[Returns]**

- `result`: AnyValue
  - Incremental division result value.

### __le__ method docstring

Less than equal comparison method.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result. This will always be False on Python since correct comparison is not possible.

### __lt__ method docstring

Less than comparison method.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result. This will always be False on Python since correct comparison is not possible.

### __mul__ method docstring

Method for multiplication.<hr>

**[Parameters]**

- `other`: Any
  - Other value to multiply.

<hr>

**[Returns]**

- `result`: AnyValue
  - Subtraction result value.

### __ne__ method docstring

Not equal comparison method.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result. This will always be False on Python since correct comparison is not possible.

### __sub__ method docstring

Method for subtraction.<hr>

**[Parameters]**

- `other`: Any
  - Other value to subtract.

<hr>

**[Returns]**

- `result`: AnyValue
  - Subtraction result value.

### __truediv__ method docstring

Method for true division.<hr>

**[Parameters]**

- `other`: Any
  - Other value for true division.

<hr>

**[Returns]**

- `result`: AnyValue
  - True division result value.

### _append_arithmetic_operation_expression method docstring

Append arithmetic operation (e.g., addition) expression.<hr>

**[Parameters]**

- `other`: Any
  - Other value to use.
- `operator`: str
  - JavaScript arithmetic operator, like '+', '*', and so on.

<hr>

**[Returns]**

- `result`: AnyValue
  - Calculated result value.

### _append_comparison_expression method docstring

Append comparison operation expression.<hr>

**[Parameters]**

- `comparison_operator`: str
  - JavaScript comparison operator (e.g., '===', '>=', and so on).
- `other`: Any
  - Other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result. This will always be False on Python since correct comparison is not possible.

### _append_constructor_expression method docstring

Append constructor expression.

### _append_incremental_arithmetic_operation_expression method docstring

Append incremental arithmetic operation (e.g., incremental addition) expression.<hr>

**[Parameters]**

- `other`: Any
  - Other value to use.
- `operator`: str
  - JavaScript arithmetic operator, like '+=', '*=', and so on.

### _append_value_setter_expression method docstring

Append value's setter expression.<hr>

**[Parameters]**

- `value`: *
  - Any value to set.

### _make_snapshot method docstring

Make value's snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _revert method docstring

Revert value if snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.