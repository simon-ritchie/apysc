"""Class implementation for the animation_reverse interface.
"""

from apysc._type.variable_name_interface import VariableNameInterface


class AnimationReverseInterface(VariableNameInterface):

    def animation_reverse(self) -> None:
        """
        Reverse the all running animations.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.animation_reverse, locals_=locals(),
                module_name=__name__, class_=AnimationReverseInterface):
            expression: str = (
                f'{self.variable_name}.timeline().reverse();'
            )
            ap.append_js_expression(expression=expression)
