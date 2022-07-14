# `apysc._type.attr_to_apysc_val_from_builtin_interface` docstrings

## Module summary

This module is for the attribute conversion interface from built-in value to apysc value.

## `AttrToApyscValFromBuiltinInterface` class docstring

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