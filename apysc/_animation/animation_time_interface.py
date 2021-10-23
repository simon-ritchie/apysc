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
