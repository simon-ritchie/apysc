"""The loop implementation class for the `ap.Dictionary` keys.
"""

from typing import Any
from typing import Dict
from typing import Generic
from typing import Optional
from typing import Type
from typing import TypeVar
from typing import cast

from typing_extensions import final

from apysc._expression.get_last_scope_interface import GetLastScopeInterface
from apysc._expression.indent_num import Indent
from apysc._expression.last_scope import LastScope
from apysc._html.debug_mode import add_debug_info_setting
from apysc._loop.for_loop_exit_mixin import ForLoopExitMixIn
from apysc._type.boolean import Boolean
from apysc._type.dictionary import Dictionary
from apysc._type.initialize_locals_and_globals_mixin import (
    InitializeLocalsAndGlobalsMixIn,
)
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String
from apysc._validation import arg_validation_decos

_DictKey = TypeVar("_DictKey", String, Int, Number, Boolean)


class ForDictKeys(
    ForLoopExitMixIn,
    GetLastScopeInterface,
    InitializeLocalsAndGlobalsMixIn,
    Generic[_DictKey],
):
    """
    The loop implementation class for the `ap.Dictionary` keys.

    References
    ----------
    - ForDictKeys class
        - https://simon-ritchie.github.io/apysc/en/for_dict_keys.html

    Examples
    --------
    >>> import apysc as ap

    >>> dict_: ap.Dictionary[ap.String, ap.Boolean] = ap.Dictionary(
    ...     {
    ...         ap.String("apple"): ap.Boolean(True),
    ...         ap.String("orange"): ap.Boolean(False),
    ...     }
    ... )
    >>> keys: ap.Array[ap.String] = ap.Array([])
    >>> with ap.ForDictKeys(dict_=dict_, dict_key_type=ap.String) as key:
    ...     keys.append(key)
    ...
    >>> ap.assert_arrays_equal(
    ...     keys,
    ...     ["apple", "orange"],
    ... )
    """

    _dict: Dictionary[_DictKey, Any]
    _dict_key_type: Type[_DictKey]
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
        dict_: Dictionary[_DictKey, Any],
        dict_key_type: Type[_DictKey],
        *,
        locals_: Optional[Dict[str, Any]] = None,
        globals_: Optional[Dict[str, Any]] = None,
        variable_name_suffix: str = "",
    ) -> None:
        """
        The loop implementation class for the `ap.Dictionary` keys.

        Parameters
        ----------
        dict_ : Dictionary[_DictKey, Any]
            A dictionary to iterate.
        dict_key_type : Type[_DictKey]
            A dictionary key type. This interface accepts hashable types,
            such as the `String`, `Int`, `Number`, or `Boolean`.
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
        - ForDictKeys class
            - https://simon-ritchie.github.io/apysc/en/for_dict_keys.html

        Examples
        --------
        >>> import apysc as ap

        >>> dict_: ap.Dictionary[ap.String, ap.Boolean] = ap.Dictionary(
        ...     {
        ...         ap.String("apple"): ap.Boolean(True),
        ...         ap.String("orange"): ap.Boolean(False),
        ...     }
        ... )
        >>> keys: ap.Array[ap.String] = ap.Array([])
        >>> with ap.ForDictKeys(dict_=dict_, dict_key_type=ap.String) as key:
        ...     keys.append(key)
        ...
        >>> ap.assert_arrays_equal(
        ...     keys,
        ...     ["apple", "orange"],
        ... )
        """
        self._initialize_locals_and_globals(locals_=locals_, globals_=globals_)
        self._dict = dict_
        self._dict_key_type = dict_key_type
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
        return LastScope.FOR_DICT_KEYS

    @final
    @add_debug_info_setting(module_name=__name__)
    def __enter__(self) -> _DictKey:
        """
        The entering method for the beginning of with-statement.

        Returns
        -------
        dict_key : _DictKey
            A dictionary key of iteration.
        """
        from apysc._expression import expression_data_util
        from apysc._loop import loop_count
        from apysc._type import revert_mixin

        loop_count.increment_current_loop_count()
        self._snapshot_name = revert_mixin.make_snapshots_of_each_scope_vars(
            locals_=self._locals, globals_=self._globals
        )
        dict_key: _DictKey = cast(
            _DictKey,
            self._dict_key_type._initialize_with_base_value(),
        )

        expression: str = (
            f"for ({dict_key.variable_name} in {self._dict.variable_name}) {{"
        )
        expression_data_util.append_js_expression(expression=expression)

        self._indent.__enter__()
        return dict_key
