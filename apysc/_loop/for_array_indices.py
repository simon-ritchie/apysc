"""The loop implementation class for the `ap.Array` indices.
"""

from typing import Any
from typing import Dict
from typing import Generic
from typing import Optional
from typing import TypeVar
from typing import Union
from typing import Generic
from typing import TypeVar

from typing_extensions import final
from apysc._expression.indent_num import Indent
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.array import Array
from apysc._type.int import Int
from apysc._validation import arg_validation_decos

_ArrValue = TypeVar("_ArrValue")


class ForArrayIndices(Generic[_ArrValue]):
    """
    The loop implementation class for the `ap.Array` indices.
    """

    _arr: Array[_ArrValue]
    _locals: Dict[str, Any]
    _globals: Dict[str, Any]
    _snapshot_name: str
    _indent: Indent

    @final
    @arg_validation_decos.is_apysc_array(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        arr: Array[_ArrValue],
        *,
        locals_: Optional[Dict[str, Any]] = None,
        globals_: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        The loop implementation class for the `ap.Array` indices.

        Parameters
        ----------
        arr : Array[_ArrValue]
            An array to iterate.
        locals_ : Optional[Dict[str, Any]], optional
            Current scope's local variables. Set locals()
            value to this argument. If specified, this interface
            reverts all local scope VariableNameMixIn
            variables (like Int, Sprite) at the end of a `For`
            scope. This setting is useful when you don't want to
            update each variable by implementing the `For` scope.
        globals_ : Optional[Dict[str, Any]], optional
            Current scope's global variables. Set globals()
            value to this argument. This setting works
            the same way as the locals_ argument.
        """
        if locals_ is None:
            locals_ = {}
        if globals_ is None:
            globals_ = {}
        self._arr = arr
        self._locals = locals_
        self._globals = globals_
        self._indent = Indent()
