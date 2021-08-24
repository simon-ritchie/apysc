"""Class implementation for the blank object interface.
This interface will be used by the custom event interface
or something else.
"""


class BlankObjectInterface:

    _is_blank_object_initialized: bool = False
    _blank_object_variable_name: str

    def _initialize_blank_object_if_not_initialized(self) -> None:
        """
        Initialize a blank object value if it hasn't been
        initialized yet.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._initialize_blank_object_if_not_initialized,
                locals_=locals(),
                module_name=__name__, class_=BlankObjectInterface):
            from apysc._expression import expression_data_util
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            from apysc._expression.event_handler_scope import \
                TemporaryNotHandlerScope
            if self._is_blank_object_initialized:
                return
            with TemporaryNotHandlerScope():
                self._blank_object_variable_name = expression_variables_util.\
                    get_next_variable_name(type_name=var_names.BLANK_OBJECT)
                expression: str = (
                    f'var {self._blank_object_variable_name} = {{}};'
                )
                expression_data_util.append_js_expression(
                    expression=expression)
                self._is_blank_object_initialized = True

    @property
    def blank_object_variable_name(self) -> str:
        """
        Get a blank object variable name.

        Returns
        -------
        blank_object_variable_name : str
            A blank object variable name.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='blank_object_variable_name', locals_=locals(),
                module_name=__name__, class_=BlankObjectInterface):
            self._initialize_blank_object_if_not_initialized()
            return self._blank_object_variable_name
