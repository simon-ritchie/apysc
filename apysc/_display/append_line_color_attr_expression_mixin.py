"""The mix-in class implementation for the
`_append_line_color_attr_expression` method.
"""

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting


class AppendLineColorAttrExpressionMixIn:
    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_line_color_attr_expression(
        self,
        *,
        expression: str,
        indent_num: int,
        skip_appending: bool = False,
    ) -> str:
        """
        Append a line-color attribute expression to a specified
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
            If this is not a `LineColorMixIn` instance.
        """
        from apysc._display import graphics_expression
        from apysc._display.line_color_mixin import LineColorMixIn

        if not isinstance(self, LineColorMixIn):
            raise TypeError(
                f"This instance is not a `{LineColorMixIn.__name__}` instance: "
                f"{type(self).__name__}"
            )
        if skip_appending:
            return expression

        self._initialize_line_color_if_not_initialized()
        expression = graphics_expression.append_stroke_expression(
            line_color=self._line_color,
            expression=expression,
            indent_num=indent_num,
        )
        return expression
