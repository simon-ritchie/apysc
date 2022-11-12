# `apysc._type.variable_name_suffix_attr_interface` docstrings

## Module summary

This module is for the attribute's variable name suffix-related interface class.

## `VariableNameSuffixAttrInterface` class docstring

### `_get_attr_variable_name_suffix` method docstring

Get an attribute's variable name suffix if its value is not blank.<hr>

**[Parameters]**

- `attr_identifier`: str
  - Attribute identifier string (e.g., `x`).

<hr>

**[Returns]**

- `attr_variable_name_suffix`: str
  - An attribute's variable name suffix. In the following cases, this value becomes a blank string. - If this instance is not the `VariableNameSuffixMixIn` instance. - If a suffix is a blank string.