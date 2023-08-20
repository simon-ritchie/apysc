"""Class implementation for the animation_time mix-in.
"""

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number
from apysc._type.variable_name_mixin import VariableNameMixIn


class AnimationTimeMixIn(VariableNameMixIn):
    @final
    @add_debug_info_setting(module_name=__name__)
    def animation_time(self) -> Number:
        """
        Get an animation elapsed millisecond.

        Returns
        -------
        elapsed_time : Number
            An animation elapsed millisecond.

        References
        ----------
        - animation_time interface
            - https://simon-ritchie.github.io/apysc/en/animation_time.html

        Examples
        --------
        >>> from typing_extensions import TypedDict
        >>> import apysc as ap
        >>> class RectOptions(TypedDict):
        ...     rectangle: ap.Rectangle
        ...
        >>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
        ...     rectangle: ap.Rectangle = options["rectangle"]
        ...     animation_time: ap.Number = rectangle.animation_time()
        ...     ap.trace("animation_time:", animation_time)
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
        >>> ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options).start()
        """
        from apysc._expression import expression_data_util

        elapsed_time: Number = Number(0.0)
        expression: str = (
            f"{elapsed_time.variable_name} = "
            f"{self.variable_name}.timeline().time();"
        )
        expression_data_util.append_js_expression(expression=expression)
        return elapsed_time
