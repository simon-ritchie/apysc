"""Class implementation for the parallel animation.
"""

from typing import List

from apysc._type.variable_name_interface import VariableNameInterface
from apysc._animation.animation_base import AnimationBase


class AnimationParallel(VariableNameInterface):
    """
    Class for the parallel animation.
    """

    _animations: List[AnimationBase]

    def __init__(self, animations: List[AnimationBase]) -> None:
        """
        Class for the parallel animation.

        Parameters
        ----------
        animations : list of AnimationBase
            Target animations.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=AnimationParallel):
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            self._animations = animations
            self.variable_name = expression_variables_util.\
                get_next_variable_name(type_name=var_names.ANIMATION_PARALLEL)
