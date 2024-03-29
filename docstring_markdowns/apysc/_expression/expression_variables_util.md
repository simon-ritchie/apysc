# `apysc._expression.expression_variables_util` docstrings

## Module summary

Implementations to manipulate expression variable name related interface. Mainly following interfaces are defined: <br>・get_next_variable_name: Get next variable name of specified type name. <br>・append_substitution_expression: Append substitution expression between two variables.

## `_get_next_variable_num` function docstring

Get a next variable number.<hr>

**[Parameters]**

- `type_name`: str
  - Any type name, e.g., `sprite`.

<hr>

**[Returns]**

- `next_variable_num`: int
  - Next variable number (start from 1).

## `_make_variable_name` function docstring

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

## `_save_next_variable_name_count` function docstring

Save a next variable name count value.<hr>

**[Parameters]**

- `type_name`: str
  - Any type name, e.g., `sp`.

## `append_substitution_expression` function docstring

Append a substitution expression between two variables.<hr>

**[Parameters]**

- `left_value`: VariableNameMixIn
  - Any left value.
- `right_value`: VariableNameMixIn
  - Any right value.

## `append_substitution_expression_with_names` function docstring

Append a substitution expression between two variable names.<hr>

**[Parameters]**

- `left_variable_name`: str
  - Left-side variable name.
- `right_variable_name`: str
  - Right-side variable name.

<hr>

**[Notes]**

If the left or right variable names are blank, this interface skips appending an expression.

## `get_next_variable_name` function docstring

Get next variable name of specified type name.<hr>

**[Parameters]**

- `type_name`: str
  - Any type name, e.g., `sp` (`Sprite`). If `sp` is specified and there is no `sp` variable name in expression data, this interface returns the `sp_1`. If the apysc already uses a variable name of `sp_1`, this interface returns `sp_2`.

<hr>

**[Returns]**

- `variable_name`: str
  - Next variable name.

<hr>

**[Notes]**

If calling this function multiple times, this interface increases a returned number.