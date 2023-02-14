# mypy: disable-error-code=type-var

"""This module is for the argument validations' decorators.

Mainly the following decorators exist.

- not_empty_string
    - Set a validation to check that a specified argument's string
        is not empty.
- handler_args_num
    - Set a validation to check a specified handler argument's
        number.
- handler_options_type
    - Set a validation to check a specified handler-options
        argument's type.
- is_event
    - Set a validation to check a specified argument's type
        is the `ap.Event` or its subclass type.
- is_num
    - Set a validation to check a specified argument's type
        is the number-related type.
- is_apysc_num
    - Set a validation to check a specified argument's type
        is the `ap.Int` or `ap.Number` type.
- is_integer
    - Set a validation to check a specified argument's type
        is the `int` or `ap.Int`.
- is_builtin_integer
    - Set a validation to check a specified argument's type
        is the built-in `int`.
- is_apysc_integer
    - Set a validation to check a specified argument's type
        is the `ap.Int`.
- num_is_gt_zero
    - Set a validation to check that a specified argument's value
        is greater than zero.
- num_is_gte_zero
    - Set a validation to check that a specified argument's value
        is greater than or equal to zero.
- num_is_0_to_1_range
    - Set a validation to check that a specified argument's value
        is 0.0 to 1.0 range.
- is_boolean
    - Set a validation to check that a specified argument's type
        is the `bool` or `ap.Boolean`.
- is_builtin_boolean
    - Set a validation to check that a specified argument's type
        is the built-in `bool`.
- is_apysc_boolean
    - Set a validation to check that a specified argument's type
        is the `ap.Boolean`.
- is_easing
    - Set a validation to check a specified argument's type
        is the `ap.Easing`.
- is_string
    - Set a validation to check a specified argument's type
        is the str or `ap.String`.
- is_builtin_string
    - Set a validation to check a specified argument's type
        is the Python built-in's `str`.
- is_apysc_string
    - Set a validation to check a specified argument's type
        is the `ap.String`.
- is_hex_color_code_format
    - Set a validation to check a specified argument's value
        is a hexadecimal color code format.
- is_animations
    - Set a validation to check a specified argument's type
        is the list of `ap.AnimationBase`.
- is_vars_dict
    - Set a validation to check a specified argument's value
        is a variables' dictionary.
- is_display_object
    - Set a validation to check a specified argument's type
        is the `ap.DisplayObject` or its subclass type.
- is_display_object_container
    - Set a validation to check a specified argument's type
        is a container of a display object instance.
- is_point_2d
    - Set a validation to check a specified argument's type
        is the `ap.Point2D`.
- is_point_2ds
    - Set a validation to check a specified argument's type
        is the list of `ap.Point2D`.
- is_valid_path_data_list
    - Set a validation to check a specified argument's type
        is the list of `ap.PathDataBase`.
- is_line_cap
    - Set a validation to check a specified argument's type
        is a line cap-related type.
- is_line_joints
    - Set a validation to check a specified argument's type
        is a line joints-related type.
- multiple_line_settings_are_not_set
    - Set a validation to check a specified argument's instance
        does not have multiple line settings.
- is_line_dot_setting
    - Set a validation to check a specified argument's type
        is the `ap.LineDotSetting`.
- is_line_dash_setting
    - Set a validation to check a specified argument's type
        is the `ap.LineDashSetting`.
- is_line_dash_dot_setting
    - Set a validation to check a specified argument's type
        is the `ap.LineDashDotSetting`.
- is_line_round_dot_setting
    - Set a validation to check a specified argument's type
        is the `ap.LineRoundDotSetting`.
- is_variable_name_interface_type
    - Set a validation to check a specified argument's type
        is the `ap.VariableNameMixIn` or its subclass type.
- is_acceptable_array_value
    - Set a validation to check a specified argument's type
        is an acceptable array value type.
- is_acceptable_dictionary_value
    - Set a validation to check a specified argument's type
        is an acceptable dictionary value type.
- is_builtin_dict
    - Set a validation to check a specified argument's type
        is the Python's `dict` type.
- is_acceptable_boolean_value
    - Set a validation to check a specified argument's type
        is an acceptable boolean value type.
- is_fps
    - Set a validation to check a specified argument's value
        is the FPS enum.
- is_four_digit_year
    - Set a validation to check a specified argument's value
        is a four-digit year (full-year).
- is_month_int
    - Set a validation to check a specified argument's value
        is a valid month integer (1-12).
- is_day_int
    - Set a validation to check a specified argument's value
        is a valid day integer (1-31).
- is_hour_int
    - Set a validation to check a specified argument's value
        is a valid hour integer (0-23).
- is_minute_int
    - Set a validation to check a specified argument's value
        is a valid minute integer (0-59).
- is_second_int
    - Set a validation to check a specified argument's value
        is a valid second integer (0-59).
- is_millisecond_int
    - Set a validation to check a specified argument's value
        is a valid millisecond integer (0-999).
- is_apysc_datetime
    - Set a validation to check a specified argument's type
        is an apysc's `DateTime` type.
- is_nums_array
    - Set a validation to check a specified `Array`'s values
        are all number-relate type.
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

# pyright: reportInvalidTypeVarUse=false
_Callable = TypeVar("_Callable", bound=Callable)


def _extract_arg_value(
    *, args: Any, kwargs: Dict[str, Any], arg_position_index: int, callable_: Callable
) -> Any:
    """
    Extract an argument value from a specified arguments' dictionary
    or list.

    Parameters
    ----------
    args : List[Any]
        A specified positional arguments' list.
    kwargs : Dict[str, Any]
        A specified keyword arguments' dictionary.'
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
    Get an argument name from a specified argument position index.

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
            "A specified function has no argument parameter "
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
    Set a validation to check that a specified argument's string
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
    Set a validation to check a specified handler argument's
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
    Set a validation to check a specified handler-options
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
    Set a validation to check a specified argument's type
    is the `ap.Event` or its subclass type.

    Parameters
    ----------
    arg_position_index : int
        _description_

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


def is_num(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check a specified argument's type
    is the number-related type.

    Parameters
    ----------
    arg_position_index : int
        _description_

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

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_num(num=num, additional_err_msg=callable_and_arg_names_msg)

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_apysc_num(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check a specified argument's type
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
                    "A specified argument value is not the `ap.Int` or "
                    f"`ap.Number` type: {type(num)}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_integer(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check a specified argument's type
    is the `int` or `ap.Int`.

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

            integer: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

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
    Set a validation to check a specified argument's type
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
    Set a validation to check a specified argument's type
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
            import apysc as ap

            integer: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            if not isinstance(integer, ap.Int):
                raise TypeError(
                    "A specified argument value is not the `ap.Int` "
                    f"type: {type(integer)}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def num_is_gt_zero(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check that a specified argument's value
    is greater than zero.

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
            from apysc._validation.number_validation import validate_num_is_gt_zero

            num: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_num_is_gt_zero(
                num=num, additional_err_msg=callable_and_arg_names_msg
            )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def num_is_gte_zero(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check that a specified argument's value
    is greater than or equal to zero.

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
            from apysc._validation.number_validation import validate_num_is_gte_zero

            num: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_num_is_gte_zero(
                num=num, additional_err_msg=callable_and_arg_names_msg
            )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def num_is_0_to_1_range(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check that a specified argument's value
    is 0.0 to 1.0 range.

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
            from apysc._validation.number_validation import validate_num_is_0_to_1_range

            num: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_num_is_0_to_1_range(
                num=num, additional_err_msg=callable_and_arg_names_msg
            )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_boolean(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check that a specified argument's type
    is the `bool` or `ap.Boolean`.

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
            from apysc._validation.bool_validation import validate_bool

            boolean: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            validate_bool(value=boolean, additional_err_msg=callable_and_arg_names_msg)

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_builtin_boolean(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check that a specified argument's type
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
    Set a validation to check that a specified argument's type
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
            import apysc as ap

            boolean: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            if not isinstance(boolean, ap.Boolean):
                raise TypeError(
                    "A specified argument value is not a `Boolean` type: "
                    f"{type(boolean)}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_easing(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check a specified argument's type
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
            import apysc as ap

            easing: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            if not isinstance(easing, ap.Easing):
                raise TypeError(
                    "A specified easing argument's type is not the "
                    f"ap.Easing: {type(easing)}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_string(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check a specified argument's type
    is the str or `ap.String`.

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
            from apysc._validation.string_validation import validate_string_type

            string: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

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
    Set a validation to check a specified argument's type
    is the Python built-in's `str`.

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
    Set a validation to check a specified argument's type
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
            import apysc as ap

            string: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            if not isinstance(string, ap.String):
                callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                    callable_=callable_, arg_position_index=arg_position_index
                )
                raise TypeError(
                    f"A specified argument's type is not the ap.String: {type(string)}"
                    f"\n{callable_and_arg_names_msg}"
                )
            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_hex_color_code_format(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check a specified argument's value
    in a hexadecimal color code format.

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


def is_animations(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check a specified argument's type
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
            import apysc as ap

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
                    "A specified animations list must be a list: "
                    f"{type(animations)}"
                    f"\n{callable_and_arg_names_msg}"
                )

            for i, animation in enumerate(animations):
                if isinstance(animation, ap.AnimationBase):
                    continue
                raise TypeError(
                    "A specified animations' list cannot contain "
                    f"non-animation instance: {type(animation)}"
                    f"Invalid index: {i}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_vars_dict(*, arg_position_index: int, optional: bool = True) -> _Callable:
    """
    Set a validation to check a specified argument's value
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
                    "A specified variables argument value is not a dictionary "
                    f"or None: {type(vars_dict)}"
                    f"\nDictionary value: {vars_dict}"
                    f"\n{callable_and_arg_names_msg}"
                )

            if not optional and not isinstance(vars_dict, dict):
                raise TypeError(
                    "A specified variables argument value is not "
                    f"a dictionary: {vars_dict}"
                    f"\n{callable_and_arg_names_msg}"
                )

            if isinstance(vars_dict, dict):
                for key in vars_dict.keys():
                    if isinstance(key, str):
                        continue
                    raise ValueError(
                        "A specified variables argument dictionary's "
                        f"key cannot contain a non-str value: {type(key)}"
                        f", {key}"
                        f"\n{callable_and_arg_names_msg}"
                    )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_display_object(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check a specified argument's type
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
    Set a validation to check a specified argument's type
    is a container of a display object instance.

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
    Set a validation to check a specified argument's type
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


def is_point_2ds(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check a specified argument's type
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
            import apysc as ap

            points: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            if not isinstance(points, list) and not isinstance(points, ap.Array):
                raise TypeError(
                    "A specified points argument type is not the list or "
                    f"ap.Array: {type(points)}"
                    f"\n{callable_and_arg_names_msg}"
                )

            value: List[ap.Point2D] = []
            if isinstance(points, list):
                value = points
            elif isinstance(points, ap.Array):
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
    Set a validation to check a specified argument's type
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
            import apysc as ap
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
                    "A specified `path_data_list`'s type is not the "
                    f"list: {type(path_data_list)}"
                    f"\n{callable_and_arg_names_msg}"
                )

            for path_data in path_data_list:
                if isinstance(path_data, ap.PathDataBase):
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
    Set a validation to check a specified argument's type
    is a line cap-related type.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.
    optional : bool
        A boolean indicating whether a specified argument can be
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


def is_line_joints(*, arg_position_index: int, optional: bool) -> _Callable:
    """
    Set a validation to check a specified argument's type
    is a line joints-related type.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.
    optional : bool
        A boolean indicating whether a specified argument can be
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
    Set a validation to check a specified argument's instance
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
    Set a validation to check a specified argument's type
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
            import apysc as ap

            setting: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            if not isinstance(setting, (type(None), ap.LineDotSetting)):
                raise TypeError(
                    "A specified setting is not the `ap.LineDotSetting` "
                    f"type or None: {type(setting)}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_line_dash_setting(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check a specified argument's type
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
            import apysc as ap

            setting: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            if not isinstance(setting, (type(None), ap.LineDashSetting)):
                raise TypeError(
                    "A specified setting is not the `ap.LineDashSetting`"
                    f" type or None: {type(setting)}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_line_dash_dot_setting(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check a specified argument's type
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
            import apysc as ap

            setting: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            if not isinstance(setting, (type(None), ap.LineDashDotSetting)):
                raise TypeError(
                    "A specified setting is not the "
                    "`ap.LineDashDotSetting` type or None: "
                    f"{type(setting)}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_line_round_dot_setting(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check a specified argument's type
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
            import apysc as ap

            setting: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            if not isinstance(setting, (type(None), ap.LineRoundDotSetting)):
                raise TypeError(
                    "A specified setting is not the `ap.LineRoundDotSetting` "
                    f"type or None: {type(setting)}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_variable_name_interface_type(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check a specified argument's type
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
                validate_variable_name_interface_type,
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
            validate_variable_name_interface_type(
                instance=instance, additional_err_msg=callable_and_arg_names_msg
            )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_acceptable_array_value(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check a specified argument's type
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
            import apysc as ap

            value: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            acceptable_types: Tuple = (list, tuple, range, ap.Array)
            if not isinstance(value, acceptable_types):
                callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                    callable_=callable_, arg_position_index=arg_position_index
                )
                raise TypeError(
                    "A specified value's type is not an acceptable array value: "
                    f"{type(value)}\nAcceptable types: {acceptable_types}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_acceptable_dictionary_value(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check a specified argument's type
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
            import apysc as ap

            value: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )
            acceptable_types: Tuple = (dict, ap.Dictionary)
            if not isinstance(value, acceptable_types):
                callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                    callable_=callable_, arg_position_index=arg_position_index
                )
                raise TypeError(
                    "A specified value's type is not an acceptable dictionary value "
                    f"type: {type(value)}\nAcceptable types: {acceptable_types}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_builtin_dict(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check a specified argument's type
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
                    "A specified value's type is not the Python's `dict`: "
                    f"{type(value)}"
                    f"\n{callable_and_arg_names_msg}"
                )
            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_acceptable_boolean_value(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check a specified argument's type
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
            import apysc as ap
            from apysc._validation import number_validation

            value: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            number_validation.validate_int_is_zero_or_one(integer=value)

            acceptable_types: Tuple = (bool, int, ap.Int, ap.Boolean)
            if not isinstance(value, acceptable_types):
                callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                    callable_=callable_, arg_position_index=arg_position_index
                )
                raise TypeError(
                    "A specified value's type is not an acceptable boolean value type: "
                    f"{type(value)}\nAcceptable types: {acceptable_types}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_fps(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check a specified argument's value
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
            import apysc as ap

            value: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            if not isinstance(value, ap.FPS):
                callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                    callable_=callable_, arg_position_index=arg_position_index
                )
                raise TypeError(
                    f"A specified value is not an FPS enum value: {type(value)}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_four_digit_year(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check a specified argument's value
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
            import apysc as ap
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
            if isinstance(year, ap.Int) and year._value != 0:
                is_length_check_target = True
            if is_length_check_target:
                year_str: str = str(year)
                if len(year_str) != 4:
                    raise ValueError(
                        f"A specified four-digit year is not a valid length: {year_str}"
                        f"\n{callable_and_arg_names_msg}"
                    )
            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_month_int(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check a specified argument's value
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
            import apysc as ap
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
            if isinstance(month, ap.Int) and month._value != 0:
                is_checking_target = True
            if isinstance(month, ap.Int):
                month = month._value
            if is_checking_target:
                if month < 1 or 12 < month:
                    raise ValueError(
                        "A specified month integer is not a valid value (1-12): "
                        f"{month}\n{callable_and_arg_names_msg}"
                    )
            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_day_int(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check a specified argument's value
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
            import apysc as ap
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
            if isinstance(day, ap.Int) and day._value != 0:
                is_checking_target = True
            if isinstance(day, ap.Int):
                day = day._value
            if is_checking_target:
                if day < 1 or 31 < day:
                    raise ValueError(
                        f"A specified day is out of range (1-31): {day}"
                        f"\n{callable_and_arg_names_msg}"
                    )
            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_hour_int(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check a specified argument's value
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
                    f"A specified hour is out of range (0-23): {hour}"
                    f"\n{callable_and_arg_names_msg}"
                )
            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_minute_int(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check a specified argument's value
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
                    f"A specified minute is out of range (0-59): {minute}"
                    f"\n{callable_and_arg_names_msg}"
                )
            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_second_int(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check a specified argument's value
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
                    f"A specified second is out of range (0-59): {second}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_millisecond_int(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check a specified argument's value
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
                    f"A specified millisecond is out of range (0-999): {millisecond}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_apysc_datetime(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check a specified argument's type
    is an apysc's `DateTime` type.

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
                    f"A specified value of type `{type(datetime_)}` is not an "
                    "apysc's DateTime instance."
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_nums_array(*, arg_position_index: int) -> _Callable:
    """
    Set a validation to check a specified `Array`'s values
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
            import apysc as ap

            arr: Any = _extract_arg_value(
                args=args,
                kwargs=kwargs,
                arg_position_index=arg_position_index,
                callable_=callable_,
            )

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index
            )
            if not isinstance(arr, ap.Array):
                raise TypeError(
                    f"A specified argument is not an `Array` instance: {type(arr)}"
                    f"\n{callable_and_arg_names_msg}"
                )
            for value in arr._value:
                if isinstance(value, (int, float, ap.Int, ap.Number)):
                    continue
                raise ValueError(
                    f"A specified array contains a non-number value: {type(value)}"
                    f"\n{callable_and_arg_names_msg}"
                )

            return callable_(*args, **kwargs)

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore
