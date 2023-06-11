"""The loop implementation class for the `ap.Array` indices and values.
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
from apysc._loop.initialize_for_loop_value_interface import (
    InitializeForLoopValueInterface,
)
from apysc._type.array import Array
from apysc._type.initialize_locals_and_globals_mixin import (
    InitializeLocalsAndGlobalsMixIn,
)
from apysc._validation import arg_validation_decos

_ArrayValue = TypeVar("_ArrayValue", bound=InitializeForLoopValueInterface)


class ForArrayIndicesAndValues(
    ForLoopExitMixIn,
    GetLastScopeInterface,
    InitializeLocalsAndGlobalsMixIn,
    Generic[_ArrayValue],
):
    """
    The loop implementation class for the `ap.Array` indices and values.
    """

    _arr: Array[_ArrayValue]
    _arr_value_type: Type[_ArrayValue]
    _variable_name_suffix: str

    @final
    @arg_validation_decos.is_apysc_array(arg_position_index=1)
    @arg_validation_decos.is_initialize_for_loop_value_interface_subclass(
        arg_position_index=2,
    )
    @arg_validation_decos.is_builtin_string(arg_position_index=5, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        arr: Array[_ArrayValue],
        arr_value_type: Type[_ArrayValue],
        *,
        locals_: Optional[Dict[str, Any]] = None,
        globals_: Optional[Dict[str, Any]] = None,
        variable_name_suffix: str = "",
    ) -> None:
        """
        The loop implementation class for the `ap.Array` indices and values.

        Parameters
        ----------
        arr : Array[_ArrayValue]
            An array to iterate.
        arr_value_type : Type[_ArrayValue]
            An array value type. This interface accepts apysc
            types, such as the `Int`, `String`, `Rectangle`.
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
        """
        self._initialize_locals_and_globals(locals_=locals_, globals_=globals_)
        self._arr = arr
        self._arr_value_type = arr_value_type
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
        return LastScope.FOR_ARRAY_INDICES_AND_VALUES
