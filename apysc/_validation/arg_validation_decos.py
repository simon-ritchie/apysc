# mypy: disable-error-code=type-var

"""This module is for the argument validations' decorators.

Mainly the following decorators exist.

- not_empty_string
    - Set a validation to check that the specified argument's string
        is not empty.
- handler_args_num
    - Set a validation to check the specified handler argument's
        number.
- handler_options_type
    - Set a validation to check the specified handler-options
        argument's type.
- is_event
    - Set a validation to check the specified argument's type
        is the `ap.Event` or its subclass type.
- is_num
    - Set a validation to check the specified argument's type
        is the number-related type.
- is_apysc_num
    - Set a validation to check the specified argument's type
        is the `ap.Int` or `ap.Number` type.
- is_integer
    - Set a validation to check the specified argument's type
        is the `int` or `ap.Int`.
- is_builtin_integer
    - Set a validation to check the specified argument's type
        is the built-in `int`.
- is_apysc_integer
    - Set a validation to check the specified argument's type
        is the `ap.Int`.
- is_apysc_int_or_number
    - Set a validation to check the specified argument's type
        is the `ap.Int` or `ap.Number`.
- is_uint8_range
    - Set a validation to check the specified argument's value
        is a range of 8-bit unsigned integer.
- num_is_gt_zero
    - Set a validation to check that the specified argument's value
        is greater than zero.
- num_is_gte_zero
    - Set a validation to check that the specified argument's value
        is greater than or equal to zero.
- num_is_0_to_1_range
    - Set a validation to check that the specified argument's value
        is 0.0 to 1.0 range.
- num_is_between
    - Set a validation to check whether the specified argument's value
        is between minimum and maximum values.
- variadic_args_len_is_between
    - Set a validation to check a variadic arguments' length is
        a range of minimum and maximum values.
- all_variadic_args_are_integers
    - Set a validation to check the specified variadic arguments'
        types are all integers.
- is_boolean
    - Set a validation to check that the specified argument's type
        is the `bool` or `ap.Boolean`.
- is_builtin_boolean
    - Set a validation to check that the specified argument's type
        is the built-in `bool`.
- is_apysc_boolean
    - Set a validation to check that the specified argument's type
        is the `ap.Boolean`.
- is_easing
    - Set a validation to check the specified argument's type
        is the `ap.Easing`.
- is_string
    - Set a validation to check the specified argument's type
        is the str or `ap.String`.
- is_builtin_string
    - Set a validation to check the specified argument's type
        is the Python built-in's `str`.
- is_apysc_string
    - Set a validation to check the specified argument's type
        is the `ap.String`.
- is_hex_color_code_format
    - Set a validation to check the specified argument's value
        is a hexadecimal color code format.
- is_color
    - Set a validation to check the specified argument's type
        is the `ap.Color`.
- are_animations
    - Set a validation to check the specified argument's type
        is the list of `ap.AnimationBase`.
- is_vars_dict
    - Set a validation to check the specified argument's value
        is a variables' dictionary.
- is_display_object
    - Set a validation to check the specified argument's type
        is the `ap.DisplayObject` or its subclass type.
- is_display_object_container
    - Set a validation to check the specified argument's type
        is a container of a display object instance.
- is_point_2d
    - Set a validation to check the specified argument's type
        is the `ap.Point2D`.
- are_point_2ds
    - Set a validation to check the specified argument's type
        is the list of `ap.Point2D`.
- is_valid_path_data_list
    - Set a validation to check the specified argument's type
        is the list of `ap.PathDataBase`.
- is_line_cap
    - Set a validation to check the specified argument's type
        is a line cap-related type.
- are_line_joints
    - Set a validation to check the specified argument's type
        is a line joints-related type.
- multiple_line_settings_are_not_set
    - Set a validation to check the specified argument's instance
        does not have multiple line settings.
- is_line_dot_setting
    - Set a validation to check the specified argument's type
        is the `ap.LineDotSetting`.
- is_line_dash_setting
    - Set a validation to check the specified argument's type
        is the `ap.LineDashSetting`.
- is_line_dash_dot_setting
    - Set a validation to check the specified argument's type
        is the `ap.LineDashDotSetting`.
- is_line_round_dot_setting
    - Set a validation to check the specified argument's type
        is the `ap.LineRoundDotSetting`.
- is_variable_name_interface_type
    - Set a validation to check the specified argument's type
        is the `ap.VariableNameMixIn` or its subclass type.
- is_acceptable_array_value
    - Set a validation to check the specified argument's type
        is an acceptable array value type.
- is_acceptable_dictionary_value
    - Set a validation to check the specified argument's type
        is an acceptable dictionary value type.
- is_builtin_dict
    - Set a validation to check the specified argument's type
        is the Python's `dict` type.
- is_apysc_dict
    - Set a validation to check the specified argument's type
        is the `ap.Dictionary` type.
- is_acceptable_boolean_value
    - Set a validation to check the specified argument's type
        is an acceptable boolean value type.
- is_fps
    - Set a validation to check the specified argument's value
        is the FPS enum.
- is_four_digit_year
    - Set a validation to check the specified argument's value
        is a four-digit year (full-year).
- is_month_int
    - Set a validation to check the specified argument's value
        is a valid month integer (1-12).
- is_day_int
    - Set a validation to check the specified argument's value
        is a valid day integer (1-31).
- is_hour_int
    - Set a validation to check the specified argument's value
        is a valid hour integer (0-23).
- is_minute_int
    - Set a validation to check the specified argument's value
        is a valid minute integer (0-59).
- is_second_int
    - Set a validation to check the specified argument's value
        is a valid second integer (0-59).
- is_millisecond_int
    - Set a validation to check the specified argument's value
        is a valid millisecond integer (0-999).
- is_apysc_datetime
    - Set a validation to check the specified argument's type
        is the apysc's `DateTime` type.
- is_apysc_array
    - Set a validation to check the specified argument's type
        is the `ap.Array`
- is_nums_array
    - Set a validation to check the specified `Array`'s values
        are all number-relate type.
- is_apysc_string_array
    - Set a validation to check the specified `Array`'s values
        are all apysc's `String` type.
- is_builtin_str_list_or_apysc_str_arr
    - Set a validation to check the specified argument's type
        is list of Python's str or Array of apysc's String.
- is_svg_text_align
    - Set a validation to check the specified argument's type
        is the `SvgTextAlign`.
- are_text_spans
    - Set a validation to check the specified argument's type
        is the list or `ap.Array` of `ap.SvgTextSpan`.
- is_x_axis_label_position
    - Set a validation to check the specified argument's type
        is the `XAxisLabelPosition`.
- is_y_axis_label_position
    - Set a validation to check the specified argument's type
        is the `YAxisLabelPosition`.
- is_list_or_array_matrix_data
    - Set a validation to check the specified argument's type
        is list of dicts or `ap.Array` of `ap.Dictionary`.
- is_initialize_with_base_value_interface_subclass
    - Set a validation to check the specified class is
        the `InitializeWithBaseValueInterface`'s subclas.
- is_svg_foreign_object_child
    - Set a validation to check the specified argument's type
        is the `SvgForeignObjectChild` class.
- is_css_text_align
    - Set a validation to check the specified argument's type
        is the `CssTextAlign` enum.
- is_css_text_align_last
    - Set a validation to check the specified argument's type
        is the `CssTextAlignLast`.
"""

import functools
import inspect
from inspect import Signature
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Tuple
from typing import TypeVar
from typing import Union

# pyright: reportInvalidTypeVarUse=false
_Callable = TypeVar("_Callable", bound=Callable)


def _extract_arg_value(
    *, args: Any, kwargs: Dict[str, Any], arg_position_index: int, callable_: Callable
) -> Any:
    """
    Extract an argument value from the specified arguments' dictionary
    or list.

    Parameters
    ----------
    args : List[Any]
        The specified positional arguments' list.
    kwargs : Dict[str, Any]
        The specified keyword arguments' dictionary.'
    arg_position_index : int
        A target argument position index.
    callable_ : Callable
        A target function or method.

    Returns
    -------
    value : Any
        An extracted any value.
    """
    value: Any = None
    arg_name: str = _get_arg_name_by_index(
        callable_=callable_, arg_position_index=arg_position_index
    )
    default_val: Any = _get_default_val_by_arg_name(
        callable_=callable_, arg_name=arg_name
    )
    if arg_name in kwargs:
        value = kwargs[arg_name]
    elif len(args) - 1 >= arg_position_index:
        value = args[arg_position_index]
    if value is None and default_val is not None:
        return default_val
    return value


def _get_arg_name_by_index(*, callable_: Callable, arg_position_index: int) -> str:
    """
    Get an argument name from the specified argument position index.

    Parameters
    ----------
    callable_ : Callable
        A target function or method.
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    arg_name : str
        A target argument name.
    """
    signature: Signature = inspect.signature(callable_)
    if len(signature.parameters) - 1 < arg_position_index:
        raise IndexError(
            "The specified function has no argument parameter "
            f"at the index of {arg_position_index}"
            f"\nActual argument length: {len(signature.parameters)}"
        )
    arg_name: str = ""
    for i, (arg_name_, _) in enumerate(signature.parameters.items()):
        if i == arg_position_index:
            arg_name = arg_name_
    return arg_name


def _get_callable_and_arg_names_msg(
    *, callable_: Callable, arg_position_index: int
) -> str:
    """
    Get a function or method and argument names' message
    for an additional error message.

    Parameters
    ----------
    callable_ : Callable
        A target function or method.
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    callable_and_arg_names_msg : str
        A function or method and argument names' message.
    """
    arg_name: str = _get_arg_name_by_index(
        callable_=callable_, arg_position_index=arg_position_index
    )
    callable_and_arg_names_msg: str = (
        f"Target callable name: {callable_.__name__}"
        f"\nTarget argument name: {arg_name}"
    )
    return callable_and_arg_names_msg


def _get_default_val_by_arg_name(*, callable_: Callable, arg_name: str) -> Any:
    """
    Get a default value of a given name's argument.

    Parameters
    ----------
    callable_ : Callable
        A target function or method.
    arg_name : str
        A target argument name.

    Returns
    -------
    default_val : Any
        A default value of a given name's argument.
    """
    default_val: Any = None
    signature: Signature = inspect.signature(callable_)
    for target_arg_name, parameter in signature.parameters.items():
        if target_arg_name != arg_name:
            continue
        default_val = parameter.default
        break
    if default_val == inspect.Signature.empty:
        return None
    return default_val


def not_empty_string(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check that the specified argument's string
    is not empty.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.string_validation import validate_not_empty_string

            string: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_not_empty_string(
                string=string,
                additional_err_msg=(
                    "An argument's string value must not be empty."
                    f"\n{callable_and_arg_names_msg}"
                ),
            )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def handler_args_num(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified handler argument's
    number.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.handler_validation import validate_handler_args_num

            handler: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_handler_args_num(
                handler=handler, additional_err_msg=callable_and_arg_names_msg
            )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def handler_options_type(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified handler-options
    argument's type.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.handler_validation import validate_options_type

            options: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_options_type(
                options=options, additional_err_msg=callable_and_arg_names_msg
            )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_event(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the `ap.Event` or its subclass type.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.event_validation import validate_event

            event: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_event(e=event, additional_err_msg=callable_and_arg_names_msg)

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_num(*, arg_position_index: int, optional: bool) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the number-related type.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.
    optional : bool
        A boolean, whether a target argument accepts
        optional None value or not.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.number_validation import validate_num

            num: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            if optional and num is None:
                return callable_(*args, **kwargs)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_num(num=num, additional_err_msg=callable_and_arg_names_msg)

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_apysc_num(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the `ap.Int` or `ap.Number` type.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._type.number_value_mixin import NumberValueMixIn

            num: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            if not isinstance(num, NumberValueMixIn):
                raise TypeError(
                    "The specified argument value is not `ap.Int` or "
                    f"`ap.Number` type: {type(num)}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_integer(*, arg_position_index: int, optional: bool) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the `int` or `ap.Int`.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.
    optional : bool
        A boolean, whether a target argument accepts
        optional None value or not.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.number_validation import validate_integer

            integer: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            if optional and integer is None:
                return callable_(*args, **kwargs)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_integer(
                integer=integer, additional_err_msg=callable_and_arg_names_msg
            )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_builtin_integer(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the built-in `int`.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.number_validation import validate_builtin_integer

            integer: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_builtin_integer(
                integer=integer, additional_err_msg=callable_and_arg_names_msg
            )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_apysc_integer(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the `ap.Int`.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._type.int import Int

            integer: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            if not isinstance(integer, Int):
                raise TypeError(
                    "The specified argument value is not `ap.Int` "
                    f"type: {type(integer)}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_apysc_int_or_number(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the `ap.Int` or `ap.Number`.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._type.int import Int
            from apysc._type.number import Number

            int_or_number: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            if not isinstance(int_or_number, (Int, Number)):
                callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                    callable_=callable_, arg_position_index=arg_position_index
                )
                raise TypeError(
                    f"The specified argument is not `ap.Int` or `ap.Number` type: "
                    f"{type(int_or_number).__name__}, {int_or_number}"
                    f"\n{callable_and_arg_names_msg}"
                )
            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_uint8_range(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's value
    is a range of unsigned integer.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._type.int import Int

            integer: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            if not isinstance(integer, (int, Int)):
                raise TypeError(
                    "The specified argument value is not an integer type: "
                    f"{type(integer).__name__}\n{callable_and_arg_names_msg}"
                )
            py_int: int = 0
            if isinstance(integer, int):
                py_int = integer
            elif isinstance(integer, Int):
                py_int = integer._value
            under_or_overflow_err_msg: str = (
                "The specified argument value is less than zero "
                f"(range of 0 to 255 is acceptable): {py_int}"
            )
            if py_int < 0:
                raise ValueError(under_or_overflow_err_msg)
            if py_int > 255:
                raise ValueError(under_or_overflow_err_msg)
            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def num_is_gt_zero(*, arg_position_index: int, optional: bool) -> _Callable:
    """
    Set a validation to check that the specified argument's value
    is greater than zero.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.
    optional : bool
        A boolean, whether a target argument accepts
        optional None value or not.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.number_validation import validate_num_is_gt_zero

            num: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            if optional and num is None:
                return callable_(*args, **kwargs)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_num_is_gt_zero(
                num=num, additional_err_msg=callable_and_arg_names_msg
            )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def num_is_gte_zero(*, arg_position_index: int, optional: bool) -> _Callable:
    """
    Set a validation to check that the specified argument's value
    is greater than or equal to zero.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.
    optional : bool
        A boolean, whether a target argument accepts
        optional None value or not.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.number_validation import validate_num_is_gte_zero

            num: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            if optional and num is None:
                return callable_(*args, **kwargs)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_num_is_gte_zero(
                num=num, additional_err_msg=callable_and_arg_names_msg
            )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def num_is_0_to_1_range(*, arg_position_index: int, optional: bool) -> _Callable:
    """
    Set a validation to check that the specified argument's value
    is 0.0 to 1.0 range.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.
    optional : bool
        A boolean, whether a target argument accepts
        optional None value or not.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.number_validation import validate_num_is_0_to_1_range

            num: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            if optional and num is None:
                return callable_(*args, **kwargs)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_num_is_0_to_1_range(
                num=num, additional_err_msg=callable_and_arg_names_msg
            )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def num_is_between(
    *,
    arg_position_index: int,
    min_value: Union[int, float],
    max_value: Union[int, float],
) -> _Callable:
    """
    Set a validation to check whether the specified argument's value
    is between minimum and maximum values.

    Notes
    -----
    This decorator only checks `int` and `float` values.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.
    min_value : Union[int, float]
        A minimum threshold value.
    max_value : Union[int, float]
        A maximum threshold value.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            num: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            if isinstance(num, (int, float)):
                callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                    callable_=callable_, arg_position_index=arg_position_index
                )
                if num < min_value:
                    raise ValueError(
                        f"The specified argument value ({num}) is "
                        f"less than {min_value}."
                        f"\n{callable_and_arg_names_msg}"
                    )
                if num > max_value:
                    raise ValueError(
                        f"The specified argument value ({num}) is greater than "
                        f"{max_value}.\n{callable_and_arg_names_msg}"
                    )
            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def variadic_args_len_is_between(
    *,
    min_length: int,
    max_length: int,
) -> _Callable:
    """
    Set a validation to check a variadic arguments' length is
    a range of minimum and maximum values.

    Parameters
    ----------
    min_length : int
        A minimum list length.
    max_length : int
        A maximum list length.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            args_len: int = len(args)
            if args_len < min_length:
                raise ValueError(
                    "The specified variadic argument's length is less than "
                    f"{min_length}.\nActual length: {args_len}"
                )
            if args_len > max_length:
                raise ValueError(
                    "The specified variadic argument's length is greater than "
                    f"{max_length}.\nActual length: {args_len}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def all_variadic_args_are_integers(*, optional: bool) -> _Callable:
    """
    Set a validation to check the specified variadic arguments'
    types are all integers.

    Parameters
    ----------
    optional : bool
        A boolean, whether a target argument accepts
        optional None value or not.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._type.int import Int

            for arg in args:
                if optional and arg is None:
                    continue
                if isinstance(arg, (int, Int)):
                    continue
                raise TypeError(
                    "The specified variadic argument value is not `int` or "
                    f"`ap.Int`: {type(arg)}, {arg}"
                )
            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_boolean(*, arg_position_index: int, optional: bool) -> _Callable:
    """
    Set a validation to check that the specified argument's type
    is the `bool` or `ap.Boolean`.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.
    optional : bool
        A boolean, whether a target argument accepts
        optional None value or not.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.bool_validation import validate_bool

            boolean: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            if optional and boolean is None:
                return callable_(*args, **kwargs)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_bool(value=boolean, additional_err_msg=callable_and_arg_names_msg)

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_builtin_boolean(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check that the specified argument's type
    is the built-in `bool`.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.bool_validation import validate_builtin_bool

            boolean: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_builtin_bool(
                value=boolean, additional_err_msg=callable_and_arg_names_msg
            )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_apysc_boolean(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check that the specified argument's type
    is the `ap.Boolean`.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._type.boolean import Boolean

            boolean: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            if not isinstance(boolean, Boolean):
                raise TypeError(
                    "The specified argument value is not a `Boolean` type: "
                    f"{type(boolean)}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_easing(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the `ap.Easing`.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._animation.easing import Easing

            easing: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            if not isinstance(easing, Easing):
                raise TypeError(
                    "The specified easing argument's type is not the "
                    f"ap.Easing: {type(easing)}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_string(*, arg_position_index: int, optional: bool) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the str or `ap.String`.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.
    optional : bool
        A boolean, whether a target argument accepts
        optional None value or not.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.string_validation import validate_string_type

            string: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            if optional and string is None:
                return callable_(*args, **kwargs)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_string_type(
                string=string, additional_err_msg=callable_and_arg_names_msg
            )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_builtin_string(*, arg_position_index: int, optional: bool) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the Python built-in's `str`.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.
    optional : bool
        A boolean indicating whether a target argument accepts
        optional None value or not.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.string_validation import validate_builtin_string_type

            string: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            if not optional:
                validate_builtin_string_type(
                    string=string, additional_err_msg=callable_and_arg_names_msg
                )
            elif string is not None:
                validate_builtin_string_type(
                    string=string, additional_err_msg=callable_and_arg_names_msg
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_apysc_string(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the `ap.String`.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._type.string import String

            string: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            if not isinstance(string, String):
                callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                    callable_=callable_, arg_position_index=arg_position_index
                )
                raise TypeError(
                    "the specified argument's type is not the "
                    f"ap.String: {type(string)}"
                    f"\n{callable_and_arg_names_msg}"
                )
            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_hex_color_code_format(*, arg_position_index: int, optional: bool) -> _Callable:
    """
    Set a validation to check the specified argument's value
    in a hexadecimal color code format.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.
    optional : bool
        A boolean, whether a target argument accepts
        optional None value or not.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._color import color_util
            from apysc._validation.color_validation import (
                validate_hex_color_code_format,
            )

            hex_color_code: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            if optional and hex_color_code is None:
                return callable_(*args, **kwargs)

            hex_color_code = color_util.remove_color_code_sharp_symbol(
                hex_color_code=hex_color_code
            )
            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_hex_color_code_format(
                hex_color_code=hex_color_code,
                additional_err_msg=callable_and_arg_names_msg,
            )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_color(*, arg_position_index: int, optional: bool) -> _Callable:
    """
    Set a validation to check the specified argument's value
    is a hexadecimal color code format.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.
    optional : bool
        A boolean indicating whether a target argument accepts
        optional None value or not.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._color.color import Color

            color: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            if optional and color is None:
                return callable_(*args, **kwargs)
            if not isinstance(color, Color):
                raise TypeError(
                    "the specified argument's type is not the ap.Color: "
                    f"{type(color).__name__}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def are_animations(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the list of `ap.AnimationBase`.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._animation.animation_base import AnimationBase

            animations: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )

            if not isinstance(animations, list):
                raise TypeError(
                    "The specified animations list must be a list: "
                    f"{type(animations)}"
                    f"\n{callable_and_arg_names_msg}"
                )

            for i, animation in enumerate(animations):
                if isinstance(animation, AnimationBase):
                    continue
                raise TypeError(
                    "The specified animations' list cannot contain "
                    f"non-animation instance: {type(animation)}"
                    f"Invalid index: {i}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_vars_dict(*, arg_position_index: int, optional: bool = True) -> _Callable:
    """
    Set a validation to check the specified argument's value
    is a variables' dictionary.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.
    optional : bool, optional
        A boolean indicating whether a target argument accepts
        optional None value or not.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            vars_dict: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )

            if optional and not (isinstance(vars_dict, dict) or vars_dict is None):
                raise TypeError(
                    "The specified variables argument value is not a dictionary "
                    f"or None: {type(vars_dict)}"
                    f"\nDictionary value: {vars_dict}"
                    f"\n{callable_and_arg_names_msg}"
                )

            if not optional and not isinstance(vars_dict, dict):
                raise TypeError(
                    "The specified variables argument value is not "
                    f"a dictionary: {vars_dict}"
                    f"\n{callable_and_arg_names_msg}"
                )

            if isinstance(vars_dict, dict):
                for key in vars_dict.keys():
                    if isinstance(key, str):
                        continue
                    raise ValueError(
                        "The specified variables argument dictionary's "
                        f"key cannot contain a non-str value: {type(key)}"
                        f", {key}"
                        f"\n{callable_and_arg_names_msg}"
                    )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_display_object(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the `ap.DisplayObject` or its subclass type.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.display_validation import validate_display_object

            display_object: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_display_object(
                display_object=display_object,
                additional_err_msg=callable_and_arg_names_msg,
            )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_display_object_container(
    *, arg_position_index: int, optional: bool
) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is a container of a display object instance.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.
    optional : bool
        A boolean, whether a target argument accepts
        optional None value or not.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.display_validation import (
                validate_display_object_container,
            )

            container_object: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            if not optional:
                validate_display_object_container(
                    container_object=container_object,
                    additional_err_msg=callable_and_arg_names_msg,
                )
            elif container_object is not None:
                validate_display_object_container(
                    container_object=container_object,
                    additional_err_msg=callable_and_arg_names_msg,
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_point_2d(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the `ap.Point2D`.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """
    from apysc._validation.geom_validation import validate_point_2d_type

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            point: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_point_2d_type(
                point=point, additional_err_msg=callable_and_arg_names_msg
            )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def are_point_2ds(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the list of `ap.Point`.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """
    from apysc._validation.geom_validation import validate_point_2d_type

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._geom.point2d import Point2D
            from apysc._type.array import Array

            points: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            if not isinstance(points, list) and not isinstance(points, Array):
                raise TypeError(
                    "The specified points argument type is not a list or "
                    f"ap.Array: {type(points)}"
                    f"\n{callable_and_arg_names_msg}"
                )

            value: List[Point2D] = []
            if isinstance(points, list):
                value = points
            elif isinstance(points, Array):
                value = points._value
            for point in value:
                validate_point_2d_type(
                    point=point, additional_err_msg=callable_and_arg_names_msg
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_valid_path_data_list(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the list of `ap.PathDataBase` and a first value is an instance of
    the `PathMoveTo`.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._geom.path_data_base import PathDataBase
            from apysc._validation.path_validation import validate_path_data_list

            path_data_list = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )

            if not isinstance(path_data_list, list):
                raise TypeError(
                    "The specified `path_data_list`'s type is not the "
                    f"list: {type(path_data_list)}"
                    f"\n{callable_and_arg_names_msg}"
                )

            for path_data in path_data_list:
                if isinstance(path_data, PathDataBase):
                    continue
                raise TypeError(
                    "A value of path_data_list argument is not a "
                    "type of `ap.PathDataBase`'s subclass: "
                    f"{type(path_data)}"
                )
            validate_path_data_list(path_data_list=path_data_list)

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_line_cap(*, arg_position_index: int, optional: bool) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is a line cap-related type.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.
    optional : bool
        A boolean indicating whether the specified argument can be
        the `None`.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.display_validation import validate_line_cap

            cap: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            if not optional:
                validate_line_cap(
                    cap=cap, additional_err_msg=callable_and_arg_names_msg
                )
            elif cap is not None:
                validate_line_cap(
                    cap=cap, additional_err_msg=callable_and_arg_names_msg
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def are_line_joints(*, arg_position_index: int, optional: bool) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is a line joints-related type.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.
    optional : bool
        A boolean indicating whether the specified argument can be
        the `None`.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.display_validation import validate_line_joints

            joints: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            if not optional:
                validate_line_joints(
                    joints=joints, additional_err_msg=callable_and_arg_names_msg
                )
            elif joints is not None:
                validate_line_joints(
                    joints=joints, additional_err_msg=callable_and_arg_names_msg
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def multiple_line_settings_are_not_set(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's instance
    does not have multiple line settings.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.display_validation import (
                validate_multiple_line_settings_are_not_set,
            )

            instance: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            result: Any = callable_(*args, **kwargs)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_multiple_line_settings_are_not_set(
                any_instance=instance, additional_err_msg=callable_and_arg_names_msg
            )

            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_line_dot_setting(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the `ap.LineDotSetting`.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._display.line_dot_setting import LineDotSetting

            setting: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            if not isinstance(setting, (type(None), LineDotSetting)):
                raise TypeError(
                    "The specified setting is not the `ap.LineDotSetting` "
                    f"type or None: {type(setting)}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_line_dash_setting(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the `ap.LineDashSetting`.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._display.line_dash_setting import LineDashSetting

            setting: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            if not isinstance(setting, (type(None), LineDashSetting)):
                raise TypeError(
                    "The specified setting is not the `ap.LineDashSetting`"
                    f" type or None: {type(setting)}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_line_dash_dot_setting(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the `ap.LineDashDotSetting`.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._display.line_dash_dot_setting import LineDashDotSetting

            setting: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            if not isinstance(setting, (type(None), LineDashDotSetting)):
                raise TypeError(
                    "The specified setting is not the "
                    "`ap.LineDashDotSetting` type or None: "
                    f"{type(setting)}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_line_round_dot_setting(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the `ap.LineRoundDotSetting`.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._display.line_round_dot_setting import LineRoundDotSetting

            setting: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            if not isinstance(setting, (type(None), LineRoundDotSetting)):
                raise TypeError(
                    "The specified setting is not the `ap.LineRoundDotSetting` "
                    f"type or None: {type(setting)}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_variable_name_interface_type(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the `ap.VariableNameMixIn` or its subclass type.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.variable_name_validation import (
                validate_variable_name_mixin_type,
            )

            instance: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_variable_name_mixin_type(
                instance=instance, additional_err_msg=callable_and_arg_names_msg
            )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_acceptable_array_value(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is an acceptable array value type.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._type.array import Array

            value: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            acceptable_types: Tuple = (list, tuple, range, Array)
            if not isinstance(value, acceptable_types):
                callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                    callable_=callable_, arg_position_index=arg_position_index
                )
                raise TypeError(
                    "The specified value's type is not an acceptable array value: "
                    f"{type(value)}\nAcceptable types: {acceptable_types}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_acceptable_dictionary_value(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is an acceptable dictionary value type.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._type.dictionary import Dictionary

            value: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            acceptable_types: Tuple = (dict, Dictionary)
            if not isinstance(value, acceptable_types):
                callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                    callable_=callable_, arg_position_index=arg_position_index
                )
                raise TypeError(
                    "The specified value's type is not an acceptable dictionary value "
                    f"type: {type(value)}\nAcceptable types: {acceptable_types}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_builtin_dict(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the Python's `dict` type.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            value: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            if not isinstance(value, dict):
                callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                    callable_=callable_, arg_position_index=arg_position_index
                )
                raise TypeError(
                    "The specified value's type is not the Python's `dict`: "
                    f"{type(value).__name__}"
                    f"\n{callable_and_arg_names_msg}"
                )
            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_apysc_dict(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the `ap.Dictionary` type.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._type.dictionary import Dictionary

            value: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            if not isinstance(value, Dictionary):
                callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                    callable_=callable_, arg_position_index=arg_position_index
                )
                raise TypeError(
                    "The specified value's type is not the `ap.Dictionary`: "
                    f"{type(value).__name__}"
                    f"\n{callable_and_arg_names_msg}"
                )
            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_acceptable_boolean_value(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is an acceptable boolean value type.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._type.boolean import Boolean
            from apysc._type.int import Int
            from apysc._validation import number_validation

            value: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            number_validation.validate_int_is_zero_or_one(integer=value)

            acceptable_types: Tuple = (bool, int, Int, Boolean)
            if not isinstance(value, acceptable_types):
                callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                    callable_=callable_, arg_position_index=arg_position_index
                )
                raise TypeError(
                    "The specified value's type is not an acceptable "
                    "boolean value type: "
                    f"{type(value)}\nAcceptable types: {acceptable_types}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_fps(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's value
    is the FPS enum.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._time.fps import FPS

            value: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            if not isinstance(value, FPS):
                callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                    callable_=callable_, arg_position_index=arg_position_index
                )
                raise TypeError(
                    f"The specified value is not an FPS enum value: {type(value)}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_four_digit_year(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's value
    is a four-digit year (full-year).

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._type.int import Int
            from apysc._validation.number_validation import validate_integer

            year: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_integer(
                integer=year, additional_err_msg=callable_and_arg_names_msg
            )
            is_length_check_target: bool = False
            if isinstance(year, int):
                is_length_check_target = True
            if isinstance(year, Int) and year._value != 0:
                is_length_check_target = True
            if is_length_check_target:
                year_str: str = str(year)
                if len(year_str) != 4:
                    raise ValueError(
                        f"The specified four-digit year is not a valid length: "
                        f"{year_str}\n{callable_and_arg_names_msg}"
                    )
            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_month_int(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's value
    is a valid month integer (1-12).

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._type.int import Int
            from apysc._validation.number_validation import validate_integer

            month: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_integer(
                integer=month, additional_err_msg=callable_and_arg_names_msg
            )
            is_checking_target: bool = False
            if isinstance(month, int):
                is_checking_target = True
            if isinstance(month, Int) and month._value != 0:
                is_checking_target = True
            if isinstance(month, Int):
                month = month._value
            if is_checking_target:
                if month < 1 or 12 < month:
                    raise ValueError(
                        "The specified month integer is not a valid value (1-12): "
                        f"{month}\n{callable_and_arg_names_msg}"
                    )
            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_day_int(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's value
    is a valid day integer (1-31).

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._type.int import Int
            from apysc._validation.number_validation import validate_integer

            day: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_integer(
                integer=day,
                additional_err_msg=callable_and_arg_names_msg,
            )
            is_checking_target: bool = False
            if isinstance(day, int):
                is_checking_target = True
            if isinstance(day, Int) and day._value != 0:
                is_checking_target = True
            if isinstance(day, Int):
                day = day._value
            if is_checking_target:
                if day < 1 or 31 < day:
                    raise ValueError(
                        f"The specified day is out of range (1-31): {day}"
                        f"\n{callable_and_arg_names_msg}"
                    )
            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_hour_int(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's value
    is a valid hour integer (0-23).

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.number_validation import validate_integer

            hour: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_integer(
                integer=hour,
                additional_err_msg=callable_and_arg_names_msg,
            )
            if hour < 0 or 23 < hour:
                raise ValueError(
                    f"The specified hour is out of range (0-23): {hour}"
                    f"\n{callable_and_arg_names_msg}"
                )
            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_minute_int(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's value
    is a valid minute integer (0-59).

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.number_validation import validate_integer

            minute: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_integer(
                integer=minute,
                additional_err_msg=callable_and_arg_names_msg,
            )
            if minute < 0 or 59 < minute:
                raise ValueError(
                    f"The specified minute is out of range (0-59): {minute}"
                    f"\n{callable_and_arg_names_msg}"
                )
            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_second_int(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's value
    is a valid second integer (0-59).

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.number_validation import validate_integer

            second: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_integer(
                integer=second,
                additional_err_msg=callable_and_arg_names_msg,
            )
            if second < 0 or 59 < second:
                raise ValueError(
                    f"The specified second is out of range (0-59): {second}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_millisecond_int(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's value
    is a valid millisecond integer (0-999).

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.number_validation import validate_integer

            millisecond: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_integer(
                integer=millisecond,
                additional_err_msg=callable_and_arg_names_msg,
            )
            if millisecond < 0 or 999 < millisecond:
                raise ValueError(
                    f"The specified millisecond is out of range (0-999): {millisecond}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_apysc_datetime(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the apysc's `DateTime` type.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._time.datetime_ import DateTime

            datetime_: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            if not isinstance(datetime_, DateTime):
                callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                    callable_=callable_, arg_position_index=arg_position_index
                )
                raise TypeError(
                    f"The specified value of type `{type(datetime_)}` is not an "
                    "apysc's DateTime instance."
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_apysc_array(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the `ap.Array`

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._type.array import Array

            arr: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            if not isinstance(arr, Array):
                callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                    callable_=callable_, arg_position_index=arg_position_index
                )
                raise TypeError(
                    "The specified argument is not "
                    f"an `ap.Array` instance: {type(arr)}, {arr}"
                    f"\n{callable_and_arg_names_msg}"
                )
            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_nums_array(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified `Array`'s values
    are all number-relate type.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._type.array import Array
            from apysc._type.int import Int
            from apysc._type.number import Number

            arr: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            if not isinstance(arr, Array):
                raise TypeError(
                    f"The specified argument is not an `Array` instance: {type(arr)}"
                    f"\n{callable_and_arg_names_msg}"
                )
            for value in arr._value:
                if isinstance(value, (int, float, Int, Number)):
                    continue
                raise ValueError(
                    f"The specified array contains a non-number value: {type(value)}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_apysc_string_array(
    *,
    arg_position_index: int,
    optional: bool,
) -> _Callable:
    """
    Set a validation to check the specified `Array`'s values
    are all apysc's `String` type.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.
    optional : bool, optional
        A boolean indicating whether a target argument accepts
        optional None value or not.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._type.array import Array
            from apysc._type.string import String

            arr: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            if optional and arr is None:
                return callable_(*args, **kwargs)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            if not isinstance(arr, Array):
                raise TypeError(
                    f"The specified argument is not an `Array` instance: {type(arr)}"
                    f"\n{callable_and_arg_names_msg}"
                )
            for value in arr._value:
                if isinstance(value, String):
                    continue
                raise TypeError(
                    "A value in an array is not an apysc's String instance: "
                    f"{type(value)}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_builtin_str_list_or_apysc_str_arr(
    *,
    arg_position_index: int,
    optional: bool,
) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is list of Python's str or Array of apysc's String.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.
    optional : bool
        A boolean indicating whether a target argument accepts
        optional None value or not.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._type.array import Array
            from apysc._type.string import String

            arr_or_list: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            if optional and arr_or_list is None:
                return callable_(*args, **kwargs)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            if isinstance(arr_or_list, list):
                for value in arr_or_list:
                    if not isinstance(value, str):
                        raise TypeError(
                            "A value in a list is not a Python's `str` value: "
                            f"{type(value)}"
                            f"\n{callable_and_arg_names_msg}"
                        )
                return callable_(*args, **kwargs)
            if isinstance(arr_or_list, Array):
                for value in arr_or_list._value:
                    if not isinstance(value, String):
                        raise TypeError(
                            "A value in an array is not an apysc's String instance: "
                            f"{type(value)}"
                            f"\n{callable_and_arg_names_msg}"
                        )
                return callable_(*args, **kwargs)
            raise TypeError(
                "The specified argument is not a list or `Array` instance: "
                f"{type(arr_or_list)}"
                f"\n{callable_and_arg_names_msg}"
            )

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_svg_text_align(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the `SvgTextAlign`.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._display.svg_text_align_mixin import SvgTextAlign

            align: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            if not isinstance(align, SvgTextAlign):
                callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                    callable_=callable_, arg_position_index=arg_position_index
                )
                raise TypeError(
                    "The specified argument is not a `SvgTextAlign` value: "
                    f"{type(align)}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def are_text_spans(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the list or `ap.Array` of `ap.SvgTextSpan`.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._display.svg_text_span import SvgTextSpan
            from apysc._type.array import Array

            text_spans: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            if not isinstance(text_spans, (list, Array)):
                raise TypeError(
                    "The specified argument is not a list or `Array` instance: "
                    f"{type(text_spans)}"
                    f"\n{callable_and_arg_names_msg}"
                )
            if isinstance(text_spans, list):
                for i, text_span in enumerate(text_spans):
                    if isinstance(text_span, SvgTextSpan):
                        continue
                    raise TypeError(
                        "There is a non-`SvgTextSpan` instance in a list: "
                        f"{type(text_span)}\nIndex: {i}"
                        f"\n{callable_and_arg_names_msg}"
                    )
            if isinstance(text_spans, Array):
                for i, text_span in enumerate(text_spans._value):
                    if isinstance(text_span, SvgTextSpan):
                        continue
                    raise TypeError(
                        "There is a non-`SvgTextSpan` instance in an array: "
                        f"{type(text_span)}\nIndex: {i}"
                        f"\n{callable_and_arg_names_msg}"
                    )
            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_x_axis_label_position(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the `XAxisLabelPosition`.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._chart.x_axis_label_position import XAxisLabelPosition

            x_axis_label_position: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            if not isinstance(x_axis_label_position, XAxisLabelPosition):
                callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                    callable_=callable_, arg_position_index=arg_position_index
                )
                raise TypeError(
                    "The specified argument is not a `XAxisLabelPosition` value: "
                    f"{type(x_axis_label_position).__name__}, {x_axis_label_position}"
                    f"\n{callable_and_arg_names_msg}"
                )
            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_y_axis_label_position(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the `YAxisLabelPosition`.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._chart.y_axis_label_position import YAxisLabelPosition

            y_axis_label_position: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            if not isinstance(y_axis_label_position, YAxisLabelPosition):
                callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                    callable_=callable_, arg_position_index=arg_position_index
                )
                raise TypeError(
                    "The specified argument is not a `YAxisLabelPosition` value: "
                    f"{type(y_axis_label_position).__name__}, {y_axis_label_position}"
                    f"\n{callable_and_arg_names_msg}"
                )
            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_list_or_array_matrix_data(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is list of dicts or `ap.Array` of `ap.Dictionary`.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._type.array import Array
            from apysc._validation import matrix_data_validation

            matrix_data: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            if isinstance(matrix_data, list):
                matrix_data_validation.validate_matrix_list_data(
                    matrix_list_data=matrix_data,
                    additional_err_msg=callable_and_arg_names_msg,
                )
                return callable_(*args, **kwargs)
            if isinstance(matrix_data, Array):
                matrix_data_validation.validate_matrix_array_data(
                    matrix_array_data=matrix_data,
                    additional_err_msg=callable_and_arg_names_msg,
                )
                return callable_(*args, **kwargs)
            raise TypeError(
                "The specified argument is not a list of dicts or "
                f"`ap.Array` of `ap.Dictionary`: {type(matrix_data).__name__}, "
                f"\n{callable_and_arg_names_msg}"
            )

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_initialize_with_base_value_interface_subclass(
    *,
    arg_position_index: int,
    optional: bool = False,
) -> _Callable:
    """
    Set a validation to check the specified class is
    the `InitializeWithBaseValueInterface`'s subclas.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.
    optional : bool
        A boolean indicating whether a target argument accepts
        optional None value or not.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._loop.initialize_with_base_value_interface import (
                InitializeWithBaseValueInterface,
            )

            class_: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            if optional and class_ is None:
                return callable_(*args, **kwargs)
            if issubclass(class_, InitializeWithBaseValueInterface):
                return callable_(*args, **kwargs)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            raise TypeError(
                f"The specified class is not an `InitializeWithBaseValueInterface`'s "
                f"subclass: {class_}"
                f"\n{callable_and_arg_names_msg}"
            )

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_svg_foreign_object_child(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the `SvgForeignObjectChild` class.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._display.svg_foreign_object_child import SvgForeignObjectChild

            child: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            if not isinstance(child, SvgForeignObjectChild):
                callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                    callable_=callable_, arg_position_index=arg_position_index
                )
                raise TypeError(
                    "The specified argument is not an `SvgForeignObjectChild` "
                    f"instance: {type(child)}"
                    f"\n{callable_and_arg_names_msg}"
                )
            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_css_text_align(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the `CssTextAlign` enum.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._display.css_text_align import CssTextAlign

            text_align: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            if not isinstance(text_align, CssTextAlign):
                callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                    callable_=callable_, arg_position_index=arg_position_index
                )
                raise TypeError(
                    "The specified argument is not a `CssTextAlign` value: "
                    f"{text_align}\n{callable_and_arg_names_msg}"
                )
            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_css_text_align_last(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check the specified argument's type
    is the `CssTextAlignLast`.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._display.css_text_align_last import CssTextAlignLast

            text_align_last: CssTextAlignLast = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            if not isinstance(text_align_last, CssTextAlignLast):
                callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                    callable_=callable_, arg_position_index=arg_position_index
                )
                raise TypeError(
                    "The specified argument is not a `CssTextAlignLast` value: "
                    f"{text_align_last}\n{callable_and_arg_names_msg}"
                )
            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore
