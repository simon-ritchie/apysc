# apysc._validation.variable_name_validation docstrings

## Module summary

Variable name related Validation interfaces.

## validate_variable_name_interface_type function docstring

Validate specified instance type is VariableNameInterface.<hr>

**[Parameters]**

- `instance`: *
  - Instance to be checked.

<hr>

**[Returns]**

- `instance`: VariableNameInterface
  - Checked instance.

<hr>

**[Raises]**

- TypeError: If specified instance type isn't VariableNameInterface.

## VariableNameInterface class docstring



### _get_previous_variable_name method docstring

Get a previous variable name.<hr>

**[Returns]**

- `previous_variable_name`: str
  - A previous variable name of this instance. If that value is not existing, then a blank string will be returned.