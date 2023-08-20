"""Class implementation for the animation_reverse mix-in.
"""

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.variable_name_mixin import VariableNameMixIn


class AnimationReverseMixIn(VariableNameMixIn):
    @final
    @add_debug_info_setting(module_name=__name__)
    def animation_reverse(self) -> None:
        """
        Reverse all running animations.

        Notes
        -----
        Suppose you call this interface multiple times and
        animations reach the beginning or end of the animation.
        In that case, this interface ignores the reverse instruction.
        This behavior means that the same interval's timer tick
        reverse setting does not work correctly (since the same
        interval setting reaches the animation start).

        References
        ----------
        - animation_reverse interface
            - https://simon-ritchie.github.io/apysc/en/animation_reverse.html

        Examples
        --------
        >>> from typing_extensions import TypedDict
        >>> import apysc as ap
        >>> class RectOptions(TypedDict):
        ...     rectangle: ap.Rectangle
        ...
        >>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
        ...     rectangle: ap.Rectangle = options["rectangle"]
        ...     rectangle.animation_reverse()
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> _ = rectangle.animation_x(
        ...     x=100,
        ...     duration=1500,
        ...     easing=ap.Easing.EASE_OUT_QUINT,
        ... ).start()
        >>> options: RectOptions = {"rectangle": rectangle}
        >>> ap.Timer(on_timer, delay=750, options=options).start()
        """
        from apysc._expression import expression_data_util

        expression: str = f"{self.variable_name}.timeline().reverse();"
        expression_data_util.append_js_expression(expression=expression)
