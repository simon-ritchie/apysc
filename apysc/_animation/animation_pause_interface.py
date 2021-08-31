"""Class implementation for the animation_pause interface.
"""

from apysc._type.variable_name_interface import VariableNameInterface


class AnimationPauseInterface(VariableNameInterface):

    def animation_pause(self) -> None:
        """
        Stop the all animations.
        """
        import apysc as ap
        expression: str = (
            f'{self.variable_name}.timeline().pause();'
        )
        ap.append_js_expression(expression=expression)
