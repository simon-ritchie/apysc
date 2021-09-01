"""Class implementation for the animation_play interface.
"""

from apysc._type.variable_name_interface import VariableNameInterface


class AnimationPlayInterface(VariableNameInterface):

    def animation_play(self) -> None:
        """
        Restart the all paused animations.
        """
        import apysc as ap
        expression: str = (
            f'{self.variable_name}.timeline().play();'
        )
        ap.append_js_expression(expression=expression)
