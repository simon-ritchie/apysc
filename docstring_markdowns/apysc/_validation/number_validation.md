# apysc._validation.number_validation docstrings

## Module summary

Number validation implementations. Mainly following interfaces are defined: <br>・validate_num Validate specified value is integer or float type. <br>・validate_integer Validate specified value is integer. <br>・validate_int_is_zero_or_one Validate specified integer value is zero or one. <br>・validate_num_is_gt_zero Validate specified value is greater than zero. <br>・validate_num_is_gte_zero Validate specified value is greater than or equal to zero. <br>・validate_nums_are_int_and_gt_zero Validate specified number values are greater integer and greater than zero.

## validate_int_is_zero_or_one function docstring

Validate specified integer value is zero or one.<hr>

**[Parameters]**

- `integer`: int or Int
  - Integer value to check.

<hr>

**[Raises]**

- ValueError: If specified integer is not zero and one.

<hr>

**[Notes]**

If argument value is not int or Int instance, then validation will be skipped.

## validate_integer function docstring

Validate specified value is integer.<hr>

**[Parameters]**

- `integer`: int or Int
  - Integer value to check.

<hr>

**[Raises]**

- ValueError: If specified value is not integer.

## validate_num function docstring

Validate specified value is integer or float type.<hr>

**[Parameters]**

- `num`: int or float or Int or Number
  - Number value to check.

<hr>

**[Raises]**

- ValueError: If specified value is not integer and float value.

## validate_num_is_gt_zero function docstring

Validate specified value is greater than zero.<hr>

**[Parameters]**

- `num`: int or float or Int or Number
  - Number value to check.

<hr>

**[Raises]**

- ValueError: If specified value is less than or equal to zero.

## validate_num_is_gte_zero function docstring

Validate specified value is greater than or equal to zero.<hr>

**[Parameters]**

- `num`: int or float or Int or Number
  - Number value to check.

<hr>

**[Raises]**

- ValueError: If specified value is less than zero.

## validate_nums_are_int_and_gt_zero function docstring

Validate specified number values are greater integer and greater than zero.<hr>

**[Parameters]**

- `nums`: list
  - Integer values to check.

<hr>

**[Raises]**

- ValueError: If any value is not integer type or less than one.