"""Class implementation for the animation_finish interface.
"""

from apysc._type.variable_name_interface import VariableNameInterface


class AnimationFinishInterface(VariableNameInterface):

    def animation_finish(self) -> None:
        """
        Finish the all animations (set the animation last value to each
        attribute).

        References
        ----------
        - animation_finish interface document
            - https://simon-ritchie.github.io/apysc/animation_finish.html
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.animation_finish, locals_=locals(),
                module_name=__name__, class_=AnimationFinishInterface):
            expression: str = (
                f'{self.variable_name}.timeline().finish();'
            )
            ap.append_js_expression(expression=expression)
