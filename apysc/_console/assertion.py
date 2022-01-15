"""Each js assertion (console.assert) interface implementations.

Mainly following interfaces are defined:

- assert_equal
    JavaScript assertion interface for equal condition.
- assert_not_equal
    JavaScript assertion interface for not equal condition.
- assert_true
    JavaScript assertion interface for true condition.
- assert_false
    JavaScript assertion interface for false condition.
- assert_arrays_equal
    JavaScript assertion interface for Array values equal condition.
- assert_arrays_not_equal
    JavaScript assertion interface for Array values not equal condition.
- assert_dicts_equal
    JavaScript assertion interface for Dictionary values equal condition.
- assert_dicts_not_equal
    JavaScript assertion interface for Dictionary values not equal
    condition.
- assert_defined
    JavaScript assertion interface for defined (not undefined)
    value condition.
- assert_undefined
    JavaScript assertion interface for undefined value condition.
"""

from typing import Any
from typing import Tuple


def assert_equal(
        left: Any, right: Any, *, msg: str = '') -> None:
    """
    JavaScript assertion interface for equal condition.

    Notes
    -----
    - If specified values are type of Array (or list, etc),
        then assert_arrays_equal function will be called instead of
        this function.
    - If specified value are type of Dictionary (or dict, etc),
        then assert_dicts_equal function will be called instead of
        this function.

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
    - assert_equal and assert_not_equal interfaces document
        - https://bit.ly/3qwx9ad

    Examples
    --------
    >>> import apysc as ap
    >>> int_1: ap.Int = ap.Int(10)
    >>> int_2: ap.Int = ap.Int(10)
    >>> ap.assert_equal(int_1, int_2)
    """
    import apysc as ap
    with ap.DebugInfo(
            callable_=assert_equal, locals_=locals(),
            module_name=__name__):
        from apysc._string import string_util
        for value in (left, right):
            if _value_type_is_array(value=value):
                assert_arrays_equal(left=left, right=right, msg=msg)
                return
        for value in (left, right):
            if _value_type_is_dict(value=value):
                assert_dicts_equal(left=left, right=right, msg=msg)
                return

        _trace_info(
            interface_label='assert_equal', left=left, right=right)

        left_str, right_str = _get_left_and_right_strs(
            left=left, right=right)

        msg = string_util.escape_str(string=msg)
        expression: str = (
            f'console.assert({left_str} === {right_str}, "{msg}");'
        )
        ap.append_js_expression(expression=expression)


def assert_not_equal(
        left: Any, right: Any, *, msg: str = '') -> None:
    """
    JavaScript assertion interface for not equal condition.

    Notes
    -----
    - If specified values are type of Array (or list, etc),
        then assert_arrays_not_equal function will be called instead of
        this function.
    - If specified value are type of Dictionary (or dict, etc),
        then assert_dicts_not_equal function will be called instead of
        this function.

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
    - assert_equal and assert_not_equal interfaces document
        - https://bit.ly/3qwx9ad

    Examples
    --------
    >>> import apysc as ap
    >>> int_1: ap.Int = ap.Int(10)
    >>> int_2: ap.Int = ap.Int(11)
    >>> ap.assert_not_equal(int_1, int_2)
    """
    import apysc as ap
    with ap.DebugInfo(
            callable_=assert_not_equal, locals_=locals(),
            module_name=__name__):
        from apysc._string import string_util
        for value in (left, right):
            if _value_type_is_array(value=value):
                assert_arrays_not_equal(left=left, right=right, msg=msg)
                return
        for value in (left, right):
            if _value_type_is_dict(value=value):
                assert_dicts_not_equal(left=left, right=right, msg=msg)
                return

        _trace_info(
            interface_label='assert_not_equal',
            left=left,
            right=right)
        left_str, right_str = _get_left_and_right_strs(
            left=left, right=right)

        msg = string_util.escape_str(string=msg)
        expression: str = (
            f'console.assert({left_str} !== {right_str}, "{msg}");'
        )
        ap.append_js_expression(expression=expression)


def assert_true(
        value: Any, *, type_strict: bool = True, msg: str = '') -> None:
    """
    JavaScript assertion interface for true condition.

    Parameters
    ----------
    value : *
        Target value to check.
    type_strict : bool, default True
        Whether strictly check actual value or not.
        For example, if type_strict is True, interger 1 will
        fail, on the contrary (if type_strict is False), integer 1
        will pass test.
    msg : str, optional
        Message to display when assertion failed.

    References
    ----------
    - assert_true and assert_false interfaces document
        - https://simon-ritchie.github.io/apysc/assert_true_and_false.html

    Examples
    --------
    >>> import apysc as ap
    >>> int_val: ap.Int = ap.Int(10)
    >>> boolean: ap.Boolean = int_val == 10
    >>> ap.assert_true(boolean)
    """
    import apysc as ap
    with ap.DebugInfo(
            callable_=assert_true, locals_=locals(),
            module_name=__name__):
        from apysc._string import string_util
        _trace_info(
            interface_label='assert_true', left='true', right=value)
        _, value_str = _get_left_and_right_strs(
            left='_', right=value)

        msg = string_util.escape_str(string=msg)
        expression: str = (
            f'console.assert({value_str} =='
        )
        expression = _add_equal_if_type_strict_setting_is_true(
            expression=expression, type_strict=type_strict)
        expression += f' true, "{msg}");'
        ap.append_js_expression(expression=expression)


def assert_false(
        value: Any, *, type_strict: bool = True, msg: str = '') -> None:
    """
    JavaScript assertion interface for false condition.

    Parameters
    ----------
    value : *
        Target value to check.
    type_strict : bool, default True
        Whether strictly check actual value or not.
        For example, if type_strict is True, interger 0 will
        fail, on the contrary (if type_strict is False), integer 0
        will pass test.
    msg : str, optional
        Message to display when assertion failed.

    References
    ----------
    - assert_true and assert_false interfaces document
        - https://simon-ritchie.github.io/apysc/assert_true_and_false.html

    Examples
    --------
    >>> import apysc as ap
    >>> int_val: ap.Int = ap.Int(10)
    >>> boolean: ap.Boolean = int_val == 11
    >>> ap.assert_false(boolean)
    """
    import apysc as ap
    with ap.DebugInfo(
            callable_=assert_false, locals_=locals(),
            module_name=__name__):
        from apysc._string import string_util
        _trace_info(
            interface_label='assert_false', left='false', right=value)
        _, value_str = _get_left_and_right_strs(
            left='_', right=value)

        msg = string_util.escape_str(string=msg)
        expression: str = (
            f'console.assert({value_str} =='
        )
        expression = _add_equal_if_type_strict_setting_is_true(
            expression=expression, type_strict=type_strict)
        expression += f' false, "{msg}");'
        ap.append_js_expression(expression=expression)


def assert_arrays_equal(
        left: Any, right: Any, *, msg: str = '') -> None:
    """
    JavaScript assertion interface for Array values equal condition.

    Notes
    -----
    This is used instead of assert_equal for Array class
    comparison (JavaScript can not compare arrays directly, like
    a Python, for example, `[1, 2] === [1, 2]` will be false).

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
    - assert_arrays_equal and assert_arrays_not_equal interfaces document
        - https://bit.ly/3I6CgUf

    Examples
    --------
    >>> import apysc as ap
    >>> arr_1: ap.Array = ap.Array([1, 2, 3])
    >>> arr_2: ap.Array = ap.Array([1, 2, 3])
    >>> ap.assert_arrays_equal(arr_1, arr_2)
    """
    import apysc as ap
    with ap.DebugInfo(
            callable_=assert_arrays_equal, locals_=locals(),
            module_name=__name__):
        _trace_arrays_or_dicts_assertion_info(
            interface_label='assert_arrays_equal',
            left=left, right=right)

        expression: str = _make_arrays_or_dicts_comparison_expression(
            left=left, right=right, msg=msg, not_condition=False)
        ap.append_js_expression(expression=expression)


def assert_arrays_not_equal(
        left: Any, right: Any, *, msg: str = '') -> None:
    """
    JavaScript assertion interface for Array values not equal condition.

    Notes
    -----
    This is used instead of assert_not_equal for Array class
    comparison (JavaScript can not compare arrays directly, like
    a Python, for example, `[1, 2] === [1, 2]` will be false).

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
    - assert_arrays_equal and assert_arrays_not_equal interfaces document
        - https://bit.ly/3I6CgUf

    Examples
    --------
    >>> import apysc as ap
    >>> arr_1: ap.Array = ap.Array([1, 2, 3])
    >>> arr_2: ap.Array = ap.Array([4, 5, 6])
    >>> ap.assert_arrays_not_equal(arr_1, arr_2)
    """
    import apysc as ap
    with ap.DebugInfo(
            callable_=assert_arrays_not_equal, locals_=locals(),
            module_name=__name__):
        _trace_arrays_or_dicts_assertion_info(
            interface_label='assert_arrays_not_equal',
            left=left, right=right)

        expression: str = _make_arrays_or_dicts_comparison_expression(
            left=left, right=right, msg=msg, not_condition=True)
        ap.append_js_expression(expression=expression)


def assert_dicts_equal(left: Any, right: Any, *, msg: str = '') -> None:
    """
    JavaScript assertion interface for Dictionary values equal
    condition.

    Notes
    -----
    This is used instead of assert_equal for Dictionary class
    comparison (JavaScript can not compare dictionary (Object)
    directly, like a Python, for example, `{"a": 10} === {"a": 10}`
    will be false).

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
    - assert_dicts_equal and assert_dicts_not_equal interfaces document
        - https://bit.ly/3GxWLJ4

    Examples
    --------
    >>> import apysc as ap
    >>> dict_1: ap.Dictionary = ap.Dictionary({'a': 10})
    >>> dict_2: ap.Dictionary = ap.Dictionary({'a': 10})
    >>> ap.assert_dicts_equal(dict_1, dict_2)
    """
    import apysc as ap
    with ap.DebugInfo(
            callable_=assert_dicts_equal, locals_=locals(),
            module_name=__name__):
        _trace_arrays_or_dicts_assertion_info(
            interface_label='assert_dicts_equal',
            left=left, right=right)

        expression: str = _make_arrays_or_dicts_comparison_expression(
            left=left, right=right, msg=msg, not_condition=False)
        ap.append_js_expression(expression=expression)


def assert_dicts_not_equal(
        left: Any, right: Any, *, msg: str = '') -> None:
    """
    JavaScript assertion interface for Dictionary values not equal
    condition.

    Notes
    -----
    This is used instead of assert_not_equal for Dictionary class
    comparison (JavaScript can not compare dictionary (Object)
    directly, like a Python, for example, `{"a": 10} !== {"a": 10}`
    will be true).

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
    - assert_dicts_equal and assert_dicts_not_equal interfaces document
        - https://bit.ly/3GxWLJ4

    Examples
    --------
    >>> import apysc as ap
    >>> dict_1: ap.Dictionary = ap.Dictionary({'a': 10})
    >>> dict_2: ap.Dictionary = ap.Dictionary({'a': 20})
    >>> ap.assert_dicts_not_equal(dict_1, dict_2)
    """
    import apysc as ap
    with ap.DebugInfo(
            callable_=assert_dicts_not_equal, locals_=locals(),
            module_name=__name__):
        _trace_arrays_or_dicts_assertion_info(
            interface_label='assert_dicts_not_equal',
            left=left, right=right)

        expression: str = _make_arrays_or_dicts_comparison_expression(
            left=left, right=right, msg=msg, not_condition=True)
        ap.append_js_expression(expression=expression)


def assert_defined(value: Any, *, msg: str = '') -> None:
    """
    JavaScript assertion interface for defined (not undefined)
    value condition.

    Parameters
    ----------
    value : *
        Target value to check.
    msg : str, optional
        Message to display when assertion failed.

    References
    ----------
    - assert_defined and assert_undefined interfaces document
        - https://bit.ly/3A2bmKz

    Examples
    --------
    >>> import apysc as ap
    >>> int_val: ap.Int = ap.Int(10)
    >>> ap.assert_defined(int_val)
    """
    import apysc as ap
    with ap.DebugInfo(
            callable_=assert_defined, locals_=locals(),
            module_name=__name__):
        from apysc._string import string_util
        _trace_info(
            interface_label='assert_defined', left='other than undefined',
            right=value)
        _, value_str = _get_left_and_right_strs(
            left='_', right=value)

        msg = string_util.escape_str(string=msg)
        expression: str = (
            f'console.assert(!_.isUndefined({value_str}), "{msg}");'
        )
        ap.append_js_expression(expression=expression)


def assert_undefined(value: Any, *, msg: str = '') -> None:
    """
    JavaScript assertion interface for undefined value condition.

    Parameters
    ----------
    value : *
        Target value to check.
    msg : str, optional
        Message to display when assertion failed.

    References
    ----------
    - assert_defined and assert_undefined interfaces document
        - https://bit.ly/3A2bmKz

    Examples
    --------
    >>> import apysc as ap
    >>> int_val: ap.Int = ap.Int(10)
    >>> ap.append_js_expression(
    ...     expression=f'{int_val.variable_name} = undefined;')
    >>> ap.assert_undefined(int_val)
    """
    import apysc as ap
    with ap.DebugInfo(
            callable_=assert_undefined, locals_=locals(),
            module_name=__name__):
        from apysc._string import string_util
        _trace_info(
            interface_label='assert_undefined', left='undefined',
            right=value)
        _, value_str = _get_left_and_right_strs(
            left='_', right=value)

        msg = string_util.escape_str(string=msg)
        expression: str = (
            f'console.assert(_.isUndefined({value_str}), "{msg}");'
        )
        ap.append_js_expression(expression=expression)


def _make_arrays_or_dicts_comparison_expression(
        *, left: Any, right: Any, msg: str,
        not_condition: bool) -> str:
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
        Result expression string.
    """
    import apysc as ap
    with ap.DebugInfo(
            callable_=_make_arrays_or_dicts_comparison_expression,
            locals_=locals(),
            module_name=__name__):
        from apysc._string import string_util
        from apysc._type import value_util
        left_exp_str: str = value_util.get_value_str_for_expression(
            value=left)
        right_exp_str: str = value_util.get_value_str_for_expression(
            value=right)
        msg = string_util.escape_str(string=msg)
        if not_condition:
            not_condition_str: str = '!'
        else:
            not_condition_str = ''
        expression: str = (
            f'console.assert({not_condition_str}_.isEqual({left_exp_str}, '
            f'{right_exp_str}), "{msg}");'
        )
        return expression


def _trace_arrays_or_dicts_assertion_info(
        *, interface_label: str, left: Any, right: Any) -> None:
    """
    Append arrays or dicts value's information trace expression.

    Parameters
    ----------
    interface_label : str
        Target assertion interface label, e.g., 'assert_arrays_equal'.
    left : *
        Left-side value to compare.
    right : *
        Right-side value to compare.
    """
    import apysc as ap
    with ap.DebugInfo(
            callable_=_trace_arrays_or_dicts_assertion_info, locals_=locals(),
            module_name=__name__):
        from apysc._type import value_util
        left_exp_str: str = value_util.get_value_str_for_expression(
            value=left)
        if isinstance(left, dict):
            left_exp_str = left_exp_str.replace('"', '')
        right_exp_str: str = value_util.get_value_str_for_expression(
            value=right)
        if isinstance(right, dict):
            right_exp_str = right_exp_str.replace('"', '')
        if isinstance(left, (ap.Array, ap.Dictionary)):
            value_str: str = value_util.get_value_str_for_expression(
                value=left.value)
            value_str = value_str.replace('"', '')
            left_info_str: str = f'{left_exp_str} ({value_str})'
        else:
            left_info_str = left_exp_str
        right_info_str = right_exp_str
        _trace_info(
            interface_label=interface_label,
            left=left_info_str,
            right=right_info_str)


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
        If the value type is Array, True will be returned.
    """
    import apysc as ap
    if isinstance(value, ap.Array):
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
        If the value type is Dictionary, True will be returned.
    """
    from apysc._type.dictionary_structure import DictionaryStructure
    if isinstance(value, DictionaryStructure):
        return True
    return False


def _add_equal_if_type_strict_setting_is_true(
        *, expression: str, type_strict: bool) -> str:
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
        If type_string setting is true, then single equal character
        will be added to tail.
    """
    if not type_strict:
        return expression
    expression += '='
    return expression


def _get_left_and_right_strs(
        *, left: Any, right: Any) -> Tuple[str, str]:
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
        Left-side value's string. If value is string, this will be
        wrapped by double quotation.
    right_str : str
        Right-side value's string. If value is string, this will be
        wrapped by double quotation.
    """
    from apysc._type import value_util
    left_str: str = value_util.get_value_str_for_expression(
        value=left)
    right_str: str = value_util.get_value_str_for_expression(value=right)
    return left_str, right_str


def _trace_info(*, interface_label: str, left: Any, right: Any) -> None:
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
    """
    import apysc as ap
    with ap.DebugInfo(
            callable_=_trace_info, locals_=locals(),
            module_name=__name__):
        from apysc._type.variable_name_interface import VariableNameInterface
        info: str = f'[{interface_label}]'
        if isinstance(left, VariableNameInterface):
            info += f'\nLeft-side variable name: {left.variable_name}'
        if isinstance(right, VariableNameInterface):
            info += f'\nRight-side variable name: {right.variable_name}'
        ap.trace(info, '\nLeft value:', left, 'right value:', right)
