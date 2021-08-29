"""Class implementation for the animation event.
"""

from apysc._event.event import Event
from apysc._animation.animation_base import AnimationBase


class AnimationEvent(Event):
    """
    Animation event class.
    """

    _this: AnimationBase

    def __init__(self, this: AnimationBase) -> None:
        """
        Animation event class.

        Parameters
        ----------
        this : AnimationBase
            Animation setting instance.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=AnimationEvent):
            from apysc._expression import var_names
            super(AnimationEvent, self).__init__(
                this=this, type_name=var_names.ANIMATION_EVENT)

    @property
    def this(self) -> AnimationBase:
        """
        Get a animation setting instance that linstening this event.

        Returns
        -------
        this : AnimationBase
            Instance that linstening this event.
        """
        return self._this
