"""The mix-in class implementation for the
`_append_x_attr_expression` method.
"""

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting


class AppendXAttrExpressionMixIn:
    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_x_attr_expression(
        self,
        *,
        expression: str,
        indent_num: int,
        skip_appending: bool = False,
    ) -> str:
        """
        Appen an x attribute expression to a specified
        expression string.

        Parameters
        ----------
        expression : str
            A target expression string.
        indent_num : int
            An indentation number.
        skip_appending : bool, optional
            A boolean, whether to skip appending.

        Returns
        -------
        expression : str
            After an appending expression string.

        Raises
        ------
        TypeError
            If this is not a `XInterface` instance.
        """
        from apysc._display import graphics_expression
        from apysc._display.x_interface import XInterface

        if not isinstance(self, XInterface):
            raise TypeError(
                f"This instance is not a `{XInterface.__name__}` instance: "
                f"{type(self).__name__}"
            )
        if skip_appending:
            return expression

        self._initialize_x_if_not_initialized()
        expression = graphics_expression.append_x_expression(
            x=self._x, expression=expression, indent_num=indent_num
        )
        return expression
