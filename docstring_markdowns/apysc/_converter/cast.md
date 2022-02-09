# `apysc._converter.cast` docstrings

## Module summary

Implementation of common cast conversion. Mainly following interfaces are defined. <br>・to_int_from_float Convert float value to int. <br>・to_float_from_int Convert int value to float. <br>・to_bool_from_int Convert int value to bool.

## `to_bool_from_int` function docstring

Convert int value to bool.<hr>

**[Parameters]**

- `integer`: int or Int
  - Integer value to convert.

<hr>

**[Returns]**

- `bool_val`: bool
  - Converted boolean value.

<hr>

**[Raises]**

- ValueError: If argument value isn't zero or one.

## `to_float_from_int` function docstring

Convert int value to float.<hr>

**[Parameters]**

- `int_or_float`: int or float or Int or Number
  - Target integer value. If float is specified, conversion will be skipped.

<hr>

**[Returns]**

- `float_val`: float or Number
  - Converted float value.

## `to_int_from_float` function docstring

Convert float value to int.<hr>

**[Parameters]**

- `int_or_float`: int or float or Int or Number
  - Target float value. If integer is specified, conversion will be skipped.

<hr>

**[Returns]**

- `int_val`: int or Int
  - Converted integer value.