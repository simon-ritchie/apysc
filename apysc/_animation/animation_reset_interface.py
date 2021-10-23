"""Class implementation for the animation_reset interface.
"""

from apysc._type.variable_name_interface import VariableNameInterface


class AnimationResetInterface(VariableNameInterface):

    def animation_reset(self) -> None:
        """
        Stop the all animations and reset.

        References
        ----------
        - animation_reset interface document
            - https://simon-ritchie.github.io/apysc/animation_reset.html
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.animation_reset, locals_=locals(),
                module_name=__name__, class_=AnimationResetInterface):
            expression: str = (
                f'{self.variable_name}.timeline().stop();'
            )
            ap.append_js_expression(expression=expression)
