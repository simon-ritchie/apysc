"""The mix-in class implementation for the
`_append_line_alpha_attr_expression` method.
"""

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting


class AppendLineAlphaAttrExpressionMixIn:
    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_line_alpha_attr_expression(
        self,
        *,
        expression: str,
        indent_num: int,
        skip_appending: bool = False,
    ) -> str:
        """
        Append line-alpha attribute expression to a specified
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
            If this is not a `LineAlphaMixIn` instance.
        """
        from apysc._display import graphics_expression
        from apysc._display.line_alpha_mixin import LineAlphaMixIn

        if not isinstance(self, LineAlphaMixIn):
            raise TypeError(
                f"This instance is not a `{LineAlphaMixIn.__name__}` instance: "
                f"{type(self).__name__}"
            )
        if skip_appending:
            return expression

        self._initialize_line_alpha_if_not_initialized()
        expression = graphics_expression.append_stroke_opacity_expression(
            line_alpha=self._line_alpha,
            expression=expression,
            indent_num=indent_num,
        )
        return expression
