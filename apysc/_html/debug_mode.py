"""Debugging mode setting interface implementations for the HTML
and JavaScript.
"""

import inspect
import os
from typing import Any
from typing import Callable
from typing import Dict
from typing import Optional
from typing import Type
from typing import Union

from apysc._display.stage import Stage
from apysc._expression.indent_num import Indent


def set_debug_mode(stage: Stage) -> None:
    """
    Set the debug mode for the HTML and JavaScript debugging.
    If this functions is called, the following setting will be applied:
    - HTML minify setting will be disabled.
    - Per each interface JavaScript divider string will be appended.

    Parameters
    ----------
    stage : Stage
        A current project stage instance.
    """
    from apysc._expression import expression_file_util
    from apysc._validation.display_validation import validate_stage
    validate_stage(stage=stage)
    file_path: str = expression_file_util.DEBUG_MODE_SETTING_FILE_PATH
    with open(file_path, 'w') as f:
        f.write('1')


def unset_debug_mode() -> None:
    """
    Unset the debug mode for the HTML and JavaScript debugging.
    """
    from apysc._expression import expression_file_util
    from apysc._file import file_util
    file_path: str = expression_file_util.DEBUG_MODE_SETTING_FILE_PATH
    file_util.remove_file_if_exists(file_path=file_path)


def is_debug_mode() -> bool:
    """
    Get a boolean value whether the current debug mode is enabled or not.

    Returns
    -------
    result : bool
        If the current debug mode is enabled, True will be returned.
    """
    from apysc._expression import expression_file_util
    file_path: str = expression_file_util.DEBUG_MODE_SETTING_FILE_PATH
    if not os.path.isfile(file_path):
        return False
    with open(file_path) as f:
        txt: str = f.read()
    if txt == '1':
        return True
    return False


def _get_callable_str(callable_: Union[Callable, str]) -> str:
    """
    Get a callable string (label).

    Parameters
    ----------
    callable_ : Callable or str
        Target function or method or property or dunder method name.

    Returns
    -------
    callable_str : str
        A callable string (label).
    """
    if isinstance(callable_, str):
        callable_str: str = callable_
    else:
        callable_str = callable_.__name__
    return callable_str


def _get_callable_count_file_path(
        callable_: Union[Callable, str],
        module_name: str,
        class_: Optional[Type] = None) -> str:
    """
    Get a specified callable count data file path.

    Parameters
    ----------
    callable_ : Callable or str
        Target function or method or property or dunder method name.
    module_name : str
        Module name. This value will be set the `__name__` value.
    class_ : Type or None, optional
        Target class type. If the target callable_ variable is not
        a method, this argument will be ignored.

    Returns
    -------
    file_path : str
        Target file path.
    """
    from apysc._expression import expression_file_util
    module_path: str = module_name.replace('.', '_')
    if class_ is None:
        class_name: str = ''
    else:
        class_name = f'_{class_.__name__}'
    callable_str: str = _get_callable_str(callable_=callable_)
    file_path: str = os.path.join(
        expression_file_util.EXPRESSION_ROOT_DIR,
        f'callable_count_{module_path}{class_name}_{callable_str}.txt'
    )
    return file_path


def _get_callable_count(
        callable_: Union[Callable, str],
        module_name: str,
        class_: Optional[Type] = None) -> int:
    """
    Get a specified callable count number.

    Parameters
    ----------
    callable_ : Callable or str
        Target function or method or property or dunder method name.
    module_name : str
        Module name. This value will be set the `__name__` value.
    class_ : Type or None, optional
        Target class type. If the target callable_ variable is not
        a method, this argument will be ignored.

    Returns
    -------
    callable_count : int
        Target count number.
    """
    file_path: str = _get_callable_count_file_path(
        callable_=callable_,
        module_name=module_name,
        class_=class_)
    if not os.path.isfile(file_path):
        return 0
    with open(file_path) as f:
        txt: str = f.read()
    try:
        callable_count: int = int(txt)
    except Exception:
        return 0
    return callable_count


def _increment_callable_count(
        callable_: Union[Callable, str],
        module_name: str,
        class_: Optional[Type] = None) -> None:
    """
    Increment a specified callable count number.

    Parameters
    ----------
    callable_ : Callable or str
        Target function or method or property or dunder method name.
    module_name : str
        Module name. This value will be set the `__name__` value.
    class_ : Type or None, optional
        Target class type. If the target callable_ variable is not
        a method, this argument will be ignored.
    """
    callable_count: int = _get_callable_count(
        callable_=callable_, module_name=module_name, class_=class_)
    file_path: str = _get_callable_count_file_path(
        callable_=callable_, module_name=module_name, class_=class_)
    with open(file_path, 'w') as f:
        f.write(str(callable_count + 1))


class DebugInfo:
    """
    Save a debug information (append callable interface name
    comment and arguments information) to the JavaScript
    expression file. This class is used at the `with` statement.
    """

    _callable: Union[Callable, str]
    _locals: Dict[str, Any]
    _module_name: str
    _class: Optional[Type]
    _DIVIDER: str = '/' * 70
    _file_path: str
    _callable_count: int
    _indent: Indent

    def __init__(
            self, callable_: Union[Callable, str],
            locals_: Dict[str, Any],
            module_name: str,
            class_: Optional[Type] = None) -> None:
        """
        Save a debug information (append callable interface name
        comment and arguments information) to the JavaScript
        expression file. This class is used at the `with` statement.

        Notes
        -----
        If the debug mode setting is not enabled, saving will
        be skipped.

        Parameters
        ----------
        callable_ : Callable or str
            Target function or method or property or dunder method name.
        locals_ : dict
            Local variables. This value will be set by the `locals()`
            function.
        module_name : str
            Module name. This value will be set the `__name__` value.
        class_ : Type or None, optional
            Target class type. If the target callable_ variable is not
            a method, this argument will be ignored.
        """
        self._callable = callable_
        self._locals = locals_
        self._module_name = module_name
        self._class = class_
        self._file_path = _get_callable_count_file_path(
            callable_=callable_, module_name=module_name, class_=class_)
        _increment_callable_count(
            callable_=callable_, module_name=module_name, class_=class_)
        self._callable_count = _get_callable_count(
            callable_=callable_, module_name=module_name, class_=class_)
        self._indent = Indent()

    def _get_class_info(self) -> str:
        """
        Get a class information string.

        Returns
        -------
        class_info : str
            Target class information string.
        """
        if self._class is None:
            class_info: str = ''
        else:
            class_info = f'\n// class: {self._class.__name__}'
        return class_info

    def __enter__(self) -> None:
        """
        The method will be called at the start of the with block.
        """
        import apysc as ap
        from apysc._type.variable_name_interface import VariableNameInterface
        if not ap.is_debug_mode():
            return
        class_info: str = self._get_class_info()
        if not self._locals:
            arguments_info: str = ''
        else:
            arguments_info = '\n// arguments and variables:'
            for argument_name, argument in self._locals.items():
                if inspect.ismodule(argument):
                    continue
                if argument_name.startswith('__'):
                    continue
                if isinstance(argument, str):
                    argument = repr(argument)[1:-1]
                    argument = f"'{argument}'"
                if isinstance(argument, VariableNameInterface):
                    argument = f'{argument}({argument.variable_name})'
                arguments_info += f'\n//    {argument_name} = {argument}'
        callable_str: str = _get_callable_str(callable_=self._callable)
        expression: str = (
            f'{self._DIVIDER}'
            f'\n// [{callable_str} {self._callable_count}] '
            'started.'
            f'\n// module name: {self._module_name}'
            f'{class_info}'
            f'{arguments_info}'
        )
        ap.append_js_expression(expression=expression)
        self._indent.__enter__()

    def __exit__(self, *args: Any) -> None:
        """
        The method will be called at the end of the with block.

        Parameters
        ----------
        *args : list
            Positional arguments.
        """
        import apysc as ap
        if not ap.is_debug_mode():
            return
        class_info: str = self._get_class_info()
        callable_str: str = _get_callable_str(callable_=self._callable)
        expression: str = (
            f'// [{callable_str} {self._callable_count}] ended.'
            f'\n// module name: {self._module_name}'
            f'{class_info}'
            f'\n{self._DIVIDER}'
        )
        self._indent.__exit__()
        ap.append_js_expression(expression=expression)
