# `apysc._type.attr_to_apysc_val_from_builtin_interface` docstrings

## Module summary

This module is for the attribute conversion interface from built-in value to apysc value.

## `_get_variable_name_suffix` function docstring

Get a target instance's variable name suffix.<hr>

**[Parameters]**

- `instance`: AttrToApyscValFromBuiltinInterface
  - A target instance.
- `attr_identifier`: str
  - Attribute identifier string (e.g., `x`).

<hr>

**[Returns]**

- `suffix`: str
  - A target instance's variable name suffix. This value becomes a blank string if a specified instance type is not the `VariableNameSuffixAttrInterface`.

## `AttrToApyscValFromBuiltinInterface` class docstring

### `_get_copied_boolean_from_builtin_val` method docstring

Get a copied Boolean value from a Python built-in bool and set an attribute's variable name suffix.<hr>

**[Parameters]**

- `bool_val`: Union[bool, Boolean]
  - Target bool value.
- `attr_identifier`: str
  - Attribute identifier string (e.g., `fill_color`).

<hr>

**[Returns]**

- `copied`: Boolean
  - Copied Boolean value.

### `_get_copied_int_from_builtin_val` method docstring

Get a copied Int value from a Python built-in int and set an attribute's variable name suffix.<hr>

**[Parameters]**

- `integer`: Union[int, Int]
  - Target integer value.
- `attr_identifier`: str
  - Attribute identifier string (e.g., `x`).

<hr>

**[Returns]**

- `copied`: Int
  - Copied Int value.

### `_get_copied_number_from_builtin_val` method docstring

Get a copied number value from a Python built-in float and set an attribute's variable name suffix.<hr>

**[Parameters]**

- `float_or_num`: Union[float, Number]
  - Target float (or Number) value.
- `attr_identifier`: str
  - Attribute identifier string (e.g., `fill_alpha`).

<hr>

**[Returns]**

- `copied`: Number
  - Copied Number value.

### `_get_copied_string_from_builtin_val` method docstring

Get a copied String value from a Python built-in str and set an attribute's variable name suffix.<hr>

**[Parameters]**

- `string`: Union[str, String]
  - Target string value.
- `attr_identifier`: str
  - Attribute identifier string (e.g., `fill_color`).

<hr>

**[Returns]**

- `copied`: String
  - Copied String value.