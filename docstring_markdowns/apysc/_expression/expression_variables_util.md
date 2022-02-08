# apysc._expression.expression_variables_util docstrings

## Module summary

Implementations to manipulate expression variable name related interface. Mainly following interfaces are defined: <br>・get_next_variable_name: Get next variable name of specified type name. <br>・append_substitution_expression: Append substitution expression between two variables.

## _get_next_variable_num function docstring

Get a next variable number.<hr>

**[Parameters]**

- `type_name`: str
  - Any type name, e.g., `sprite`.

<hr>

**[Returns]**

- `next_variable_num`: int
  - Next variable number (start from 1).

## _make_variable_name function docstring

Make variable name from type name and variable num.<hr>

**[Parameters]**

- `type_name`: str
  - Any type name, e.g., `sprite`.
- `variable_num`: int
  - Target variable number (start from 1).

<hr>

**[Returns]**

- `variable_name`: str
  - Variable name that concatenated type name and variable number.

## _save_next_variable_name_count function docstring

Save a next variable name count value.<hr>

**[Parameters]**

- `type_name`: str
  - Any type name, e.g., `sp`.

## append_substitution_expression function docstring

Append a substitution expression between two variables.<hr>

**[Parameters]**

- `left_value`: VariableNameInterface
  - Any left value.
- `right_value`: VariableNameInterface
  - Any right value.

## append_substitution_expression_with_names function docstring

Append a substitution expression between two variable names.<hr>

**[Parameters]**

- `left_variable_name`: str
  - Left-side variable name.
- `right_variable_name`: str
  - Right-side variable name.

<hr>

**[Notes]**

If the left or the right variable names are blank, then expression appending will be skipped.

## get_next_variable_name function docstring

Get next variable name of specified type name.<hr>

**[Parameters]**

- `type_name`: str
  - Any type name, e.g., `sprite`. If `sprite` is specified and there is no `sprite` variable name in expression file, then `sprite_1` will be returned. If variable name of `sprite_1` is already used, then `sprite_2` will be returned.

<hr>

**[Returns]**

- `variable_name`: str
  - Next variable name.

<hr>

**[Notes]**

If call this function multiple times, then returned number will be increased.

## Tuple class docstring

Tuple type; Tuple[X, Y] is the cross-product type of X and Y. Example: Tuple[T1, T2] is a tuple of two elements corresponding to type variables T1 and T2. Tuple[int, float, str] is a tuple of an int, a float and a string. To specify a variable-length tuple of homogeneous type, use Tuple[T, ...].

Tuple type; Tuple[X, Y] is the cross-product type of X and Y. Example: Tuple[T1, T2] is a tuple of two elements corresponding to type variables T1 and T2. Tuple[int, float, str] is a tuple of an int, a float and a string. To specify a variable-length tuple of homogeneous type, use Tuple[T, ...].

### __add__ method docstring

Return self+value.

### TupleMeta method docstring

Metaclass for Tuple (internal).

### __contains__ method docstring

Return key in self.

### tuple method docstring

tuple() -> empty tuple tuple(iterable) -> tuple initialized from iterable's items If the argument is a tuple, the return value is the same object.

### __getitem__ method docstring

Return self[key].

### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### __iter__ method docstring

Implement iter(self).

### __len__ method docstring

Return len(self).

### __mul__ method docstring

Return self*value.

### object method docstring

The most base type

### __rmul__ method docstring

Return value*self.

### Tuple method docstring

Tuple type; Tuple[X, Y] is the cross-product type of X and Y. Example: Tuple[T1, T2] is a tuple of two elements corresponding to type variables T1 and T2. Tuple[int, float, str] is a tuple of an int, a float and a string. To specify a variable-length tuple of homogeneous type, use Tuple[T, ...].

### count method docstring

T.count(value) -> integer -- return number of occurrences of value

### index method docstring

T.index(value, [start, [stop]]) -> integer -- return first index of value. Raises ValueError if the value is not present.

## VariableNameInterface class docstring



### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### _get_previous_variable_name method docstring

Get a previous variable name.<hr>

**[Returns]**

- `previous_variable_name`: str
  - A previous variable name of this instance. If that value is not existing, then a blank string will be returned.