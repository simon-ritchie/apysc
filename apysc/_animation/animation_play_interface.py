"""Class implementation for the animation_play interface.
"""

from apysc._type.variable_name_interface import VariableNameInterface


class AnimationPlayInterface(VariableNameInterface):

    def animation_play(self) -> None:
        """
        Restart the all paused animations.

        References
        ----------
        - animation_pause and animation_play interfaces document
            - https://bit.ly/3m2Xh8Y

        Examples
        --------
        >>> from typing_extensions import TypedDict
        >>> import apysc as ap
        >>> class RectOptions(TypedDict):
        ...     rectangle: ap.Rectangle
        >>> def on_timer_1(
        ...         e: ap.TimerEvent,
        ...         options: RectOptions) -> None:
        ...     rectangle: ap.Rectangle = options['rectangle']
        ...     rectangle.animation_pause()
        >>> def on_timer_2(
        ...         e: ap.TimerEvent,
        ...         options: RectOptions) -> None:
        ...     rectangle: ap.Rectangle = options['rectangle']
        ...     rectangle.animation_play()
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> _ = rectangle.animation_x(
        ...     x=100,
        ...     duration=1500,
        ...     easing=ap.Easing.EASE_OUT_QUINT,
        ... ).start()
        >>> options: RectOptions = {'rectangle': rectangle}
        >>> ap.Timer(on_timer_1, delay=500, options=options).start()
        >>> ap.Timer(on_timer_2, delay=1000, options=options).start()
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.animation_play, locals_=locals(),
                module_name=__name__, class_=AnimationPlayInterface):
            expression: str = (
                f'{self.variable_name}.timeline().play();'
            )
            ap.append_js_expression(expression=expression)
