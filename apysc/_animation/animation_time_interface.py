"""Class implementation for the animation_time interface.
"""

from apysc._type.number import Number
from apysc._type.variable_name_interface import VariableNameInterface


class AnimationTimeInterface(VariableNameInterface):

    def animation_time(self) -> Number:
        """
        Get an animation elapsed milisecond.

        Returns
        -------
        elapsed_time : Number
            An animation elapsed milisecond.

        References
        ----------
        - animation_time interface document
            - https://simon-ritchie.github.io/apysc/animation_time.html

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
        ...     animation_time: ap.Number = rectangle.animation_time()
        ...     ap.trace('animation_time:', animation_time)
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
        >>> ap.Timer(
        ...     on_timer, delay=ap.FPS.FPS_60,
        ...     options=options).start()
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.animation_time, locals_=locals(),
                module_name=__name__, class_=AnimationTimeInterface):
            elapsed_time: Number = Number(0.0)
            expression: str = (
                f'{elapsed_time.variable_name} = '
                f'{self.variable_name}.timeline().time();'
            )
            ap.append_js_expression(expression=expression)
            return elapsed_time
