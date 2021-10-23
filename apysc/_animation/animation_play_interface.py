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
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.animation_play, locals_=locals(),
                module_name=__name__, class_=AnimationPlayInterface):
            expression: str = (
                f'{self.variable_name}.timeline().play();'
            )
            ap.append_js_expression(expression=expression)
