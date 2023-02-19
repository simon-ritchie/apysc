# `apysc._type.variable_name_suffix_utils` docstrings

## Module summary

The utilities implementations for the variable name suffix-related functions.

## `get_attr_or_variable_name_suffix` function docstring

Get an attribute or variable name's suffix if a specified instance's type is the `VariableNameSuffixAttrOrVarMixIn` and its suffix value is not blank.<hr>

**[Parameters]**

- `instance`: Any
  - A target instance.
- `value_identifier`: str
  - A value identifier string (e.g., `x`).

<hr>

**[Returns]**

- `attr_or_variable_name_suffix`: str
  - An attribute or variable's name suffix. In the following cases, this value becomes a blank string. - If a specified instance is not the `VariableNameSuffixMixIn` and `VariableNameSuffixAttrOrVarMixIn` instance. - If a suffix is a blank string.