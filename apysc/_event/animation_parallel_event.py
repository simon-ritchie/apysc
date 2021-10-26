"""Class implementation for the animation parallel event.
"""

from apysc._event.event import Event
from apysc._animation.animation_parallel import AnimationParallel


class AnimationParallelEvent(Event[AnimationParallel]):
    """
    Animation parallel event class.
    """

    def __init__(self, this: AnimationParallel) -> None:
        """
        Animation parallel event class.

        Parameters
        ----------
        this : AnimationParallel
            Parallel animation setting instance.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=AnimationParallelEvent):
            from apysc._expression import var_names
            super(AnimationParallelEvent, self).__init__(
                this=this, type_name=var_names.ANIMATION_PARALLEL_EVENT)
