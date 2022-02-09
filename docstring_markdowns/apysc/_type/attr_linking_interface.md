# apysc._type.attr_linking_interface docstrings

## Module summary

Class implementation for the attribute linking interface. This interface is used for updating an old property value to achieve consistency in the handler functions.

### _append_applying_new_attr_val_exp method docstring

Append the expression of applying new attribute value to each stacked value.<hr>

**[Parameters]**

- `new_attr`: Int or Number or String or Boolean
  - New attribute value.
- `attr_name`: str
  - Target attribute name.

### _append_attr_to_linking_stack method docstring

Append an attribute to the linking attribute stack.<hr>

**[Parameters]**

- `attr`: Int or Number or String or Boolean
  - Target attribute to be appended.
- `attr_name`: str
  - Target attribute name.

### _initialize_attr_linking_stack method docstring

Initialize the _attr_linking_stack attribute if it hasn't been initialized yet.<hr>

**[Parameters]**

- `attr_name`: str
  - Target attribute name.

### _is_target_attr_already_linked method docstring

Get a boolean value whether a specified attribute has already been appended to the linking attribute stack.<hr>

**[Parameters]**

- `attr`: Int or Number or String or Boolean
  - Target attribute to be appended.
- `attr_name`: str
  - Target attribute name.

<hr>

**[Returns]**

- `result`: bool
  - If a specified attribute has already been appended to the linking stack, this value will be True.