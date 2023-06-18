# `apysc._type.value_util` docstrings

## Module summary

Each types common value utilities. Mainly following interfaces are defined: <br>・get_value_str_for_expression <br> ・Get a value string for expression. <br>・get_copy <br> ・Get a copy of a specified instance if it is an instance of CopyMixIn.

## `_get_value_str_from_dict` function docstring

Get a value string from a dictionary object.<hr>

**[Parameters]**

- `value`: dict
  - Dictionary object to convert to string.

<hr>

**[Returns]**

- `value_str`: str
  - Converted string, e.g., '{"any_key": 10, "other_key": any_variable}'

## `_get_value_str_from_iterable` function docstring

Get a value string from an iterable object.<hr>

**[Parameters]**

- `value`: list or tuple or Array
  - Target iterable object.

<hr>

**[Returns]**

- `value_str`: str
  - Converted string, e.g., '[10, "Hello!", true, any_variable]'.

## `_validate_dict_key_type` function docstring

Validate whether a dictionary key type is the `int`, `str`, `float`, `bool`, `ap.Int`, `ap.String`, or `ap.Boolean`.<hr>

**[Parameters]**

- `key`: *
  - Dictionary key to validate.

<hr>

**[Raises]**

- TypeError: If a key-type isn't the `int`, `str`, `float`, `bool`, `ap.Int`, `ap.String`, or `ap.Boolean`.

## `get_copy` function docstring

Get a copy of a specified instance if it is an instance of CopyMixIn.<hr>

**[Parameters]**

- `value`: *
  - Any value to copy.

<hr>

**[Returns]**

- `copied`: *
  - Copied value. If a value is not an instance of CopyMixIn, this interface returns an argument value directly.

## `get_value_str_for_expression` function docstring

Get a value string for expression.<hr>

**[Parameters]**

- `value`: *
  - Any value to convert to string.

<hr>

**[Returns]**

- `value_str`: str
  - String for expression. If a value is an instance of VariableNameMixIn, this interface returns a variable's name. Otherwise, this interface returns a string-casted value. A bool value becomes lowercase (true or false), and this interface quotes a string value by double quotation. This interface converts a List or tuple value to a JavaScript Array expression, e.g., '[10, "Hello!", true, any_variable]'. None becomes NaN.