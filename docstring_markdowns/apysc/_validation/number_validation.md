# `apysc._validation.number_validation` docstrings

## Module summary

Number validation implementations. Mainly following interfaces are defined: <br>・validate_num Validate specified value is integer or float type. <br>・validate_integer Validate specified value is integer. <br>・validate_int_is_zero_or_one Validate specified integer value is zero or one. <br>・validate_num_is_gt_zero Validate specified value is greater than zero. <br>・validate_num_is_gte_zero Validate specified value is greater than or equal to zero. <br>・validate_nums_are_int_and_gt_zero Validate specified number values are greater integer and greater than zero.

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

<hr>

**[Raises]**

- ValueError: If a specified value is not an integer.

## `validate_num` function docstring

Validate a specified value is an integer or float type.<hr>

**[Parameters]**

- `num`: int or float or Int or Number
  - Number value to check.

<hr>

**[Raises]**

- ValueError: If specified value is not an integer and float value.

## `validate_num_is_gt_zero` function docstring

Validate specified value is greater than zero.<hr>

**[Parameters]**

- `num`: int or float or Int or Number
  - Number value to check.

<hr>

**[Raises]**

- ValueError: If specified value is less than or equal to zero.

## `validate_num_is_gte_zero` function docstring

Validate whether a specified value is greater than or equal to zero.<hr>

**[Parameters]**

- `num`: int or float or Int or Number
  - Number value to check.

<hr>

**[Raises]**

- ValueError: If specified value is less than zero.

## `validate_nums_are_int_and_gt_zero` function docstring

Validate specified number values are greater integer and greater than zero.<hr>

**[Parameters]**

- `nums`: list
  - Integer values to check.

<hr>

**[Raises]**

- ValueError: If any value is not integer type or less than one.