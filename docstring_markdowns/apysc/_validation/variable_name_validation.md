# `apysc._validation.variable_name_validation` docstrings

## Module summary

Variable name-related Validation interfaces.

## `validate_variable_name_mixin_type` function docstring

Validate specified instance type is VariableNameMixIn.<hr>

**[Parameters]**

- `instance`: *
  - Instance to be checked.
- `additional_err_msg`: str, optional
  - An additional error message to display.

<hr>

**[Returns]**

- `instance`: VariableNameMixIn
  - Checked instance.

<hr>

**[Raises]**

- TypeError: If specified instance type isn't VariableNameMixIn.