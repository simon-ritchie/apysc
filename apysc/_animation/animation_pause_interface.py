"""Class implementation for the animation_pause interface.
"""

from apysc._type.variable_name_interface import VariableNameInterface


class AnimationPauseInterface(VariableNameInterface):

    def animation_pause(self) -> None:
        """
        Stop the all animations.

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
        >>> def on_timer(
        ...         e: ap.TimerEvent,
        ...         options: RectOptions) -> None:
        ...     rectangle: ap.Rectangle = options['rectangle']
        ...     rectangle.animation_pause()
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
        >>> ap.Timer(on_timer, delay=750, options=options).start()
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.animation_pause, locals_=locals(),
                module_name=__name__, class_=AnimationPauseInterface):
            expression: str = (
                f'{self.variable_name}.timeline().pause();'
            )
            ap.append_js_expression(expression=expression)
