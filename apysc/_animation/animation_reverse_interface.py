"""Class implementation for the animation_reverse interface.
"""

from apysc._type.variable_name_interface import VariableNameInterface


class AnimationReverseInterface(VariableNameInterface):

    def animation_reverse(self) -> None:
        """
        Reverse the all running animations.

        Notes
        -----
        If you call this interface multiple times and animations
        have been reached at the beginning or end of the animation,
        then the reverse instruction will be ignored.
        This means that the same interval's timer tick reverse
        setting will not work correctly (since the same interval
        setting will reach the animation start).

        References
        ----------
        - animation_reverse interface document
            - https://simon-ritchie.github.io/apysc/animation_reverse.html

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
        ...     rectangle.animation_reverse()
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
                callable_=self.animation_reverse, locals_=locals(),
                module_name=__name__, class_=AnimationReverseInterface):
            expression: str = (
                f'{self.variable_name}.timeline().reverse();'
            )
            ap.append_js_expression(expression=expression)
