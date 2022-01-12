"""Class implementation for the animation event.
"""

from typing import Generic
from typing import TypeVar

from apysc._animation import animation_base
from apysc._event.event import Event
from apysc._type.variable_name_interface import VariableNameInterface

_T = TypeVar('_T', bound=VariableNameInterface)


class AnimationEvent(Event, Generic[_T]):
    """
    Animation event class.

    Examples
    --------
    >>> import apysc as ap
    >>> def on_animation_complete(
    ...         e: ap.AnimationEvent[ap.Rectangle],
    ...         options: dict) -> None:
    ...     rectangle: ap.Rectangle = e.this.target
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.begin_fill(color='#0af')
    >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    ...     x=50, y=50, width=50, height=50)
    >>> _ = rectangle.animation_x(
    ...     x=100).animation_complete(on_animation_complete)
    """

    _this: 'animation_base.AnimationBase[_T]'

    def __init__(
            self, *,
            this: 'animation_base.AnimationBase[_T]') -> None:
        """
        Animation event class.

        Parameters
        ----------
        this : AnimationBase
            Animation setting instance.

        Examples
        --------
        >>> import apysc as ap
        >>> def on_animation_complete(
        ...         e: ap.AnimationEvent[ap.Rectangle],
        ...         options: dict) -> None:
        ...     rectangle: ap.Rectangle = e.this.target
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> _ = rectangle.animation_x(
        ...     x=100).animation_complete(on_animation_complete)

        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=AnimationEvent):
            from apysc._expression import var_names
            super(AnimationEvent, self).__init__(
                this=this, type_name=var_names.ANIMATION_EVENT)

    @property
    def this(self) -> 'animation_base.AnimationBase[_T]':
        """
        Get a animation setting instance that linstening this event.

        Returns
        -------
        this : AnimationBase
            Instance that linstening this event.

        Examples
        --------
        >>> import apysc as ap
        >>> def on_animation_complete(
        ...         e: ap.AnimationEvent[ap.Rectangle],
        ...         options: dict) -> None:
        ...     rectangle: ap.Rectangle = e.this.target
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> _ = rectangle.animation_x(
        ...     x=100).animation_complete(on_animation_complete)
        """
        return self._this
