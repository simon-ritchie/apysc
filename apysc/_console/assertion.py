"""Each js assertion (console.assert) interface implementations.

Mainly following interfaces are defined:

- assert_equal
    JavaScript assertion interface for the equal condition.
- assert_not_equal
    JavaScript assertion interface for the not equal condition.
- assert_true
    JavaScript assertion interface for the true condition.
- assert_false
    JavaScript assertion interface for the false condition.
- assert_greater
    JavaScript assertion interface for the greater than condition.
- assert_greater_equal
    JavaScript assertion interface for the greater than or equal to condition.
- assert_less
    JavaScript assertion interface for the less than condition.
- assert_less_equal
    JavaScript assertion interface for the less than or equal to condition.
- assert_arrays_equal
    JavaScript assertion interface for the Array values equal condition.
- assert_arrays_not_equal
    JavaScript assertion interface for the Array values not equal condition.
- assert_dicts_equal
    JavaScript assertion interface for the Dictionary values equal condition.
- assert_dicts_not_equal
    JavaScript assertion interface for the Dictionary values not equal
    condition.
- assert_defined
    JavaScript assertion interface for the defined (not undefined)
    value condition.
- assert_undefined
    JavaScript assertion interface for the undefined value condition.
"""

from typing import Any
from typing import Tuple
from typing import Union

from apysc._console._trace import DEFAULT_OUTER_FRAMES_INDEX
from apysc._console._trace import TemporaryOuterFramesIndexAdjustment
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.number import Number


@add_debug_info_setting(module_name=__name__)
def assert_equal(left: Any, right: Any, *, msg: str = "") -> None:
    """
    JavaScript assertion interface for the equal condition.

    Notes
    -----
    - If specified values are types of Array (or list),
        then this interface calls the assert_arrays_equal
        function instead.
    - If specified values are types of Dictionary (or dict),
        then this interface calls the assert_dicts_equal instead.

    Parameters
    ----------
    left : *
        Left-side value to compare.
    right : *
        Right-side value to compare.
    msg : str, optional
        Message to display when assertion failed.

    References
    ----------
    - assert_equal and assert_not_equal interfaces
        - https://simon-ritchie.github.io/apysc/en/assert_equal_and_not_equal.html  # noqa

    Examples
    --------
    >>> import apysc as ap
    >>> int_1: ap.Int = ap.Int(10)
    >>> int_2: ap.Int = ap.Int(10)
    >>> ap.assert_equal(int_1, int_2)
    """
    from apysc._expression import expression_data_util
    from apysc._string import string_util

    for value in (left, right):
        if _value_type_is_array(value=value):
            assert_arrays_equal(
                left=left, right=right, msg=msg, outer_frames_index_adjustment=2
            )
            return
    for value in (left, right):
        if _value_type_is_dict(value=value):
            assert_dicts_equal(
                left=left, right=right, msg=msg, outer_frames_index_adjustment=2
            )
            return

    _trace_info(
        interface_label=assert_equal.__name__,
        left=left,
        right=right,
        outer_frames_index_adjustment=4,
    )

    left_str: str
    right_str: str
    left_str, right_str = _get_left_and_right_strs(left=left, right=right)

    msg = string_util.escape_str(string=msg)
    expression: str = f'console.assert({left_str} === {right_str}, "{msg}");'
    expression_data_util.append_js_expression(expression=expression)


@add_debug_info_setting(module_name=__name__)
def assert_not_equal(left: Any, right: Any, *, msg: str = "") -> None:
    """
    JavaScript assertion interface for the not equal condition.

    Notes
    -----
    - If specified values are types of Array (or list),
        then this interface calls the assert_arrays_not_equal
        function instead.
    - If specified values are types of Dictionary (or dict),
        this interface calls the assert_dicts_not_equal
        function instead.

    Parameters
    ----------
    left : *
        Left-side value to compare.
    right : *
        Right-side value to compare.
    msg : str, optional
        Message to display when assertion failed.

    References
    ----------
    - assert_equal and assert_not_equal interfaces
        - https://simon-ritchie.github.io/apysc/en/assert_equal_and_not_equal.html  # noqa

    Examples
    --------
    >>> import apysc as ap
    >>> int_1: ap.Int = ap.Int(10)
    >>> int_2: ap.Int = ap.Int(11)
    >>> ap.assert_not_equal(int_1, int_2)
    """
    from apysc._expression import expression_data_util
    from apysc._string import string_util

    for value in (left, right):
        if _value_type_is_array(value=value):
            assert_arrays_not_equal(
                left=left, right=right, msg=msg, outer_frames_index_adjustment=2
            )
            return
    for value in (left, right):
        if _value_type_is_dict(value=value):
            assert_dicts_not_equal(
                left=left, right=right, msg=msg, outer_frames_index_adjustment=2
            )
            return

    _trace_info(
        interface_label=assert_not_equal.__name__,
        left=left,
        right=right,
        outer_frames_index_adjustment=4,
    )
    left_str: str
    right_str: str
    left_str, right_str = _get_left_and_right_strs(left=left, right=right)

    msg = string_util.escape_str(string=msg)
    expression: str = f'console.assert({left_str} !== {right_str}, "{msg}");'
    expression_data_util.append_js_expression(expression=expression)


@add_debug_info_setting(module_name=__name__)
def assert_true(value: Any, *, type_strict: bool = True, msg: str = "") -> None:
    """
    JavaScript assertion interface for the true condition.

    Parameters
    ----------
    value : *
        Target value to check.
    type_strict : bool, default True
        Whether strictly check actual value or not.
        For example, if type_strict is True,
        an integer of 1 fails tests. On the contrary
        (if type_strict is False), an integer of 1 passes tests.
    msg : str, optional
        Message to display when assertion failed.

    References
    ----------
    - assert_true and assert_false interfaces
        - https://simon-ritchie.github.io/apysc/en/assert_true_and_false.html

    Examples
    --------
    >>> import apysc as ap
    >>> int_val: ap.Int = ap.Int(10)
    >>> boolean: ap.Boolean = int_val == 10
    >>> ap.assert_true(boolean)
    """
    from apysc._expression import expression_data_util
    from apysc._string import string_util

    _trace_info(
        interface_label=assert_true.__name__,
        left="true",
        right=value,
        outer_frames_index_adjustment=4,
    )
    _, value_str = _get_left_and_right_strs(left="_", right=value)

    msg = string_util.escape_str(string=msg)
    expression: str = f"console.assert({value_str} =="
    expression = _add_equal_if_type_strict_setting_is_true(
        expression=expression, type_strict=type_strict
    )
    expression += f' true, "{msg}");'
    expression_data_util.append_js_expression(expression=expression)


@add_debug_info_setting(module_name=__name__)
def assert_false(value: Any, *, type_strict: bool = True, msg: str = "") -> None:
    """
    JavaScript assertion interface for the false condition.

    Parameters
    ----------
    value : *
        Target value to check.
    type_strict : bool, default True
        Whether strictly check actual value or not.
        For example, if type_strict is True, an integer
        of 0 fails tests. On the contrary (if type_strict
        is False), an integer of 0 passes tests.
    msg : str, optional
        Message to display when assertion failed.

    References
    ----------
    - assert_true and assert_false interfaces
        - https://simon-ritchie.github.io/apysc/en/assert_true_and_false.html

    Examples
    --------
    >>> import apysc as ap
    >>> int_val: ap.Int = ap.Int(10)
    >>> boolean: ap.Boolean = int_val == 11
    >>> ap.assert_false(boolean)
    """
    from apysc._expression import expression_data_util
    from apysc._string import string_util

    _trace_info(
        interface_label=assert_false.__name__,
        left="false",
        right=value,
        outer_frames_index_adjustment=4,
    )
    _, value_str = _get_left_and_right_strs(left="_", right=value)

    msg = string_util.escape_str(string=msg)
    expression: str = f"console.assert({value_str} =="
    expression = _add_equal_if_type_strict_setting_is_true(
        expression=expression, type_strict=type_strict
    )
    expression += f' false, "{msg}");'
    expression_data_util.append_js_expression(expression=expression)


@add_debug_info_setting(module_name=__name__)
def assert_greater(
    left: Union[int, float, Int, Number],
    right: Union[int, float, Int, Number],
    *,
    msg: str = "",
) -> None:
    """
    JavaScript assertion interface for the greater than condition.

    Parameters
    ----------
    left : Union[int, float, Int, Number]
        Left-side (greater) value to compare.
    right : Union[int, float, Int, Number]
        Right-side (less) value to compare.
    msg : str, optional
        Message to display when assertion failed.

    Examples
    --------
    >>> import apysc as ap
    >>> int_val_1: ap.Int = ap.Int(10)
    >>> int_val_2: ap.Int = ap.Int(9)
    >>> ap.assert_greater(left=int_val_1, right=int_val_2)
    """
    from apysc._expression import expression_data_util
    from apysc._string import string_util

    _trace_info(
        interface_label=assert_greater.__name__,
        left=left,
        right=right,
        outer_frames_index_adjustment=4,
    )
    left_str: str
    right_str: str
    left_str, right_str = _get_left_and_right_strs(left=left, right=right)
    msg = string_util.escape_str(string=msg)
    expression: str = f'console.assert({left_str} > {right_str}, "{msg}");'
    expression_data_util.append_js_expression(expression=expression)


@add_debug_info_setting(module_name=__name__)
def assert_greater_equal(
    left: Union[int, float, Int, Number],
    right: Union[int, float, Int, Number],
    *,
    msg: str = "",
) -> None:
    """
    JavaScript assertion interface for the greater than or equal to condition.

    Parameters
    ----------
    left : Union[int, float, Int, Number]
        Left-side (greater) value to compare.
    right : Union[int, float, Int, Number]
        Right-side (less) value to compare.
    msg : str, optional
        Message to display when assertion failed.

    Examples
    --------
    >>> import apysc as ap
    >>> int_val_1: ap.Int = ap.Int(10)
    >>> int_val_2: ap.Int = ap.Int(9)
    >>> ap.assert_greater_equal(left=int_val_1, right=int_val_2)
    >>> int_val_3: ap.Int = ap.Int(10)
    >>> ap.assert_greater_equal(left=int_val_1, right=int_val_3)
    """
    from apysc._expression import expression_data_util
    from apysc._string import string_util

    _trace_info(
        interface_label=assert_greater_equal.__name__,
        left=left,
        right=right,
        outer_frames_index_adjustment=4,
    )
    left_str: str
    right_str: str
    left_str, right_str = _get_left_and_right_strs(left=left, right=right)
    msg = string_util.escape_str(string=msg)
    expression: str = f'console.assert({left_str} >= {right_str}, "{msg}");'
    expression_data_util.append_js_expression(expression=expression)


@add_debug_info_setting(module_name=__name__)
def assert_less(
    left: Union[int, float, Int, Number],
    right: Union[int, float, Int, Number],
    *,
    msg: str = "",
) -> None:
    """
    JavaScript assertion interface for the less than condition.

    Parameters
    ----------
    left : Union[int, float, Int, Number]
        Left-side (less) value to compare.
    right : Union[int, float, Int, Number]
        Right-side (greater) value to compare.
    msg : str, optional
        Message to display when assertion failed.

    Examples
    --------
    >>> import apysc as ap
    >>> int_val_1: ap.Int = ap.Int(9)
    >>> int_val_2: ap.Int = ap.Int(10)
    >>> ap.assert_greater_equal(left=int_val_1, right=int_val_2)
    """
    from apysc._expression import expression_data_util
    from apysc._string import string_util

    _trace_info(
        interface_label=assert_less.__name__,
        left=left,
        right=right,
        outer_frames_index_adjustment=4,
    )
    left_str: str
    right_str: str
    left_str, right_str = _get_left_and_right_strs(left=left, right=right)
    msg = string_util.escape_str(string=msg)
    expression: str = f'console.assert({left_str} < {right_str}, "{msg}");'
    expression_data_util.append_js_expression(expression=expression)


@add_debug_info_setting(module_name=__name__)
def assert_less_equal(
    left: Union[int, float, Int, Number],
    right: Union[int, float, Int, Number],
    *,
    msg: str = "",
) -> None:
    """
    JavaScript assertion interface for the less than or equal to condition.

    Parameters
    ----------
    left : Union[int, float, Int, Number]
        Left-side (less) value to compare.
    right : Union[int, float, Int, Number]
        Right-side (greater) value to compare.
    msg : str, optional
        Message to display when assertion failed.

    Examples
    --------
    >>> import apysc as ap
    >>> int_val_1: ap.Int = ap.Int(9)
    >>> int_val_2: ap.Int = ap.Int(10)
    >>> ap.assert_greater_equal(left=int_val_1, right=int_val_2)
    >>> int_val_3: ap.Int = ap.Int(9)
    >>> ap.assert_greater_equal(left=int_val_1, right=int_val_3)
    """
    from apysc._expression import expression_data_util
    from apysc._string import string_util

    _trace_info(
        interface_label=assert_less_equal.__name__,
        left=left,
        right=right,
        outer_frames_index_adjustment=4,
    )
    left_str: str
    right_str: str
    left_str, right_str = _get_left_and_right_strs(left=left, right=right)
    msg = string_util.escape_str(string=msg)
    expression: str = f'console.assert({left_str} <= {right_str}, "{msg}");'
    expression_data_util.append_js_expression(expression=expression)


@add_debug_info_setting(module_name=__name__)
def assert_arrays_equal(
    left: Any, right: Any, *, msg: str = "", outer_frames_index_adjustment: int = 0
) -> None:
    """
    JavaScript assertion interface for the Array values equal condition.

    Notes
    -----
    This interface is used instead of assert_equal for
    Array class comparison (JavaScript can not compare
    arrays directly, like a Python, for example,
    `[1, 2] === [1, 2]` becomes false).

    Parameters
    ----------
    left : *
        Left-side value to compare.
    right : *
        Right-side value to compare.
    msg : str, optional
        Message to display when assertion failed.
    outer_frames_index_adjustment : int, optional
        The trace's outer frames index adjustment setting.
        This function uses this argument to adjust the caller's information.
        Also, this function only uses this argument in internal logic.

    References
    ----------
    - assert_arrays_equal and assert_arrays_not_equal interfaces
        - https://simon-ritchie.github.io/apysc/en/assert_arrays_equal_and_arrays_not_equal.html  # noqa

    Examples
    --------
    >>> import apysc as ap
    >>> _ = ap.Stage()
    >>> arr_1: ap.Array = ap.Array([1, 2, 3])
    >>> arr_2: ap.Array = ap.Array([1, 2, 3])
    >>> ap.assert_arrays_equal(arr_1, arr_2)
    """
    from apysc._expression import expression_data_util

    _trace_arrays_or_dicts_assertion_info(
        interface_label=assert_arrays_equal.__name__,
        left=left,
        right=right,
        outer_frames_index_adjustment=outer_frames_index_adjustment + 5,
    )

    expression: str = _make_arrays_or_dicts_comparison_expression(
        left=left, right=right, msg=msg, not_condition=False
    )
    expression_data_util.append_js_expression(expression=expression)


@add_debug_info_setting(module_name=__name__)
def assert_arrays_not_equal(
    left: Any, right: Any, *, msg: str = "", outer_frames_index_adjustment: int = 0
) -> None:
    """
    JavaScript assertion interface for the Array values not equal condition.

    Notes
    -----
    This interface is used instead of assert_not_equal for
    Array class comparison (JavaScript can not compare arrays
    directly, like a Python, for example,
    `[1, 2] === [1, 2]` becomes false).

    Parameters
    ----------
    left : *
        Left-side value to compare.
    right : *
        Right-side value to compare.
    msg : str, optional
        Message to display when assertion failed.
    outer_frames_index_adjustment : int, optional
        The trace's outer frames index adjustment setting.
        This function uses this argument to adjust the caller's information.
        Also, this function only uses this argument in internal logic.

    References
    ----------
    - assert_arrays_equal and assert_arrays_not_equal interfaces
        - https://simon-ritchie.github.io/apysc/en/assert_arrays_equal_and_arrays_not_equal.html  # noqa

    Examples
    --------
    >>> import apysc as ap
    >>> _ = ap.Stage()
    >>> arr_1: ap.Array = ap.Array([1, 2, 3])
    >>> arr_2: ap.Array = ap.Array([4, 5, 6])
    >>> ap.assert_arrays_not_equal(arr_1, arr_2)
    """
    from apysc._expression import expression_data_util

    _trace_arrays_or_dicts_assertion_info(
        interface_label=assert_arrays_not_equal.__name__,
        left=left,
        right=right,
        outer_frames_index_adjustment=outer_frames_index_adjustment + 5,
    )

    expression: str = _make_arrays_or_dicts_comparison_expression(
        left=left, right=right, msg=msg, not_condition=True
    )
    expression_data_util.append_js_expression(expression=expression)


@add_debug_info_setting(module_name=__name__)
def assert_dicts_equal(
    left: Any, right: Any, *, msg: str = "", outer_frames_index_adjustment: int = 0
) -> None:
    """
    JavaScript assertion interface for the Dictionary values equal
    condition.

    Notes
    -----
    This interface is used instead of assert_equal for
    Dictionary class comparison (JavaScript can not compare
    dictionary (Object) directly, like a Python, for example,
    `{"a": 10} === {"a": 10}` becomes false).

    Parameters
    ----------
    left : *
        Left-side value to compare.
    right : *
        Right-side value to compare.
    msg : str, optional
        Message to display when assertion failed.
    outer_frames_index_adjustment : int, optional
        The trace's outer frames index adjustment setting.
        This function uses this argument to adjust the caller's information.
        Also, this function only uses this argument in internal logic.

    References
    ----------
    - assert_dicts_equal and assert_dicts_not_equal interfaces
        - https://simon-ritchie.github.io/apysc/en/assert_dicts_equal_and_dicts_not_equal.html  # noqa

    Examples
    --------
    >>> import apysc as ap
    >>> dict_1: ap.Dictionary = ap.Dictionary({"a": 10})
    >>> dict_2: ap.Dictionary = ap.Dictionary({"a": 10})
    >>> ap.assert_dicts_equal(dict_1, dict_2)
    """
    from apysc._expression import expression_data_util

    _trace_arrays_or_dicts_assertion_info(
        interface_label=assert_dicts_equal.__name__,
        left=left,
        right=right,
        outer_frames_index_adjustment=outer_frames_index_adjustment + 5,
    )

    expression: str = _make_arrays_or_dicts_comparison_expression(
        left=left, right=right, msg=msg, not_condition=False
    )
    expression_data_util.append_js_expression(expression=expression)


@add_debug_info_setting(module_name=__name__)
def assert_dicts_not_equal(
    left: Any, right: Any, *, msg: str = "", outer_frames_index_adjustment: int = 0
) -> None:
    """
    JavaScript assertion interface for the Dictionary values not equal
    condition.

    Notes
    -----
    This interface is used instead of assert_not_equal for
    Dictionary class comparison (JavaScript can not
    compare dictionary (Object) directly, like a Python,
    for example, `{"a": 10} !== {"a": 10}` becomes true).

    Parameters
    ----------
    left : *
        Left-side value to compare.
    right : *
        Right-side value to compare.
    msg : str, optional
        Message to display when assertion failed.
    outer_frames_index_adjustment : int, optional
        The trace's outer frames index adjustment setting.
        This function uses this argument to adjust the caller's information.
        Also, this function only uses this argument in internal logic.

    References
    ----------
    - assert_dicts_equal and assert_dicts_not_equal interfaces
        - https://simon-ritchie.github.io/apysc/en/assert_dicts_equal_and_dicts_not_equal.html  # noqa

    Examples
    --------
    >>> import apysc as ap
    >>> dict_1: ap.Dictionary = ap.Dictionary({"a": 10})
    >>> dict_2: ap.Dictionary = ap.Dictionary({"a": 20})
    >>> ap.assert_dicts_not_equal(dict_1, dict_2)
    """
    from apysc._expression import expression_data_util

    _trace_arrays_or_dicts_assertion_info(
        interface_label=assert_dicts_not_equal.__name__,
        left=left,
        right=right,
        outer_frames_index_adjustment=outer_frames_index_adjustment + 5,
    )

    expression: str = _make_arrays_or_dicts_comparison_expression(
        left=left, right=right, msg=msg, not_condition=True
    )
    expression_data_util.append_js_expression(expression=expression)


@add_debug_info_setting(module_name=__name__)
def assert_defined(value: Any, *, msg: str = "") -> None:
    """
    JavaScript assertion interface for the defined (not undefined)
    value condition.

    Parameters
    ----------
    value : *
        Target value to check.
    msg : str, optional
        Message to display when assertion failed.

    References
    ----------
    - assert_defined and assert_undefined interfaces
        - https://simon-ritchie.github.io/apysc/en/assert_defined_and_undefined.html  # noqa

    Examples
    --------
    >>> import apysc as ap
    >>> int_val: ap.Int = ap.Int(10)
    >>> ap.assert_defined(int_val)
    """
    from apysc._expression import expression_data_util
    from apysc._string import string_util

    _trace_info(
        interface_label=assert_defined.__name__,
        left="other than undefined",
        right=value,
        outer_frames_index_adjustment=4,
    )
    _, value_str = _get_left_and_right_strs(left="_", right=value)

    msg = string_util.escape_str(string=msg)
    expression: str = f'console.assert(!_.isUndefined({value_str}), "{msg}");'
    expression_data_util.append_js_expression(expression=expression)


@add_debug_info_setting(module_name=__name__)
def assert_undefined(value: Any, *, msg: str = "") -> None:
    """
    JavaScript assertion interface for the undefined value condition.

    Parameters
    ----------
    value : *
        Target value to check.
    msg : str, optional
        Message to display when assertion failed.

    References
    ----------
    - assert_defined and assert_undefined interfaces
        - https://simon-ritchie.github.io/apysc/en/assert_defined_and_undefined.html  # noqa

    Examples
    --------
    >>> import apysc as ap
    >>> int_val: ap.Int = ap.Int(10)
    >>> ap.append_js_expression(expression=f"{int_val.variable_name} = undefined;")
    >>> ap.assert_undefined(int_val)
    """
    from apysc._expression import expression_data_util
    from apysc._string import string_util

    _trace_info(
        interface_label=assert_undefined.__name__,
        left="undefined",
        right=value,
        outer_frames_index_adjustment=4,
    )
    _, value_str = _get_left_and_right_strs(left="_", right=value)

    msg = string_util.escape_str(string=msg)
    expression: str = f'console.assert(_.isUndefined({value_str}), "{msg}");'
    expression_data_util.append_js_expression(expression=expression)


@add_debug_info_setting(module_name=__name__)
def _make_arrays_or_dicts_comparison_expression(
    *, left: Any, right: Any, msg: str, not_condition: bool
) -> str:
    """
    Make arrays or dicts comparison (assert_arrays_equal,
    assert_arrays_not_equal, assert_dicts_equal, or
    assert_dicts_not_equal) expression string.

    Parameters
    ----------
    left : *
        Left-side value to compare.
    right : *
        Right-side value to compare.
    msg : str, optional
        Message to display when assertion failed.
    not_condition : bool
        Boolean value whether this expression is not condition
        (assert_arrays_not_equal) or not.

    Returns
    -------
    expression : str
        A result expression string.
    """
    from apysc._string import string_util
    from apysc._type import value_util

    left_exp_str: str = value_util.get_value_str_for_expression(value=left)
    right_exp_str: str = value_util.get_value_str_for_expression(value=right)
    msg = string_util.escape_str(string=msg)
    if not_condition:
        not_condition_str: str = "!"
    else:
        not_condition_str = ""
    expression: str = (
        f"console.assert({not_condition_str}_.isEqual({left_exp_str}, "
        f'{right_exp_str}), "{msg}");'
    )
    return expression


@add_debug_info_setting(module_name=__name__)
def _trace_arrays_or_dicts_assertion_info(
    *,
    interface_label: str,
    left: Any,
    right: Any,
    outer_frames_index_adjustment: int,
) -> None:
    """
    Append arrays or dictionaries values' information
    trace expression.

    Parameters
    ----------
    interface_label : str
        Target assertion interface label, e.g., 'assert_arrays_equal'.
    left : *
        Left-side value to compare.
    right : *
        Right-side value to compare.
    outer_frames_index_adjustment : int
        The trace's outer frames index adjustment setting.
        This function uses this argument to adjust the caller's information.
    """
    from apysc._type import value_util
    from apysc._type.array import Array
    from apysc._type.dictionary import Dictionary

    left_exp_str: str = value_util.get_value_str_for_expression(value=left)
    if isinstance(left, dict):
        left_exp_str = left_exp_str.replace('"', "")
    right_exp_str: str = value_util.get_value_str_for_expression(value=right)
    if isinstance(right, dict):
        right_exp_str = right_exp_str.replace('"', "")
    if isinstance(left, (Array, Dictionary)):
        value_str: str = value_util.get_value_str_for_expression(value=left.value)
        value_str = value_str.replace('"', "")
        left_info_str: str = f"{left_exp_str} ({value_str})"
    else:
        left_info_str = left_exp_str
    right_info_str = right_exp_str
    _trace_info(
        interface_label=interface_label,
        left=left_info_str,
        right=right_info_str,
        outer_frames_index_adjustment=outer_frames_index_adjustment + 1,
    )


def _value_type_is_array(*, value: Any) -> bool:
    """
    Get a boolean value whether the specified value is
    Array type or not.

    Parameters
    ----------
    value : *
        Target value to check.

    Returns
    -------
    result : bool
        If the value type is Array, this interface returns True.
    """
    from apysc._type.array import Array

    if isinstance(value, Array):
        return True
    return False


def _value_type_is_dict(*, value: Any) -> bool:
    """
    Get a boolean value whether the specified value is
    Dictionary type or not.

    Parameters
    ----------
    value : *
        Target value to check.

    Returns
    -------
    result : bool
        If the value type is Dictionary, this interface returns True.
    """
    from apysc._type.dictionary_structure import DictionaryStructure

    if isinstance(value, DictionaryStructure):
        return True
    return False


def _add_equal_if_type_strict_setting_is_true(
    *, expression: str, type_strict: bool
) -> str:
    """
    Add single equal character to expression if type_string setting
    is True.

    Parameters
    ----------
    expression : str
        Expression to be added.
    type_strict: bool
        Type strict setting value.

    Returns
    -------
    expression : str
        If the type_strict setting is True value,
        this interface appends a single equal character to tail.
    """
    if not type_strict:
        return expression
    expression += "="
    return expression


def _get_left_and_right_strs(*, left: Any, right: Any) -> Tuple[str, str]:
    """
    Get left and right value strings from specified values.

    Parameters
    ----------
    left : *
        Left-side value to compare.
    right : *
        Right-side value to compare.

    Returns
    -------
    left_str : str
        Left-side value's string. If a value is a string,
        this interface wraps this left-side value by
        double quotation.
    right_str : str
        Right-side value's string. If a value is a string,
        this interface wraps this right-side value by
        double quotation.
    """
    from apysc._string import string_util
    from apysc._type import value_util

    if isinstance(left, str):
        left = string_util.escape_str(string=left)
    if isinstance(right, str):
        right = string_util.escape_str(string=right)

    left_str: str = value_util.get_value_str_for_expression(value=left)
    right_str: str = value_util.get_value_str_for_expression(value=right)
    return left_str, right_str


@add_debug_info_setting(module_name=__name__)
def _trace_info(
    *,
    interface_label: str,
    left: Any,
    right: Any,
    outer_frames_index_adjustment: int,
) -> None:
    """
    Append trace expression of specified values.

    Parameters
    ----------
    interface_label : str
        Target assertion interface label, e.g., 'assert_equal'.
    left : *
        Left-side value to compare.
    right : *
        Right-side value to compare.
    outer_frames_index_adjustment : int
        The trace's outer frames index adjustment setting.
        This function uses this argument to adjust the caller's information.
    """
    from apysc._console._trace import trace
    from apysc._type.variable_name_mixin import VariableNameMixIn

    info: str = f"[{interface_label}]"
    if isinstance(left, VariableNameMixIn):
        info += f"\nLeft-side variable name: {left.variable_name}"
    if isinstance(right, VariableNameMixIn):
        info += f"\nRight-side variable name: {right.variable_name}"
    outer_frames_index_adjustment = (
        DEFAULT_OUTER_FRAMES_INDEX + outer_frames_index_adjustment
    )
    with TemporaryOuterFramesIndexAdjustment(
        temporary_outer_frames_index_adjustments=outer_frames_index_adjustment
    ):
        trace(info, "\nLeft value:", left, "right value:", right)
