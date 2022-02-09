# apysc._type.boolean docstrings

## Module summary

Class implementation for boolean.

## Boolean class docstring

Boolean class for the apysc library.<hr>

**[Notes]**

The Bool class is the alias of the Boolean, and it behaves the same as the Boolean class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> bool_val_1: ap.Boolean = ap.Boolean(True)
>>> bool_val_1
Boolean(True)

>>> bool_val_2: ap.Bool = ap.Bool(True)
>>> bool_val_2
Boolean(True)

>>> bool_val_2.not_
Boolean(False)
```

<hr>

**[References]**

- [Boolean document](https://simon-ritchie.github.io/apysc/boolean.html)

### __bool__ method docstring

Get a boolean value directly.<hr>

**[Returns]**

- `result`: bool
  - Current boolean value.

### __eq__ method docstring

Comparison method for equal condition.<hr>

**[Parameters]**

- `other`: *
  - Other value to compare (Boolean, bool, int, or Int).

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### __init__ method docstring

Boolean class for apysc library.<hr>

**[Parameters]**

- `value`: bool or int or Boolean or Int
  - Initial boolean value. 0 or 1 are acceptable for an integer value.

<hr>

**[Notes]**

The Bool class is the alias of the Boolean, and it behaves the same as the Boolean class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> bool_val_1: ap.Boolean = ap.Boolean(True)
>>> bool_val_1
Boolean(True)

>>> bool_val_2: ap.Bool = ap.Bool(True)
>>> bool_val_2
Boolean(True)
```

<hr>

**[References]**

- [Boolean document](https://simon-ritchie.github.io/apysc/boolean.html)

### __ne__ method docstring

Comparison method for not equal condition.<hr>

**[Parameters]**

- `other`: *
  - Other value to compare (Boolean, bool, int, or Int).

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### __repr__ method docstring

Get a representation string of this instance.<hr>

**[Returns]**

- `repr_str`: str
  - Representation string of this instance.

### _append_constructor_expression method docstring

Append constructor expression.

### _append_eq_expression method docstring

Append __eq__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: Boolean or Int
  - Other value to compare.

### _append_ne_expression method docstring

Append __ne__ method expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result boolean value.
- `other`: Boolean or Int
  - Other value to compare.

### _append_not_prop_expression method docstring

Append not_ property expression.<hr>

**[Parameters]**

- `result`: Boolean
  - Result Boolean value.

### _append_value_setter_expression method docstring

Append value's setter expression.<hr>

**[Parameters]**

- `value`: bool or VariableNameInterface
  - Any value to set.

### _get_bool_from_arg_value method docstring

Get bool value from specified argument value.<hr>

**[Parameters]**

- `value`: bool or int or Boolean or Int
  - Specified value. 0 or 1 are acceptable for integer value.

<hr>

**[Returns]**

- `result`: bool
  - Converted boolean value.

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

### _set_value_and_skip_expression_appending method docstring

Update value attribute and skip expression appending.<hr>

**[Parameters]**

- `value`: bool or int or Boolean or Int
  - Any boolean value to set.

### _validate_comparison_other_type method docstring

Validate comparison's other value type.<hr>

**[Parameters]**

- `other`: *
  - Other value to compare.

<hr>

**[Raises]**

- ValueError: If other value type is not Boolean, bool, Int, and int.