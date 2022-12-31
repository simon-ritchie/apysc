# `apysc._type.variable_name_suffix_attr_or_var_mixin` docstrings

## Module summary

This module is for the attribute or variable name's suffix-related mix-in class.

## `VariableNameSuffixAttrOrVarMixIn` class docstring

### `_get_attr_or_variable_name_suffix` method docstring

Get an attribute or variable name's suffix if its value is not blank.<hr>

**[Parameters]**

- `value_identifier`: str
  - Value identifier string (e.g., `x`).

<hr>

**[Returns]**

- `attr_or_variable_name_suffix`: str
  - An attribute or variable's name suffix. In the following cases, this value becomes a blank string. - If this instance is not the `VariableNameSuffixMixIn` instance. - If a suffix is a blank string.