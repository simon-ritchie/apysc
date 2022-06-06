"""This module is for the argument validations' decorators.

Mainly the following decorators exist.

- not_empty_string
    - Set the validation to check that a specified argument's string
        is not empty.
- handler_args_num
    - Set the validation to check a specified handler argument's
        number.
- handler_options_type
    - Set the validation to check a specified handler-options
        argument's type.
- is_event
    - Set the validation to check a specified argument's type
        is the `ap.Event` or its subclass type.
- is_num
    - Set the validation to check a specified argument's type
        is the number-related type.
- is_apysc_num
    - Set the validation to check a specified argument's type
        is the `ap.Int` or `ap.Number` type.
- is_integer
    - Set the validation to check a specified argument's type
        is the `int` or `ap.Int`.
- is_builtin_integer
    - Set the validation to check a specified argument's type
        is the built-in `int`.
- is_apysc_integer
    - Set the validation to check a specified argument's type
        is the `ap.Int`.
- num_is_gt_zero
    - Set the validation to check that a specified argument's value
        is greater than zero.
- num_is_gte_zero
    - Set the validation to check that a specified argument's value
        is greater than or equal to zero.
- num_is_0_to_1_range
    - Set the validation to check that a specified argument's value
        is 0.0 to 1.0 range.
- is_boolean
    - Set the validation to check that a specified argument's type
        is the `bool` or `ap.Boolean`.
- is_builtin_boolean
    - Set the validation to check that a specified argument's type
        is the built-in `bool`.
- is_apysc_boolean
    - Set the validation to check that a specified argument's type
        is the `ap.Boolean`.
- is_easing
    - Set the validation to check a specified argument's type
        is the `ap.Easing`.
- is_string
    - Set the validation to check a specified argument's type
        is the str or `ap.String`.
- is_builtin_string
    - Set the validation to check a specified argument's type
        is the Python built-in's `str`.
- is_hex_color_code_format
    - Set the validation to check a specified argument's value
        is a hexadecimal color code format.
- is_animations
    - Set the validation to check a specified argument's type
        is the list of `ap.AnimationBase`.
- is_vars_dict
    - Set the validation to check a specified argument's value
        is a variables' dictionary.
- is_display_object
    - Set the validation to check a specified argument's type
        is the `ap.DisplayObject` or its subclass type.
- is_display_object_container
    - Set the validation to check a specified argument's type
        is a container of a display object instance.
- is_point_2d
    - Set the validation to check a specified argument's type
        is the `ap.Point2D`.
- is_point_2ds
    - Set the validation to check a specified argument's type
        is the list of `ap.Point2D`.
- is_path_data_list
    - Set the validation to check a specified argument's type
        is the list of `ap.PathDataBase`.
- is_line_cap
    - Set the validation to check a specified argument's type
        is a line cap-related type.
- is_line_joints
    - Set the validation to check a specified argument's type
        is a line joints-related type.
- multiple_line_settings_are_not_set
    - Set the validation to check a specified argument's instance
        does not have multiple line settings.
- is_line_dot_setting
    - Set the validation to check a specified argument's type
        is the `ap.LineDotSetting`.
- is_line_dash_setting
    - Set the validation to check a specified argument's type
        is the `ap.LineDashSetting`.
- is_line_dash_dot_setting
    - Set the validation to check a specified argument's type
        is the `ap.LineDashDotSetting`.
- is_line_round_dot_setting
    - Set the validation to check a specified argument's type
        is the `ap.LineRoundDotSetting`.
- is_variable_name_interface_type
    - Set the validation to check a specified argument's type
        is the `ap.VariableNameInterface` or its subclass type.
"""

import functools
import inspect
from inspect import Signature
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import TypeVar

# pyright: reportInvalidTypeVarUse=false
_F = TypeVar('_F', bound=Callable)


def _extract_arg_value(
        *, args: Any, kwargs: Dict[str, Any],
        arg_position_index: int,
        callable_: Callable) -> Any:
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
        callable_=callable_, arg_position_index=arg_position_index)
    default_val: Any = _get_default_val_by_arg_name(
        callable_=callable_, arg_name=arg_name)
    if arg_name in kwargs:
        value = kwargs[arg_name]
    elif len(args) - 1 >= arg_position_index:
        value = args[arg_position_index]
    if value is None and default_val is not None:
        return default_val
    return value


def _get_arg_name_by_index(
        *, callable_: Callable, arg_position_index: int) -> str:
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
            'A specified function has no argument parameter '
            f'at the index of {arg_position_index}'
            f'\nActual argument length: {len(signature.parameters)}')
    arg_name: str = ''
    for i, (arg_name_, _) in enumerate(signature.parameters.items()):
        if i == arg_position_index:
            arg_name = arg_name_
    return arg_name


def _get_callable_and_arg_names_msg(
        *, callable_: Callable, arg_position_index: int) -> str:
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
        callable_=callable_, arg_position_index=arg_position_index)
    callable_and_arg_names_msg: str = (
        f'Target callable name: {callable_.__name__}'
        f'\nTarget argument name: {arg_name}'
    )
    return callable_and_arg_names_msg


def _get_default_val_by_arg_name(
        *, callable_: Callable, arg_name: str) -> Any:
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


def not_empty_string(*, arg_position_index: int) -> _F:
    """
    Set the validation to check that a specified argument's string
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.string_validation import \
                validate_not_empty_string
            string: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            validate_not_empty_string(
                string=string,
                additional_err_msg=(
                    'An argument\'s string value must not be empty.'
                    f'\n{callable_and_arg_names_msg}'
                ))

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def handler_args_num(*, arg_position_index: int) -> _F:
    """
    Set the validation to check a specified handler argument's
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.handler_validation import \
                validate_handler_args_num
            handler: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            validate_handler_args_num(
                handler=handler,
                additional_err_msg=callable_and_arg_names_msg)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def handler_options_type(*, arg_position_index: int) -> _F:
    """
    Set the validation to check a specified handler-options
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.handler_validation import \
                validate_options_type
            options: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            validate_options_type(
                options=options,
                additional_err_msg=callable_and_arg_names_msg)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_event(*, arg_position_index: int) -> _F:
    """
    Set the validation to check a specified argument's type
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.event_validation import validate_event
            event: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            validate_event(
                e=event, additional_err_msg=callable_and_arg_names_msg)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_num(*, arg_position_index: int) -> _F:
    """
    Set the validation to check a specified argument's type
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.number_validation import validate_num
            num: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            validate_num(
                num=num,
                additional_err_msg=callable_and_arg_names_msg)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_apysc_num(*, arg_position_index: int) -> _F:
    """
    Set the validation to check a specified argument's type
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._type.number_value_interface import NumberValueInterface
            num: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            if not isinstance(num, NumberValueInterface):
                raise TypeError(
                    'A specified argument value is not the `ap.Int` or '
                    f'`ap.Number` type: {type(num)}'
                    f'\n{callable_and_arg_names_msg}')

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_integer(*, arg_position_index: int) -> _F:
    """
    Set the validation to check a specified argument's type
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.number_validation import validate_integer
            integer: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            validate_integer(
                integer=integer,
                additional_err_msg=callable_and_arg_names_msg)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_builtin_integer(*, arg_position_index: int) -> _F:
    """
    Set the validation to check a specified argument's type
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.number_validation import \
                validate_builtin_integer
            integer: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            validate_builtin_integer(
                integer=integer,
                additional_err_msg=callable_and_arg_names_msg)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_apysc_integer(*, arg_position_index: int) -> _F:
    """
    Set the validation to check a specified argument's type
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            import apysc as ap
            integer: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            if not isinstance(integer, ap.Int):
                raise TypeError(
                    'A specified argument value is not the `ap.Int` '
                    f'type: {type(integer)}'
                    f'\n{callable_and_arg_names_msg}')

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def num_is_gt_zero(*, arg_position_index: int) -> _F:
    """
    Set the validation to check that a specified argument's value
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.number_validation import \
                validate_num_is_gt_zero
            num: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            validate_num_is_gt_zero(
                num=num, additional_err_msg=callable_and_arg_names_msg)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def num_is_gte_zero(*, arg_position_index: int) -> _F:
    """
    Set the validation to check that a specified argument's value
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.number_validation import \
                validate_num_is_gte_zero
            num: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            validate_num_is_gte_zero(
                num=num, additional_err_msg=callable_and_arg_names_msg)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def num_is_0_to_1_range(*, arg_position_index: int) -> _F:
    """
    Set the validation to check that a specified argument's value
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.number_validation import \
                validate_num_is_0_to_1_range
            num: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            validate_num_is_0_to_1_range(
                num=num, additional_err_msg=callable_and_arg_names_msg)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_boolean(*, arg_position_index: int) -> _F:
    """
    Set the validation to check that a specified argument's type
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.bool_validation import validate_bool
            boolean: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            validate_bool(
                value=boolean, additional_err_msg=callable_and_arg_names_msg)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_builtin_boolean(*, arg_position_index: int) -> _F:
    """
    Set the validation to check that a specified argument's type
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.bool_validation import validate_builtin_bool
            boolean: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            validate_builtin_bool(
                value=boolean, additional_err_msg=callable_and_arg_names_msg)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_apysc_boolean(*, arg_position_index: int) -> _F:
    """
    Set the validation to check that a specified argument's type
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            import apysc as ap
            boolean: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            if not isinstance(boolean, ap.Boolean):
                raise TypeError(
                    'A specified argument value is not a `Boolean` type: '
                    f'{type(boolean)}'
                    f'\n{callable_and_arg_names_msg}')

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_easing(*, arg_position_index: int) -> _F:
    """
    Set the validation to check a specified argument's type
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            import apysc as ap
            easing: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            if not isinstance(easing, ap.Easing):
                raise TypeError(
                    'A specified easing argument\'s type is not the '
                    f'ap.Easing: {type(easing)}'
                    f'\n{callable_and_arg_names_msg}')

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_string(*, arg_position_index: int) -> _F:
    """
    Set the validation to check a specified argument's type
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.string_validation import \
                validate_string_type
            string: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            validate_string_type(
                string=string, additional_err_msg=callable_and_arg_names_msg)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_builtin_string(*, arg_position_index: int, optional: bool) -> _F:
    """
    Set the validation to check a specified argument's type
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.string_validation import \
                validate_builtin_string_type
            string: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            if not optional:
                validate_builtin_string_type(
                    string=string,
                    additional_err_msg=callable_and_arg_names_msg)
            elif string is not None:
                validate_builtin_string_type(
                    string=string,
                    additional_err_msg=callable_and_arg_names_msg)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_hex_color_code_format(*, arg_position_index: int) -> _F:
    """
    Set the validation to check a specified argument's value
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._color import color_util
            from apysc._validation.color_validation import \
                validate_hex_color_code_format
            hex_color_code: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            hex_color_code = color_util.remove_color_code_sharp_symbol(
                hex_color_code=hex_color_code)
            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            validate_hex_color_code_format(
                hex_color_code=hex_color_code,
                additional_err_msg=callable_and_arg_names_msg)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_animations(*, arg_position_index: int) -> _F:
    """
    Set the validation to check a specified argument's type
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            import apysc as ap
            animations: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)
            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)

            if not isinstance(animations, list):
                raise TypeError(
                    'A specified animations list must be a list: '
                    f'{type(animations)}'
                    f'\n{callable_and_arg_names_msg}')

            for i, animation in enumerate(animations):
                if isinstance(animation, ap.AnimationBase):
                    continue
                raise TypeError(
                    'A specified animations\' list cannot contain '
                    f'non-animation instance: {type(animation)}'
                    f'Invalid index: {i}'
                    f'\n{callable_and_arg_names_msg}')

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_vars_dict(
        *, arg_position_index: int, optional: bool = True) -> _F:
    """
    Set the validation to check a specified argument's value
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            vars_dict: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)
            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)

            if optional and not (
                isinstance(
                    vars_dict,
                    dict) or vars_dict is None):
                raise TypeError(
                    'A specified variables argument value is not a dictionary '
                    f'or None: {type(vars_dict)}'
                    f'\nDictionary value: {vars_dict}'
                    f'\n{callable_and_arg_names_msg}')

            if not optional and not isinstance(vars_dict, dict):
                raise TypeError(
                    'A specified variables argument value is not '
                    f'a dictionary: {vars_dict}'
                    f'\n{callable_and_arg_names_msg}')

            if isinstance(vars_dict, dict):
                for key in vars_dict.keys():
                    if isinstance(key, str):
                        continue
                    raise ValueError(
                        'A specified variables argument dictionary\'s '
                        f'key cannot contain a non-str value: {type(key)}'
                        f', {key}'
                        f'\n{callable_and_arg_names_msg}')

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_display_object(*, arg_position_index: int) -> _F:
    """
    Set the validation to check a specified argument's type
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.display_validation import \
                validate_display_object
            display_object: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            validate_display_object(
                display_object=display_object,
                additional_err_msg=callable_and_arg_names_msg)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_display_object_container(
        *, arg_position_index: int,
        optional: bool) -> _F:
    """
    Set the validation to check a specified argument's type
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.display_validation import \
                validate_display_object_container
            container_object: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            if not optional:
                validate_display_object_container(
                    container_object=container_object,
                    additional_err_msg=callable_and_arg_names_msg)
            elif container_object is not None:
                validate_display_object_container(
                    container_object=container_object,
                    additional_err_msg=callable_and_arg_names_msg)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_point_2d(*, arg_position_index: int) -> _F:
    """
    Set the validation to check a specified argument's type
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            point: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            validate_point_2d_type(
                point=point, additional_err_msg=callable_and_arg_names_msg)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_point_2ds(*, arg_position_index: int) -> _F:
    """
    Set the validation to check a specified argument's type
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            import apysc as ap
            points: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)
            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            if (
                    not isinstance(points, list)
                    and not isinstance(points, ap.Array)):
                raise TypeError(
                    'A specified points argument type is not the list or '
                    f'ap.Array: {type(points)}'
                    f'\n{callable_and_arg_names_msg}')

            value: List[ap.Point2D] = []
            if isinstance(points, list):
                value = points
            elif isinstance(points, ap.Array):
                value = points._value
            for point in value:
                validate_point_2d_type(
                    point=point,
                    additional_err_msg=callable_and_arg_names_msg)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_path_data_list(*, arg_position_index: int) -> _F:
    """
    Set the validation to check a specified argument's type
    is the list of `ap.PathDataBase`.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            import apysc as ap
            from apysc._validation.path_validation import \
                validate_path_data_list
            path_data_list = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)

            if not isinstance(path_data_list, list):
                raise TypeError(
                    'A specified `path_data_list`\'s type is not the '
                    f'list: {type(path_data_list)}'
                    f'\n{callable_and_arg_names_msg}')

            for path_data in path_data_list:
                if isinstance(path_data, ap.PathDataBase):
                    continue
                raise TypeError(
                    'A value of path_data_list argument is not a '
                    'type of `ap.PathDataBase`\'s subclass: '
                    f'{type(path_data)}')
            validate_path_data_list(path_data_list=path_data_list)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_line_cap(
        *, arg_position_index: int,
        optional: bool) -> _F:
    """
    Set the validation to check a specified argument's type
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.display_validation import validate_line_cap
            cap: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            if not optional:
                validate_line_cap(
                    cap=cap, additional_err_msg=callable_and_arg_names_msg)
            elif cap is not None:
                validate_line_cap(
                    cap=cap, additional_err_msg=callable_and_arg_names_msg)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_line_joints(
        *, arg_position_index: int,
        optional: bool) -> _F:
    """
    Set the validation to check a specified argument's type
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.display_validation import \
                validate_line_joints
            joints: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            if not optional:
                validate_line_joints(
                    joints=joints,
                    additional_err_msg=callable_and_arg_names_msg)
            elif joints is not None:
                validate_line_joints(
                    joints=joints,
                    additional_err_msg=callable_and_arg_names_msg)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def multiple_line_settings_are_not_set(*, arg_position_index: int) -> _F:
    """
    Set the validation to check a specified argument's instance
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.display_validation import \
                validate_multiple_line_settings_are_not_set
            instance: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            result: Any = callable_(*args, **kwargs)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            validate_multiple_line_settings_are_not_set(
                any_instance=instance,
                additional_err_msg=callable_and_arg_names_msg)

            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_line_dot_setting(*, arg_position_index: int) -> _F:
    """
    Set the validation to check a specified argument's type
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
    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            import apysc as ap
            setting: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            if not isinstance(setting, (type(None), ap.LineDotSetting)):
                raise TypeError(
                    'A specified setting is not the `ap.LineDashSetting` '
                    f'type or None: {type(setting)}'
                    f'\n{callable_and_arg_names_msg}')

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_line_dash_setting(*, arg_position_index: int) -> _F:
    """
    Set the validation to check a specified argument's type
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            import apysc as ap
            setting: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            if not isinstance(setting, (type(None), ap.LineDashSetting)):
                raise TypeError(
                    'A specified setting is not the `ap.LineDashSetting`'
                    f' type or None: {type(setting)}'
                    f'\n{callable_and_arg_names_msg}')

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_line_dash_dot_setting(*, arg_position_index: int) -> _F:
    """
    Set the validation to check a specified argument's type
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            import apysc as ap
            setting: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            if not isinstance(
                    setting, (type(None), ap.LineDashDotSetting)):
                raise TypeError(
                    'A specified setting is not the '
                    '`ap.LineDashDotSetting` type or None: '
                    f'{type(setting)}'
                    f'\n{callable_and_arg_names_msg}')

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_line_round_dot_setting(*, arg_position_index: int) -> _F:
    """
    Set the validation to check a specified argument's type
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

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            import apysc as ap
            setting: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            if not isinstance(setting, (type(None), ap.LineRoundDotSetting)):
                raise TypeError(
                    'A specified setting is not the `ap.LineRoundDotSetting` '
                    f'type or None: {type(setting)}'
                    f'\n{callable_and_arg_names_msg}')

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def is_variable_name_interface_type(*, arg_position_index: int) -> _F:
    """
    Set the validation to check a specified argument's type
    is the `ap.VariableNameInterface` or its subclass type.

    Parameters
    ----------
    arg_position_index : int
        A target argument position index.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _F) -> _F:

        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            from apysc._validation.variable_name_validation import \
                validate_variable_name_interface_type
            instance: Any = _extract_arg_value(
                args=args, kwargs=kwargs,
                arg_position_index=arg_position_index, callable_=callable_)

            callable_and_arg_names_msg: str = _get_callable_and_arg_names_msg(
                callable_=callable_, arg_position_index=arg_position_index)
            validate_variable_name_interface_type(
                instance=instance,
                additional_err_msg=callable_and_arg_names_msg)

            result: Any = callable_(*args, **kwargs)
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore
