"""The class implementations for the initial substitution expression
mix-in.
"""

from abc import ABC
from abc import abstractmethod

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting


class InitialSubstitutionExpMixIn(ABC):
    @abstractmethod
    def _create_initial_substitution_expression(self) -> str:
        """
        Create an initial value's substitution expression string.
        """

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_initial_substitution_expression_if_in_handler_scope(
        self,
        skip_appending: bool,
    ) -> None:
        """
        Append an initial value's expression if a current scope is
        in a handler scope.

        Parameters
        ----------
        skip_appending : bool
            A boolean indicates whether to skip appending an expression
            or not.
        """
        import apysc as ap
        from apysc._expression import event_handler_scope

        if skip_appending:
            return

        if not event_handler_scope.current_scope_is_in_event_handler():
            return
        expression: str = self._create_initial_substitution_expression()
        ap.append_js_expression(expression=expression)
