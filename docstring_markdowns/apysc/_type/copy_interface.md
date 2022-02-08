# apysc._type.copy_interface docstrings

## Module summary

Class implementation for copy interface.

## deepcopy function docstring

Deep copy operation on arbitrary Python objects. See the module's __doc__ string for more info.

## CopyInterface class docstring



### _append_copy_expression method docstring

Append copy expression.<hr>

**[Parameters]**

- `result_variable_name`: str
  - Copied value's variable name.

### _append_value_updating_cpy_exp_to_handler_scope method docstring

Append a value updating copy expression if the current scope is an event handler's one.<hr>

**[Parameters]**

- `result_variable_name`: str
  - Copied value's variable name.

### _copy method docstring

Make a deep copy of this instance.<hr>

**[Returns]**

- `result`: *
  - Copied instance.

### _get_previous_variable_name method docstring

Get a previous variable name.<hr>

**[Returns]**

- `previous_variable_name`: str
  - A previous variable name of this instance. If that value is not existing, then a blank string will be returned.

## TypeNameInterface class docstring



## VariableNameInterface class docstring



### _get_previous_variable_name method docstring

Get a previous variable name.<hr>

**[Returns]**

- `previous_variable_name`: str
  - A previous variable name of this instance. If that value is not existing, then a blank string will be returned.