"""The class implementation for the return expression.
"""


class Return:
    """
    Class for the return expression.

    References
    ----------
    - Return document
        - https://simon-ritchie.github.io/apysc/return.html
    """

    def __init__(self) -> None:
        """
        Class for the return expression.

        Notes
        -----
        This class can be instantiated only in an event handler scope.

        References
        ----------
        - Return document
            - https://simon-ritchie.github.io/apysc/return.html
        """
        import apysc as ap
        self._validate_current_scope_is_event_handler()
        ap.append_js_expression(expression='return;')

    def _validate_current_scope_is_event_handler(self) -> None:
        """
        Validate whether the current scope is an event handler
        scope or not.
        """
        from apysc._expression import event_handler_scope
        event_handler_scope_count: int = \
            event_handler_scope.get_current_event_handler_scope_count()
        if event_handler_scope_count > 0:
            return
        raise Exception(
            'The `Return` class can be instantiated only in an event '
            'handler scope.')
