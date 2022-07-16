# `apysc._converter.to_apysc_val_from_builtin` docstrings

## Module summary

Each interface to get an apysc value from a Python built-in one.

## `get_copied_boolean_from_builtin_val` function docstring

Get a copied Boolean value from a Python built-in bool.<hr>

**[Parameters]**

- `bool_val`: bool or Boolean
  - Target bool value.
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript's debugging.

<hr>

**[Returns]**

- `copied`: Boolean
  - Copied Boolean value.

## `get_copied_int_from_builtin_val` function docstring

Get a copied Int value from a Python built-in int.<hr>

**[Parameters]**

- `integer`: int or Int
  - Target integer value.
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript's debugging.

<hr>

**[Returns]**

- `copied`: Int
  - Copied Int value.

## `get_copied_number_from_builtin_val` function docstring

Get a copied number value from a Python built-in float.<hr>

**[Parameters]**

- `float_or_num`: float or Number
  - Target float (or Number) value.
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript's debugging.

<hr>

**[Returns]**

- `copied`: Number
  - Copied Number value.

## `get_copied_string_from_builtin_val` function docstring

Get a copied String value from a Python built-in str.<hr>

**[Parameters]**

- `string`: str or String
  - Target string value.
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript's debugging.

<hr>

**[Returns]**

- `copied`: String
  - Copied String value.