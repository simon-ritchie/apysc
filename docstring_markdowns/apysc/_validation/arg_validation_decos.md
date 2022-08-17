# `apysc._validation.arg_validation_decos` docstrings

## Module summary

This module is for the argument validations' decorators. Mainly the following decorators exist. <br>・not_empty_string <br> ・Set the validation to check that a specified argument's string is not empty. <br>・handler_args_num <br> ・Set the validation to check a specified handler argument's number. <br>・handler_options_type <br> ・Set the validation to check a specified handler-options argument's type. <br>・in_handler_assignment <br> ・Set the validation to check whether there isn't an assignment of the basic type values (e.g., ap.Int, ap.String) in a specified handler's source. <br>・is_event <br> ・Set the validation to check a specified argument's type is the `ap.Event` or its subclass type. <br>・is_num <br> ・Set the validation to check a specified argument's type is the number-related type. <br>・is_apysc_num <br> ・Set the validation to check a specified argument's type is the `ap.Int` or `ap.Number` type. <br>・is_integer <br> ・Set the validation to check a specified argument's type is the `int` or `ap.Int`. <br>・is_builtin_integer <br> ・Set the validation to check a specified argument's type is the built-in `int`. <br>・is_apysc_integer <br> ・Set the validation to check a specified argument's type is the `ap.Int`. <br>・num_is_gt_zero <br> ・Set the validation to check that a specified argument's value is greater than zero. <br>・num_is_gte_zero <br> ・Set the validation to check that a specified argument's value is greater than or equal to zero. <br>・num_is_0_to_1_range <br> ・Set the validation to check that a specified argument's value is 0.0 to 1.0 range. <br>・is_boolean <br> ・Set the validation to check that a specified argument's type is the `bool` or `ap.Boolean`. <br>・is_builtin_boolean <br> ・Set the validation to check that a specified argument's type is the built-in `bool`. <br>・is_apysc_boolean <br> ・Set the validation to check that a specified argument's type is the `ap.Boolean`. <br>・is_easing <br> ・Set the validation to check a specified argument's type is the `ap.Easing`. <br>・is_string <br> ・Set the validation to check a specified argument's type is the str or `ap.String`. <br>・is_builtin_string <br> ・Set the validation to check a specified argument's type is the Python built-in's `str`. <br>・is_hex_color_code_format <br> ・Set the validation to check a specified argument's value is a hexadecimal color code format. <br>・is_animations <br> ・Set the validation to check a specified argument's type is the list of `ap.AnimationBase`. <br>・is_vars_dict <br> ・Set the validation to check a specified argument's value is a variables' dictionary. <br>・is_display_object <br> ・Set the validation to check a specified argument's type is the `ap.DisplayObject` or its subclass type. <br>・is_display_object_container <br> ・Set the validation to check a specified argument's type is a container of a display object instance. <br>・is_point_2d <br> ・Set the validation to check a specified argument's type is the `ap.Point2D`. <br>・is_point_2ds <br> ・Set the validation to check a specified argument's type is the list of `ap.Point2D`. <br>・is_path_data_list <br> ・Set the validation to check a specified argument's type is the list of `ap.PathDataBase`. <br>・is_line_cap <br> ・Set the validation to check a specified argument's type is a line cap-related type. <br>・is_line_joints <br> ・Set the validation to check a specified argument's type is a line joints-related type. <br>・multiple_line_settings_are_not_set <br> ・Set the validation to check a specified argument's instance does not have multiple line settings. <br>・is_line_dot_setting <br> ・Set the validation to check a specified argument's type is the `ap.LineDotSetting`. <br>・is_line_dash_setting <br> ・Set the validation to check a specified argument's type is the `ap.LineDashSetting`. <br>・is_line_dash_dot_setting <br> ・Set the validation to check a specified argument's type is the `ap.LineDashDotSetting`. <br>・is_line_round_dot_setting <br> ・Set the validation to check a specified argument's type is the `ap.LineRoundDotSetting`. <br>・is_variable_name_interface_type <br> ・Set the validation to check a specified argument's type is the `ap.VariableNameInterface` or its subclass type. <br>・is_acceptable_array_value <br> ・Set the validation to check a specified argument's type is an acceptable array value type. <br>・is_acceptable_dictionary_value <br> ・Set the validation to check a specified argument's type is an acceptable dictionary value type. <br>・is_acceptable_boolean_value <br> ・Set the validation to check a specified argument's type is an acceptable boolean value type.

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

## `in_handler_assignment` function docstring

Set the validation to check whether there isn't assignment of the basic type values (e.g., ap.Int, ap.String) in a specified handler's source.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_acceptable_array_value` function docstring

Set the validation to check a specified argument's type is an acceptable array value type.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_acceptable_boolean_value` function docstring

Set the validation to check a specified argument's type is an acceptable boolean value type.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_acceptable_dictionary_value` function docstring

Set the validation to check a specified argument's type is an acceptable dictionary value type.<hr>

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

## `is_apysc_integer` function docstring

Set the validation to check a specified argument's type is the `ap.Int`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_apysc_num` function docstring

Set the validation to check a specified argument's type is the `ap.Int` or `ap.Number` type.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_boolean` function docstring

Set the validation to check that a specified argument's type is the `bool` or `ap.Boolean`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_builtin_boolean` function docstring

Set the validation to check that a specified argument's type is the built-in `bool`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_builtin_integer` function docstring

Set the validation to check a specified argument's type is the built-in `int`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_builtin_string` function docstring

Set the validation to check a specified argument's type is the Python built-in's `str`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.
- `optional`: bool, optional
  - A boolean indicating whether a target argument accepts optional None value or not.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_display_object` function docstring

Set the validation to check a specified argument's type is the `ap.DisplayObject` or its subclass type.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_display_object_container` function docstring

Set the validation to check a specified argument's type is a container of a display object instance.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.
- `optional`: bool, optional
  - A boolean indicating whether a target argument accepts optional None value or not.

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

## `is_event` function docstring

Set the validation to check a specified argument's type is the `ap.Event` or its subclass type.<hr>

**[Parameters]**

- `arg_position_index`: int
  - _description_

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

## `is_line_cap` function docstring

Set the validation to check a specified argument's type is a line cap-related type.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.
- `optional`: bool
  - A boolean indicating whether a specified argument can be the `None`.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_line_dash_dot_setting` function docstring

Set the validation to check a specified argument's type is the `ap.LineDashDotSetting`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_line_dash_setting` function docstring

Set the validation to check a specified argument's type is the `ap.LineDashSetting`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_line_dot_setting` function docstring

Set the validation to check a specified argument's type is the `ap.LineDotSetting`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_line_joints` function docstring

Set the validation to check a specified argument's type is a line joints-related type.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.
- `optional`: bool
  - A boolean indicating whether a specified argument can be the `None`.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_line_round_dot_setting` function docstring

Set the validation to check a specified argument's type is the `ap.LineRoundDotSetting`.<hr>

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

## `is_path_data_list` function docstring

Set the validation to check a specified argument's type is the list of `ap.PathDataBase`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_point_2d` function docstring

Set the validation to check a specified argument's type is the `ap.Point2D`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_point_2ds` function docstring

Set the validation to check a specified argument's type is the list of `ap.Point`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_string` function docstring

Set the validation to check a specified argument's type is the str or `ap.String`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_variable_name_interface_type` function docstring

Set the validation to check a specified argument's type is the `ap.VariableNameInterface` or its subclass type.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

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

## `multiple_line_settings_are_not_set` function docstring

Set the validation to check a specified argument's instance does not have multiple line settings.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

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