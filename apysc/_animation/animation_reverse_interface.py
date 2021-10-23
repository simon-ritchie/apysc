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
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.animation_reverse, locals_=locals(),
                module_name=__name__, class_=AnimationReverseInterface):
            expression: str = (
                f'{self.variable_name}.timeline().reverse();'
            )
            ap.append_js_expression(expression=expression)
