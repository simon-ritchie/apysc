# `apysc._validation.arg_validation_decos` docstrings

## Module summary

This module is for the argument validations' decorators. Mainly the following decorators exist. <br>・not_empty_string <br> ・Set the validation to check that a specified argument's string is not empty. <br>・handler_args_num <br> ・Set the validation to check a specified handler argument's number. <br>・handler_options_type <br> ・Set the validation to check a specified handler-options argument's type. <br>・is_num <br> ・Set the validation to check a specified argument's type is the number-related type. <br>・is_integer <br> ・Set the validation to check a specified argument's type is the `int` or `ap.Int`. <br>・num_is_gt_zero <br> ・Set the validation to check that a specified argument's value is greater than zero. <br>・num_is_gte_zero <br> ・Set the validation to check that a specified argument's value is greater than or equal to zero. <br>・num_is_0_to_1_range <br> ・Set the validation to check that a specified argument's value is 0.0 to 1.0 range. <br>・is_apysc_boolean <br> ・Set the validation to check that a specified argument's type is the `ap.Boolean`. <br>・is_easing <br> ・Set the validation to check a specified argument's type is the `ap.Easing`. <br>・is_hex_color_code_format <br> ・Set the validation to check a specified argument's value is a hexadecimal color code format. <br>・is_animations <br> ・Set the validation to check a specified argument's type is the list of `ap.AnimationBase`. <br>・is_vars_dict <br> ・Set the validation to check a specified argument's value is a variables' dictionary.

## `_extract_arg_value` function docstring

Extract an argument value from a specified arguments' dictionary or list.<hr>

**[Parameters]**

- `args`: List[Any]
  - A specified positional arguments' list.
- `kwargs`: Dict[str, Any]
  - A specified keyword arguments' dictionary.'
- `arg_position_index`: int
  - A target argument position index.
- `callable_`: Callable
  - A target function or method.

<hr>

**[Returns]**

- `value`: Any
  - An extracted any value.

## `_get_arg_name_by_index` function docstring

Get an argument name from a specified argument position index.<hr>

**[Parameters]**

- `callable_`: Callable
  - A target function or method.
- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `arg_name`: str
  - A target argument name.

## `_get_callable_and_arg_names_msg` function docstring

Get a function or method and argument names' message for an additional error message.<hr>

**[Parameters]**

- `callable_`: Callable
  - A target function or method.
- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `callable_and_arg_names_msg`: str
  - A function or method and argument names' message.

## `_get_default_val_by_arg_name` function docstring

Get a default value of a given name's argument.<hr>

**[Parameters]**

- `callable_`: Callable
  - A target function or method.
- `arg_name`: str
  - A target argument name.

<hr>

**[Returns]**

- `default_val`: Any
  - A default value of a given name's argument.

## `handler_args_num` function docstring

Set the validation to check a specified handler argument's number.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `handler_options_type` function docstring

Set the validation to check a specified handler-options argument's type.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_animations` function docstring

Set the validation to check a specified argument's type is the list of `ap.AnimationBase`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_apysc_boolean` function docstring

Set the validation to check that a specified argument's type is the `ap.Boolean`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_easing` function docstring

Set the validation to check a specified argument's type is the `ap.Easing`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_hex_color_code_format` function docstring

Set the validation to check a specified argument's value in a hexadecimal color code format.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_integer` function docstring

Set the validation to check a specified argument's type is the `int` or `ap.Int`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_num` function docstring

Set the validation to check a specified argument's type is the number-related type.<hr>

**[Parameters]**

- `arg_position_index`: int
  - _description_

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_vars_dict` function docstring

Set the validation to check a specified argument's value is a variables' dictionary.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.
- `optional`: bool, optional
  - A boolean indicating whether a target argument accepts optional None value or not.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `not_empty_string` function docstring

Set the validation to check that a specified argument's string is not empty.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `num_is_0_to_1_range` function docstring

Set the validation to check that a specified argument's value is 0.0 to 1.0 range.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `num_is_gt_zero` function docstring

Set the validation to check that a specified argument's value is greater than zero.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `num_is_gte_zero` function docstring

Set the validation to check that a specified argument's value is greater than or equal to zero.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.