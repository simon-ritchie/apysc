# `apysc._type.value_util` docstrings

## Module summary

Each types common value utilities. Mainly following interfaces are defined: <br>・get_value_str_for_expression Get a value string for expression. <br>・get_copy Get a copy of specified instance if it is instance of CopyInterface.

## `_get_value_str_from_dict` function docstring

Get a value string from dictionary object.<hr>

**[Parameters]**

- `value`: dict
  - Dictionary object to convert to string.

<hr>

**[Returns]**

- `value_str`: str
  - Converted string, e.g., '{"any_key": 10, "other_key": any_variable}'

## `_get_value_str_from_iterable` function docstring

Get a value string from iterable object.<hr>

**[Parameters]**

- `value`: list or tuple or Array
  - Target iterable object.

<hr>

**[Returns]**

- `value_str`: str
  - Converted string, e.g., '[10, "Hello!", true, any_variable]'.

## `_validate_dict_key_type` function docstring

Validate whether a dictionary key type is str or int.<hr>

**[Parameters]**

- `key`: *
  - Dictionary key to validate.

<hr>

**[Raises]**

- TypeError: If key type isn't str or int.

## `get_copy` function docstring

Get a copy of specified instance if it is instance of CopyInterface.<hr>

**[Parameters]**

- `value`: *
  - Any value to copy.

<hr>

**[Returns]**

- `copied`: *
  - Copied value. If value is not instance of CopyInterface, then argument value will be returned directly.

## `get_value_str_for_expression` function docstring

Get a value string for expression.<hr>

**[Parameters]**

- `value`: *
  - Any value to convert to string.

<hr>

**[Returns]**

- `value_str`: str
  - String for expression. If value is instance of VariableNameInterface, then variable's name will be returned, otherwise string casted value will be returned. Bool value will be lowercase (true or false) and str value will be quoted by double quotation. List or tuple value will be converted to js Array expression, e.g., '[10, "Hello!", true, any_variable]'. None will be Nan.