"""The loop implementation class for the `ap.Dictionary` values.
"""

from typing import Any
from typing import Dict
from typing import Generic
from typing import Optional
from typing import Type
from typing import TypeVar

from typing_extensions import final

from apysc._expression.get_last_scope_interface import GetLastScopeInterface
from apysc._expression.indent_num import Indent
from apysc._expression.last_scope import LastScope
from apysc._html.debug_mode import add_debug_info_setting
from apysc._loop.for_loop_exit_mixin import ForLoopExitMixIn
from apysc._loop.initialize_with_base_value_interface import (
    InitializeWithBaseValueInterface,
)
from apysc._type.dictionary import Dictionary
from apysc._type.initialize_locals_and_globals_mixin import (
    InitializeLocalsAndGlobalsMixIn,
)
from apysc._type.string import String
from apysc._validation import arg_validation_decos

_DictValue = TypeVar("_DictValue", bound=InitializeWithBaseValueInterface)


class ForDictValues(
    ForLoopExitMixIn,
    GetLastScopeInterface,
    InitializeLocalsAndGlobalsMixIn,
    Generic[_DictValue],
):
    """
    The loop implementation class for the `ap.Dictionary` values.

    References
    ----------
    - ForDictValues class
        - https://simon-ritchie.github.io/apysc/en/for_dict_values.html

    References
    ----------
    >>> import apysc as ap

    >>> _ = ap.Stage(
    ...     stage_width=250,
    ...     stage_height=150,
    ...     background_color=ap.Color("#333"),
    ...     stage_elem_id="stage",
    ... )
    >>> dict_: ap.Dictionary[str, ap.Number] = ap.Dictionary(
    ...     {"a": ap.Number(50), "b": ap.Number(150)},
    ... )
    >>> with ap.ForDictValues(dict_=dict_, dict_value_type=ap.Number) as value:
    ...     _ = ap.Rectangle(
    ...         x=value, y=50, width=50, height=50, fill_color=ap.Color("#0af")
    ...     )
    ...
    """

    _dict: Dictionary[Any, _DictValue]
    _dict_value_type: Type[_DictValue]
    _variable_name_suffix: str

    @final
    @arg_validation_decos.is_apysc_dict(arg_position_index=1)
    @arg_validation_decos.is_initialize_with_base_value_interface_subclass(
        arg_position_index=2,
    )
    @arg_validation_decos.is_builtin_string(arg_position_index=5, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        dict_: Dictionary[Any, _DictValue],
        dict_value_type: Type[_DictValue],
        *,
        locals_: Optional[Dict[str, Any]] = None,
        globals_: Optional[Dict[str, Any]] = None,
        variable_name_suffix: str = "",
    ) -> None:
        """
        The loop implementation class for the `ap.Dictionary` values.

        Parameters
        ----------
        dict_ : Dictionary[Any, _DictValue]
            A dictionary to iterate.
        dict_value_type : Type[_DictValue]
            A dictionary value type. This interface accepts
            `InitializeWithBaseValueInterface` subclasses,
            such as the `Int`, `String`, or `Rectangle`.
        locals_ : Optional[Dict[str, Any]], optional
            Current scope's local variables. Set locals()
            value to this argument. If specified, this interface
            reverts all local scope VariableNameMixIn
            variables (like Int, Sprite) at the end of a with-statement
            scope. This setting is useful when you don't want to
            update each variable.
        globals_ : Optional[Dict[str, Any]], optional
            Current scope's global variables. Set globals()
            value to this argument. This setting works
            the same way as the locals_ argument.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        References
        ----------
        - ForDictValues class
            - https://simon-ritchie.github.io/apysc/en/for_dict_values.html

        References
        ----------
        >>> import apysc as ap

        >>> _ = ap.Stage(
        ...     stage_width=250,
        ...     stage_height=150,
        ...     background_color=ap.Color("#333"),
        ...     stage_elem_id="stage",
        ... )
        >>> dict_: ap.Dictionary[str, ap.Number] = ap.Dictionary(
        ...     {"a": ap.Number(50), "b": ap.Number(150)},
        ... )
        >>> with ap.ForDictValues(dict_=dict_, dict_value_type=ap.Number) as value:
        ...     _ = ap.Rectangle(
        ...         x=value, y=50, width=50, height=50, fill_color=ap.Color("#0af")
        ...     )
        ...
        """
        self._initialize_locals_and_globals(locals_, globals_=globals_)
        self._dict = dict_
        self._dict_value_type = dict_value_type
        self._variable_name_suffix = variable_name_suffix
        self._indent = Indent()

    @final
    def _get_last_scope(self) -> LastScope:
        """
        Get a target last scope value.

        Returns
        -------
        last_scope : LastScope
            A target last scope.
        """
        return LastScope.FOR_DICT_VALUES

    @final
    @add_debug_info_setting(module_name=__name__)
    def __enter__(self) -> _DictValue:
        """
        The entering method for the beginning of with-statement.

        Returns
        -------
        dict_value : _DictValue
            A dictionary value of iteration.
        """
        from apysc._expression import expression_data_util
        from apysc._loop import loop_count
        from apysc._type import revert_mixin
        from apysc._validation.variable_name_validation import (
            validate_variable_name_mixin_type,
        )

        loop_count.increment_current_loop_count()
        self._snapshot_name = revert_mixin.make_snapshots_of_each_scope_vars(
            locals_=self._locals, globals_=self._globals
        )
        dict_value: _DictValue = self._dict_value_type._initialize_with_base_value()
        dict_value_variable_name: str = validate_variable_name_mixin_type(
            instance=dict_value,
        ).variable_name

        dict_key: String = String("", variable_name_suffix=self._variable_name_suffix)
        expression: str = (
            f"for ({dict_key.variable_name} in {self._dict.variable_name}) {{"
            f"\n  {dict_value_variable_name} = {self._dict.variable_name}"
            f"[{dict_key.variable_name}];"
        )
        expression_data_util.append_js_expression(expression=expression)

        self._indent.__enter__()
        return dict_value
