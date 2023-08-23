"""The mix-in class implementation for the `for`-loop `__exit__` method.
"""

from typing import Any
from typing import Dict

from typing_extensions import final

from apysc._expression.indent_num import Indent
from apysc._html.debug_mode import add_debug_info_setting


class ForLoopExitMixIn:
    _locals: Dict[str, Any]
    _globals: Dict[str, Any]
    _snapshot_name: str
    _indent: Indent

    @final
    @add_debug_info_setting(module_name=__name__)
    def __exit__(self, *args: Any) -> None:
        """
        The exiting method for the beginning of with-statement.
        """
        from apysc._expression import expression_data_util
        from apysc._expression import last_scope
        from apysc._expression.get_last_scope_interface import GetLastScopeInterface
        from apysc._loop import loop_count
        from apysc._type import revert_mixin

        loop_count.decrement_current_loop_count()
        revert_mixin.revert_each_scope_vars(
            snapshot_name=self._snapshot_name,
            locals_=self._locals,
            globals_=self._globals,
        )
        self._indent.__exit__()
        expression_data_util.append_js_expression(expression="}")
        if isinstance(self, GetLastScopeInterface):
            last_scope.set_last_scope(value=self._get_last_scope())
        else:
            raise TypeError(
                "This interface is only available a `GetLastScopeInterface` "
                f"subclass: {type(self).__name__}, {self}"
            )
