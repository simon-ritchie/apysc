# `apysc._validation.arg_validation_decos` docstrings

## Module summary

This module is for the argument validations' decorators. Mainly the following decorators exist. <br>・not_empty_string <br> ・Set a validation to check that the specified argument's string is not empty. <br>・handler_args_num <br> ・Set a validation to check the specified handler argument's number. <br>・handler_options_type <br> ・Set a validation to check the specified handler-options argument's type. <br>・is_event <br> ・Set a validation to check the specified argument's type is the `ap.Event` or its subclass type. <br>・is_num <br> ・Set a validation to check the specified argument's type is the number-related type. <br>・is_apysc_num <br> ・Set a validation to check the specified argument's type is the `ap.Int` or `ap.Number` type. <br>・is_integer <br> ・Set a validation to check the specified argument's type is the `int` or `ap.Int`. <br>・is_builtin_integer <br> ・Set a validation to check the specified argument's type is the built-in `int`. <br>・is_apysc_integer <br> ・Set a validation to check the specified argument's type is the `ap.Int`. <br>・is_apysc_int_or_number <br> ・Set a validation to check the specified argument's type is the `ap.Int` or `ap.Number`. <br>・is_uint8_range <br> ・Set a validation to check the specified argument's value is a range of 8-bit unsigned integer. <br>・num_is_gt_zero <br> ・Set a validation to check that the specified argument's value is greater than zero. <br>・num_is_gte_zero <br> ・Set a validation to check that the specified argument's value is greater than or equal to zero. <br>・num_is_0_to_1_range <br> ・Set a validation to check that the specified argument's value is 0.0 to 1.0 range. <br>・num_is_between <br> ・Set a validation to check whether the specified argument's value is between minimum and maximum values. <br>・variadic_args_len_is_between <br> ・Set a validation to check a variadic arguments' length is a range of minimum and maximum values. <br>・all_variadic_args_are_integers <br> ・Set a validation to check the specified variadic arguments' types are all integers. <br>・is_boolean <br> ・Set a validation to check that the specified argument's type is the `bool` or `ap.Boolean`. <br>・is_builtin_boolean <br> ・Set a validation to check that the specified argument's type is the built-in `bool`. <br>・is_apysc_boolean <br> ・Set a validation to check that the specified argument's type is the `ap.Boolean`. <br>・is_easing <br> ・Set a validation to check the specified argument's type is the `ap.Easing`. <br>・is_string <br> ・Set a validation to check the specified argument's type is the str or `ap.String`. <br>・is_builtin_string <br> ・Set a validation to check the specified argument's type is the Python built-in's `str`. <br>・is_apysc_string <br> ・Set a validation to check the specified argument's type is the `ap.String`. <br>・is_hex_color_code_format <br> ・Set a validation to check the specified argument's value is a hexadecimal color code format. <br>・is_color <br> ・Set a validation to check the specified argument's type is the `ap.Color`. <br>・are_animations <br> ・Set a validation to check the specified argument's type is the list of `ap.AnimationBase`. <br>・is_vars_dict <br> ・Set a validation to check the specified argument's value is a variables' dictionary. <br>・is_display_object <br> ・Set a validation to check the specified argument's type is the `ap.DisplayObject` or its subclass type. <br>・is_display_object_container <br> ・Set a validation to check the specified argument's type is a container of a display object instance. <br>・is_point_2d <br> ・Set a validation to check the specified argument's type is the `ap.Point2D`. <br>・are_point_2ds <br> ・Set a validation to check the specified argument's type is the list of `ap.Point2D`. <br>・is_valid_path_data_list <br> ・Set a validation to check the specified argument's type is the list of `ap.PathDataBase`. <br>・is_line_cap <br> ・Set a validation to check the specified argument's type is a line cap-related type. <br>・are_line_joints <br> ・Set a validation to check the specified argument's type is a line joints-related type. <br>・multiple_line_settings_are_not_set <br> ・Set a validation to check the specified argument's instance does not have multiple line settings. <br>・is_line_dot_setting <br> ・Set a validation to check the specified argument's type is the `ap.LineDotSetting`. <br>・is_line_dash_setting <br> ・Set a validation to check the specified argument's type is the `ap.LineDashSetting`. <br>・is_line_dash_dot_setting <br> ・Set a validation to check the specified argument's type is the `ap.LineDashDotSetting`. <br>・is_line_round_dot_setting <br> ・Set a validation to check the specified argument's type is the `ap.LineRoundDotSetting`. <br>・is_variable_name_interface_type <br> ・Set a validation to check the specified argument's type is the `ap.VariableNameMixIn` or its subclass type. <br>・is_acceptable_array_value <br> ・Set a validation to check the specified argument's type is an acceptable array value type. <br>・is_acceptable_dictionary_value <br> ・Set a validation to check the specified argument's type is an acceptable dictionary value type. <br>・is_builtin_dict <br> ・Set a validation to check the specified argument's type is the Python's `dict` type. <br>・is_apysc_dict <br> ・Set a validation to check the specified argument's type is the `ap.Dictionary` type. <br>・is_acceptable_boolean_value <br> ・Set a validation to check the specified argument's type is an acceptable boolean value type. <br>・is_fps <br> ・Set a validation to check the specified argument's value is the FPS enum. <br>・is_four_digit_year <br> ・Set a validation to check the specified argument's value is a four-digit year (full-year). <br>・is_month_int <br> ・Set a validation to check the specified argument's value is a valid month integer (1-12). <br>・is_day_int <br> ・Set a validation to check the specified argument's value is a valid day integer (1-31). <br>・is_hour_int <br> ・Set a validation to check the specified argument's value is a valid hour integer (0-23). <br>・is_minute_int <br> ・Set a validation to check the specified argument's value is a valid minute integer (0-59). <br>・is_second_int <br> ・Set a validation to check the specified argument's value is a valid second integer (0-59). <br>・is_millisecond_int <br> ・Set a validation to check the specified argument's value is a valid millisecond integer (0-999). <br>・is_apysc_datetime <br> ・Set a validation to check the specified argument's type is the apysc's `DateTime` type. <br>・is_apysc_array <br> ・Set a validation to check the specified argument's type is the `ap.Array` <br>・is_nums_array <br> ・Set a validation to check the specified `Array`'s values are all number-relate type. <br>・is_apysc_string_array <br> ・Set a validation to check the specified `Array`'s values are all apysc's `String` type. <br>・is_builtin_str_list_or_apysc_str_arr <br> ・Set a validation to check the specified argument's type is list of Python's str or Array of apysc's String. <br>・is_svg_text_align <br> ・Set a validation to check the specified argument's type is the `SvgTextAlign`. <br>・are_text_spans <br> ・Set a validation to check the specified argument's type is the list or `ap.Array` of `ap.SvgTextSpan`. <br>・is_x_axis_label_position <br> ・Set a validation to check the specified argument's type is the `XAxisLabelPosition`. <br>・is_y_axis_label_position <br> ・Set a validation to check the specified argument's type is the `YAxisLabelPosition`. <br>・is_list_or_array_matrix_data <br> ・Set a validation to check the specified argument's type is list of dicts or `ap.Array` of `ap.Dictionary`. <br>・is_initialize_with_base_value_interface_subclass <br> ・Set a validation to check the specified class is the `InitializeWithBaseValueInterface`'s subclas. <br>・is_svg_foreign_object_child <br> ・Set a validation to check the specified argument's type is the `SvgForeignObjectChild` class. <br>・is_css_text_align <br> ・Set a validation to check the specified argument's type is the `CssTextAlign` enum. <br>・is_css_text_align_last <br> ・Set a validation to check the specified argument's type is the `CssTextAlignLast`. <br>・is_fill_color_mixin <br> ・Set a validation to check the specified argument's type is the `FillColorMixIn` or its subclass type. <br>・is_svg_mask <br> ・Set a validation to check the specified argument's type is the `SvgMask`. <br>・is_fixed_html_svg_icon <br> ・Set a validation to check the specified argument's type is the `FixedHtmlSvgIconBase` or its subclass type. <br>・is_rectangle_geom <br> ・Set a validation to check the specified argument's type is the `RectangleGeom`.

## `_extract_arg_value` function docstring

Extract an argument value from the specified arguments' dictionary or list.<hr>

**[Parameters]**

- `args`: List[Any]
  - The specified positional arguments' list.
- `kwargs`: Dict[str, Any]
  - The specified keyword arguments' dictionary.'
- `arg_position_index`: int
  - A target argument position index.
- `callable_`: Callable
  - A target function or method.

<hr>

**[Returns]**

- `value`: Any
  - An extracted any value.

## `_get_arg_name_by_index` function docstring

Get an argument name from the specified argument position index.<hr>

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

## `all_variadic_args_are_integers` function docstring

Set a validation to check the specified variadic arguments' types are all integers.<hr>

**[Parameters]**

- `optional`: bool
  - A boolean, whether a target argument accepts optional None value or not.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `are_animations` function docstring

Set a validation to check the specified argument's type is the list of `ap.AnimationBase`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `are_line_joints` function docstring

Set a validation to check the specified argument's type is a line joints-related type.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.
- `optional`: bool
  - A boolean indicating whether the specified argument can be the `None`.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `are_point_2ds` function docstring

Set a validation to check the specified argument's type is the list of `ap.Point`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `are_text_spans` function docstring

Set a validation to check the specified argument's type is the list or `ap.Array` of `ap.SvgTextSpan`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `handler_args_num` function docstring

Set a validation to check the specified handler argument's number.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `handler_options_type` function docstring

Set a validation to check the specified handler-options argument's type.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_acceptable_array_value` function docstring

Set a validation to check the specified argument's type is an acceptable array value type.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_acceptable_boolean_value` function docstring

Set a validation to check the specified argument's type is an acceptable boolean value type.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_acceptable_dictionary_value` function docstring

Set a validation to check the specified argument's type is an acceptable dictionary value type.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_apysc_array` function docstring

Set a validation to check the specified argument's type is the `ap.Array`<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_apysc_boolean` function docstring

Set a validation to check that the specified argument's type is the `ap.Boolean`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_apysc_datetime` function docstring

Set a validation to check the specified argument's type is the apysc's `DateTime` type.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_apysc_dict` function docstring

Set a validation to check the specified argument's type is the `ap.Dictionary` type.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_apysc_int_or_number` function docstring

Set a validation to check the specified argument's type is the `ap.Int` or `ap.Number`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_apysc_integer` function docstring

Set a validation to check the specified argument's type is the `ap.Int`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_apysc_num` function docstring

Set a validation to check the specified argument's type is the `ap.Int` or `ap.Number` type.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_apysc_string` function docstring

Set a validation to check the specified argument's type is the `ap.String`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_apysc_string_array` function docstring

Set a validation to check the specified `Array`'s values are all apysc's `String` type.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.
- `optional`: bool, optional
  - A boolean indicating whether a target argument accepts optional None value or not.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_boolean` function docstring

Set a validation to check that the specified argument's type is the `bool` or `ap.Boolean`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.
- `optional`: bool
  - A boolean, whether a target argument accepts optional None value or not.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_builtin_boolean` function docstring

Set a validation to check that the specified argument's type is the built-in `bool`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_builtin_dict` function docstring

Set a validation to check the specified argument's type is the Python's `dict` type.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_builtin_integer` function docstring

Set a validation to check the specified argument's type is the built-in `int`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_builtin_str_list_or_apysc_str_arr` function docstring

Set a validation to check the specified argument's type is list of Python's str or Array of apysc's String.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.
- `optional`: bool
  - A boolean indicating whether a target argument accepts optional None value or not.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_builtin_string` function docstring

Set a validation to check the specified argument's type is the Python built-in's `str`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.
- `optional`: bool
  - A boolean indicating whether a target argument accepts optional None value or not.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_color` function docstring

Set a validation to check the specified argument's value is a hexadecimal color code format.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.
- `optional`: bool
  - A boolean indicating whether a target argument accepts optional None value or not.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_css_text_align` function docstring

Set a validation to check the specified argument's type is the `CssTextAlign` enum.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_css_text_align_last` function docstring

Set a validation to check the specified argument's type is the `CssTextAlignLast`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_day_int` function docstring

Set a validation to check the specified argument's value is a valid day integer (1-31).<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_display_object` function docstring

Set a validation to check the specified argument's type is the `ap.DisplayObject` or its subclass type.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_display_object_container` function docstring

Set a validation to check the specified argument's type is a container of a display object instance.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.
- `optional`: bool
  - A boolean, whether a target argument accepts optional None value or not.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_easing` function docstring

Set a validation to check the specified argument's type is the `ap.Easing`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_event` function docstring

Set a validation to check the specified argument's type is the `ap.Event` or its subclass type.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_fill_color_mixin` function docstring

Set a validation to check the specified argument's type is the `FillColorMixIn` or its subclass type.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_fixed_html_svg_icon` function docstring

Set a validation to check the specified argument's type is the `FixedHtmlSvgIconBase` or its subclass type.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.
- `optional`: bool
  - A boolean, whether a target argument accepts optional None value or not.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_four_digit_year` function docstring

Set a validation to check the specified argument's value is a four-digit year (full-year).<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_fps` function docstring

Set a validation to check the specified argument's value is the FPS enum.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_hex_color_code_format` function docstring

Set a validation to check the specified argument's value in a hexadecimal color code format.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.
- `optional`: bool
  - A boolean, whether a target argument accepts optional None value or not.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_hour_int` function docstring

Set a validation to check the specified argument's value is a valid hour integer (0-23).<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_initialize_with_base_value_interface_subclass` function docstring

Set a validation to check the specified class is the `InitializeWithBaseValueInterface`'s subclas.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.
- `optional`: bool
  - A boolean indicating whether a target argument accepts optional None value or not.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_integer` function docstring

Set a validation to check the specified argument's type is the `int` or `ap.Int`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.
- `optional`: bool
  - A boolean, whether a target argument accepts optional None value or not.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_line_cap` function docstring

Set a validation to check the specified argument's type is a line cap-related type.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.
- `optional`: bool
  - A boolean indicating whether the specified argument can be the `None`.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_line_dash_dot_setting` function docstring

Set a validation to check the specified argument's type is the `ap.LineDashDotSetting`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_line_dash_setting` function docstring

Set a validation to check the specified argument's type is the `ap.LineDashSetting`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_line_dot_setting` function docstring

Set a validation to check the specified argument's type is the `ap.LineDotSetting`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_line_round_dot_setting` function docstring

Set a validation to check the specified argument's type is the `ap.LineRoundDotSetting`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_list_or_array_matrix_data` function docstring

Set a validation to check the specified argument's type is list of dicts or `ap.Array` of `ap.Dictionary`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_millisecond_int` function docstring

Set a validation to check the specified argument's value is a valid millisecond integer (0-999).<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_minute_int` function docstring

Set a validation to check the specified argument's value is a valid minute integer (0-59).<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_month_int` function docstring

Set a validation to check the specified argument's value is a valid month integer (1-12).<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_num` function docstring

Set a validation to check the specified argument's type is the number-related type.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.
- `optional`: bool
  - A boolean, whether a target argument accepts optional None value or not.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_nums_array` function docstring

Set a validation to check the specified `Array`'s values are all number-relate type.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_point_2d` function docstring

Set a validation to check the specified argument's type is the `ap.Point2D`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_rectangle_geom` function docstring

Set a validation to check the specified argument's type is the `RectangleGeom`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_second_int` function docstring

Set a validation to check the specified argument's value is a valid second integer (0-59).<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_string` function docstring

Set a validation to check the specified argument's type is the str or `ap.String`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.
- `optional`: bool
  - A boolean, whether a target argument accepts optional None value or not.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_svg_foreign_object_child` function docstring

Set a validation to check the specified argument's type is the `SvgForeignObjectChild` class.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_svg_mask` function docstring

Set a validation to check the specified argument's type is the `SvgMask`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.
- `optional`: bool
  - A boolean, whether a target argument accepts optional None value or not.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_svg_text_align` function docstring

Set a validation to check the specified argument's type is the `SvgTextAlign`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_uint8_range` function docstring

Set a validation to check the specified argument's value is a range of unsigned integer.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_valid_path_data_list` function docstring

Set a validation to check the specified argument's type is the list of `ap.PathDataBase` and a first value is an instance of the `PathMoveTo`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_variable_name_interface_type` function docstring

Set a validation to check the specified argument's type is the `ap.VariableNameMixIn` or its subclass type.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_vars_dict` function docstring

Set a validation to check the specified argument's value is a variables' dictionary.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.
- `optional`: bool, optional
  - A boolean indicating whether a target argument accepts optional None value or not.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_x_axis_label_position` function docstring

Set a validation to check the specified argument's type is the `XAxisLabelPosition`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `is_y_axis_label_position` function docstring

Set a validation to check the specified argument's type is the `YAxisLabelPosition`.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `multiple_line_settings_are_not_set` function docstring

Set a validation to check the specified argument's instance does not have multiple line settings.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `not_empty_string` function docstring

Set a validation to check that the specified argument's string is not empty.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `num_is_0_to_1_range` function docstring

Set a validation to check that the specified argument's value is 0.0 to 1.0 range.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.
- `optional`: bool
  - A boolean, whether a target argument accepts optional None value or not.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `num_is_between` function docstring

Set a validation to check whether the specified argument's value is between minimum and maximum values.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.
- `min_value`: Union[int, float]
  - A minimum threshold value.
- `max_value`: Union[int, float]
  - A maximum threshold value.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

<hr>

**[Notes]**

This decorator only checks `int` and `float` values.

## `num_is_gt_zero` function docstring

Set a validation to check that the specified argument's value is greater than zero.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.
- `optional`: bool
  - A boolean, whether a target argument accepts optional None value or not.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `num_is_gte_zero` function docstring

Set a validation to check that the specified argument's value is greater than or equal to zero.<hr>

**[Parameters]**

- `arg_position_index`: int
  - A target argument position index.
- `optional`: bool
  - A boolean, whether a target argument accepts optional None value or not.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

## `variadic_args_len_is_between` function docstring

Set a validation to check a variadic arguments' length is a range of minimum and maximum values.<hr>

**[Parameters]**

- `min_length`: int
  - A minimum list length.
- `max_length`: int
  - A maximum list length.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.