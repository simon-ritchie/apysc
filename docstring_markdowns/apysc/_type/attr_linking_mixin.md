# `apysc._type.attr_linking_mixin` docstrings

## Module summary

Class implementation for the attribute linking mix-in. This mix-in updates an old property value to achieve consistency in the handler functions.

## `_get_variable_name_from_attr` function docstring

Get a variable name from a specified attribute.<hr>

**[Parameters]**

- `attr`: _Attr
  - An attribute.

<hr>

**[Returns]**

- `variable_name`: str
  - A specified attribute's variable name.

## `AttrLinkingMixIn` class docstring

### `_append_applying_new_attr_val_exp` method docstring

Append the expression of applying a new attribute value to each stacked value.<hr>

**[Parameters]**

- `new_attr`: Int or Number or String or Boolean
  - New attribute value.
- `attr_name`: str
  - Target attribute name.

### `_append_attr_to_linking_stack` method docstring

Append an attribute to the linking attribute stack.<hr>

**[Parameters]**

- `attr`: Int or Number or String or Boolean
  - Target attribute to be appended.
- `attr_name`: str
  - Target attribute name.

### `_initialize_attr_linking_stack` method docstring

Initialize the _attr_linking_stack attribute if this instance does not initialize it yet.<hr>

**[Parameters]**

- `attr_name`: str
  - Target attribute name.

### `_is_target_attr_already_linked` method docstring

Get a boolean value whether this instance already appends a specified attribute to the linking attribute stack.<hr>

**[Parameters]**

- `attr`: Int or Number or String or Boolean
  - Target attribute to be appended.
- `attr_name`: str
  - Target attribute name.

<hr>

**[Returns]**

- `result`: bool
  - If this instance already appends a specified attribute to the linking stack, this interface returns True.