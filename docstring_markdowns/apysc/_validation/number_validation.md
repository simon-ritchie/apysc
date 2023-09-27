# `apysc._validation.number_validation` docstrings

## Module summary

Number validation implementations. Mainly following interfaces are defined: <br>・validate_num <br> ・Validate a specified value as an integer or float type. <br>・validate_integer <br> ・Validate whether a specified value is an integer or not. <br>・validate_builtin_integer <br> ・Validate whether a specified value is a built-in integer or not. <br>・validate_int_is_zero_or_one <br> ・Validate specified integer value is zero or one. <br>・validate_num_is_gt_zero <br> ・Validate specified value is greater than zero. <br>・validate_num_is_gte_zero <br> ・Validate whether a specified value is greater than or equal to zero. <br>・validate_num_is_0_to_1_range <br> ・Validate whether a specified number is from 0.0 to 1.0. <br>・validate_apysc_int_or_number <br> ・Validate whether a specified value is an apysc's `Int` or `Number`.

## `validate_apysc_int_or_number` function docstring

Validate whether a specified value is an apysc's `Int` or `Number`.<hr>

**[Parameters]**

- `value`: Any
  - A value to check.

<hr>

**[Returns]**

- `value`: Union[Int, Number]
  - An apysc's `Int` or `Number` value.

## `validate_builtin_integer` function docstring

Validate whether a specified value is a built-in integer or not.<hr>

**[Parameters]**

- `integer`: int
  - A target integer to check.
- `additional_err_msg`: str, optional
  - An additional error message to display.

<hr>

**[Raises]**

- ValueError: If a specified value is not a built-in integer.

## `validate_int_is_zero_or_one` function docstring

Validate specified integer value is zero or one.<hr>

**[Parameters]**

- `integer`: Int or int
  - Integer value to check.

<hr>

**[Raises]**

- ValueError: If a specified integer is not zero and one.

<hr>

**[Notes]**

This interface skips validation if an argument value is not an Int or int instance.

## `validate_integer` function docstring

Validate whether a specified value is an integer or not.<hr>

**[Parameters]**

- `integer`: Int or int
  - Integer value to check.
- `additional_err_msg`: str, optional
  - An additional error message to display.

<hr>

**[Raises]**

- ValueError: If a specified value is not an integer.

## `validate_num` function docstring

Validate a specified value as an integer or float type.<hr>

**[Parameters]**

- `num`: int or float or Int or Number
  - Number value to check.
- `additional_err_msg`: str, optional
  - An additional error message to display.

<hr>

**[Raises]**

- ValueError: If a specified value is not an integer and float value.

## `validate_num_is_0_to_1_range` function docstring

Validate whether a specified number is from 0.0 to 1.0.<hr>

**[Parameters]**

- `num`: float or Number
  - A number value to check.
- `additional_err_msg`: str, optional
  - An additional error message to display.

<hr>

**[Raises]**

- ValueError: If a specified opacity is out of the 0.0 to 1.0 range.

## `validate_num_is_gt_zero` function docstring

Validate specified value is greater than zero.<hr>

**[Parameters]**

- `num`: int or float or Int or Number
  - Number value to check.
- `additional_err_msg`: str, optional
  - An additional error message to display.

<hr>

**[Raises]**

- ValueError: If a specified value is less than or equal to zero.

## `validate_num_is_gte_zero` function docstring

Validate whether a specified value is greater than or equal to zero.<hr>

**[Parameters]**

- `num`: int or float or Int or Number
  - Number value to check.
- `additional_err_msg`: str, optional
  - An additional error message to display.

<hr>

**[Raises]**

- ValueError: If a specified value is less than zero.