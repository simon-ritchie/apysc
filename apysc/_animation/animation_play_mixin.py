"""Class implementation for the animation_play mix-in.
"""

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.variable_name_mixin import VariableNameMixIn


class AnimationPlayMixIn(VariableNameMixIn):
    @final
    @add_debug_info_setting(module_name=__name__)
    def animation_play(self) -> None:
        """
        Restart all paused animations.

        References
        ----------
        - animation_pause and animation_play interfaces
            - https://simon-ritchie.github.io/apysc/en/animation_pause_and_play.html  # noqa

        Examples
        --------
        >>> from typing_extensions import TypedDict
        >>> import apysc as ap
        >>> class RectOptions(TypedDict):
        ...     rectangle: ap.Rectangle
        ...
        >>> def on_timer_1(e: ap.TimerEvent, options: RectOptions) -> None:
        ...     rectangle: ap.Rectangle = options["rectangle"]
        ...     rectangle.animation_pause()
        >>> def on_timer_2(e: ap.TimerEvent, options: RectOptions) -> None:
        ...     rectangle: ap.Rectangle = options["rectangle"]
        ...     rectangle.animation_play()
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> _ = rectangle.animation_x(
        ...     x=100,
        ...     duration=1500,
        ...     easing=ap.Easing.EASE_OUT_QUINT,
        ... ).start()
        >>> options: RectOptions = {"rectangle": rectangle}
        >>> ap.Timer(on_timer_1, delay=500, options=options).start()
        >>> ap.Timer(on_timer_2, delay=1000, options=options).start()
        """
        import apysc as ap

        expression: str = f"{self.variable_name}.timeline().play();"
        ap.append_js_expression(expression=expression)
