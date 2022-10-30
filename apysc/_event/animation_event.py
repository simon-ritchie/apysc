"""Class implementation for the animation event.
"""

from typing import Generic
from typing import TypeVar

from typing_extensions import final

from apysc._animation import animation_base
from apysc._event.event import Event
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.variable_name_mixin import VariableNameMixIn

_T = TypeVar("_T", bound=VariableNameMixIn)


class AnimationEvent(Event, Generic[_T]):
    """
    Animation event class.

    Examples
    --------
    >>> import apysc as ap
    >>> def on_animation_complete(
    ...     e: ap.AnimationEvent[ap.Rectangle], options: dict
    ... ) -> None:
    ...     rectangle: ap.Rectangle = e.this.target
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.begin_fill(color="#0af")
    >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    ...     x=50, y=50, width=50, height=50
    ... )
    >>> _ = rectangle.animation_x(x=100).animation_complete(on_animation_complete)
    """

    _this: "animation_base.AnimationBase[_T]"

    @final
    @add_debug_info_setting(module_name=__name__)
    def __init__(self, *, this: "animation_base.AnimationBase[_T]") -> None:
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
        ...     e: ap.AnimationEvent[ap.Rectangle], options: dict
        ... ) -> None:
        ...     rectangle: ap.Rectangle = e.this.target
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> _ = rectangle.animation_x(x=100).animation_complete(on_animation_complete)

        """
        from apysc._expression import var_names

        super(AnimationEvent, self).__init__(
            this=this, type_name=var_names.ANIMATION_EVENT
        )

    @property
    @add_debug_info_setting(module_name=__name__)
    def this(self) -> "animation_base.AnimationBase[_T]":
        """
        Get an animation setting instance of listening to this event.

        Returns
        -------
        this : AnimationBase
            Instance of listening to this event.

        Examples
        --------
        >>> import apysc as ap
        >>> def on_animation_complete(
        ...     e: ap.AnimationEvent[ap.Rectangle], options: dict
        ... ) -> None:
        ...     rectangle: ap.Rectangle = e.this.target
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> _ = rectangle.animation_x(x=100).animation_complete(on_animation_complete)
        """
        return self._this
