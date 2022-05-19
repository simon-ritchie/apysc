# `apysc._validation.arg_validation_decos` docstrings

## Module summary

This module is for the argument validations' decorators. Mainly the following decorators exist. <br>・not_empty_string <br> ・Set the validation to check that a specified argument's string is not empty. <br>・handler_args_num <br> ・Set the validation to check a specified handler argument's number. <br>・handler_options_type <br> ・Set the validation to check a specified handler-options argument's type. <br>・is_integer <br> ・Set the validation to check a specified argument's type is the `int` or `ap.Int`. <br>・num_is_gt_zero <br> ・Set the validation to check that a specified argument's value is greater than zero. <br>・is_easing <br> ・Set the validation to check a specified argument's type is the `ap.Easing`.

## `_extract_arg_value` function docstring

Extract an argument value from a specified arguments' dictionary or list.<hr>

**[Parameters]**

- `args`: List[Any]
  - A specified positional arguments' list.
- `kwargs`: Dict[str, Any]
  - A specified keyword arguments' dictionary.'
- `arg_position_index`: int
  - A target argument position index.
- `arg_name`: str
  - A target argument name to check.
- `default_val`: Any
  - A default value of a target argument.

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
- `arg_name`: str
  - A target argument name.

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

- `_wrapped`: Callable
  - Wrapped callable object.

## `handler_options_type` function docstring

Set the validation to check a specified handler-options argument's type.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `_wrapped`: Callable
  - Wrapped callable object.

## `is_easing` function docstring

Set the validation to check a specified argument's type is the `ap.Easing`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `_wrapped`: Callable
  - Wrapped callable object.

## `is_integer` function docstring

Set the validation to check a specified argument's type is the `int` or `ap.Int`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `_wrapped`: Callable
  - Wrapped callable object.

## `not_empty_string` function docstring

Set the validation to check that a specified argument's string is not empty.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `_wrapped`: Callable
  - Wrapped callable object.

## `num_is_gt_zero` function docstring

Set the validation to check that a specified argument's value is greater than zero.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `_wrapped`: Callable
  - Wrapped callable object.