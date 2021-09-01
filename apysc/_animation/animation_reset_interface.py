"""Class implementation for the animation_reset interface.
"""

from apysc._type.variable_name_interface import VariableNameInterface


class AnimationResetInterface(VariableNameInterface):

    def animation_reset(self) -> None:
        """
        Stop the all animations and reset.
        """
        import apysc as ap
        expression: str = (
            f'{self.variable_name}.timeline().stop();'
        )
        ap.append_js_expression(expression=expression)
