"""Debugging mode setting interface implementations for the HTML
and JavaScript.
"""

import os
import inspect
from typing import Any, Callable, Dict, Optional, Type


def set_debug_mode() -> None:
    """
    Set the debug mode for the HTML and JavaScript debugging.
    If this functions is called, the following setting will be applied:
    - HTML minify setting will be disabled.
    - Per each interface JavaScript divider string will be appended.
    """
    from apysc._expression import expression_file_util
    file_path: str = expression_file_util.DEBUG_MODE_SETTING_FILE_PATH
    with open(file_path, 'w') as f:
        f.write('1')


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


def _get_callable_count_file_path(
        callable_: Callable,
        module_name: str,
        class_: Optional[Type] = None) -> str:
    """
    Get a specified callable count data file path.

    Parameters
    ----------
    callable_ : Callable
        Target function or method.
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
    file_path: str = os.path.join(
        expression_file_util.EXPRESSION_ROOT_DIR,
        f'callable_count_{module_path}{class_name}_{callable_.__name__}.txt'
    )
    return file_path


def _get_callable_count(
        callable_: Callable,
        module_name: str,
        class_: Optional[Type] = None) -> int:
    """
    Get a specified callable count number.

    Parameters
    ----------
    callable_ : Callable
        Target function or method.
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
        callable_: Callable,
        module_name: str,
        class_: Optional[Type] = None) -> None:
    """
    Increment a specified callable count number.

    Parameters
    ----------
    callable_ : Callable
        Target function or method.
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

    _callable: Callable
    _locals: Dict[str, Any]
    _module_name: str
    _class: Optional[Type]
    _DIVIDER: str = '/' * 70
    _file_path: str
    _callable_count: int

    def __init__(
            self, callable_: Callable, locals_: Dict[str, Any],
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
        callable_ : Callable
            Target function or method.
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
                if isinstance(argument, str) and argument == '':
                    argument = "''"
                if isinstance(argument, VariableNameInterface):
                    argument = f'{argument}({argument.variable_name})'
                arguments_info += f'\n//    {argument_name} = {argument}'
        expression: str = (
            f'{self._DIVIDER}'
            f'\n// [{self._callable.__name__} {self._callable_count}] '
            'started.'
            f'\n// module name: {self._module_name}'
            f'{class_info}'
            f'{arguments_info}'
        )
        ap.append_js_expression(expression=expression)

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
        expression: str = (
            f'// [{self._callable.__name__} {self._callable_count}] ended.'
            f'\n// module name: {self._module_name}'
            f'{class_info}'
            f'\n{self._DIVIDER}'
        )
        ap.append_js_expression(expression=expression)
