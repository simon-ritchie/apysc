"""Class implementation for the prevent_default mix-in.
"""

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.variable_name_mixin import VariableNameMixIn


class PreventDefaultMixIn(VariableNameMixIn):
    @final
    @add_debug_info_setting(module_name=__name__)
    def prevent_default(self) -> None:
        """
        Prevent event's default behavior.

        References
        ----------
        - Event class prevent_default and stop_propagation interfaces
            - https://simon-ritchie.github.io/apysc/en/event_prevent_default_and_stop_propagation.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> def on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     e.prevent_default()
        ...     rectangle: ap.Rectangle = e.this
        ...     rectangle.fill_color = ap.String("#f0a")
        ...     rectangle.unbind_mouseup_all()
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> _ = rectangle.click(on_click)
        """
        import apysc as ap

        expression: str = f"{self.variable_name}.preventDefault();"
        ap.append_js_expression(expression=expression)
