"""This module is for the `return` expression class
implementation.
"""

from typing_extensions import final


class Return:
    """
    Class for the return expression.

    References
    ----------
    - Return
        - https://simon-ritchie.github.io/apysc/en/return.html
    """

    @final
    def __init__(self) -> None:
        """
        Class for the return expression.

        Notes
        -----
        This class can be instantiated only in an event handler scope.

        References
        ----------
        - Return
            - https://simon-ritchie.github.io/apysc/en/return.html

        Examples
        --------
        >>> import apysc as ap
        >>> def on_timer(e: ap.TimerEvent, options: dict) -> None:
        ...     '''
        ...     The handler that the timer calls.
        ...
        ...     Parameters
        ...     ----------
        ...     e : ap.TimerEvent
        ...         Event instance.
        ...     options : dict
        ...         Optional arguments dictionary.
        ...     '''
        ...     with ap.If(e.this.current_count > 10):
        ...         ap.Return()
        ...     ap.trace("Not returned.")
        >>> ap.Timer(on_timer, delay=100).start()
        """
        from apysc._expression import expression_data_util

        self._validate_current_scope_is_event_handler()
        expression_data_util.append_js_expression(expression="return;")

    @final
    def _validate_current_scope_is_event_handler(self) -> None:
        """
        Validate whether the current scope is an event handler
        scope or not.
        """
        from apysc._expression import event_handler_scope

        if event_handler_scope.current_scope_is_in_event_handler():
            return
        raise Exception(
            "The `Return` class can be instantiated only in an event " "handler scope."
        )
