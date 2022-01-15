"""Class implementation for the prevent_default interface.
"""

from apysc._type.variable_name_interface import VariableNameInterface


class PreventDefaultInterface(VariableNameInterface):

    def prevent_default(self) -> None:
        """
        Prevent event's default behavior.

        Refenreces
        ----------
        - Event class prevent_default and stop_propagation interfaces document
            - https://bit.ly/3qqd4lH

        Examples
        --------
        >>> import apysc as ap
        >>> def on_click(
        ...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     e.prevent_default()
        ...     rectangle: ap.Rectangle = e.this
        ...     rectangle.fill_color = ap.String('#f0a')
        ...     rectangle.unbind_mouseup_all()
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> _ = rectangle.click(on_click)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.prevent_default, locals_=locals(),
                module_name=__name__, class_=PreventDefaultInterface):
            expression: str = (
                f'{self.variable_name}.preventDefault();'
            )
            ap.append_js_expression(expression=expression)
