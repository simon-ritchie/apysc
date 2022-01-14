"""Class Implementation for basic event.
"""

from typing import Generic
from typing import Optional
from typing import TypeVar

from apysc._type.variable_name_interface import VariableNameInterface

T = TypeVar('T', bound=VariableNameInterface)


class Event(Generic[T], VariableNameInterface):
    """
    Basic event class.

    Examples
    --------
    >>> import apysc as ap
    >>> def on_custom_event(
    ...         e: ap.Event[ap.Rectangle], options: dict) -> None:
    ...     rectangle: ap.Rectangle = e.this
    ...     rectangle.fill_color = ap.String('#f0a')
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.begin_fill(color='#0af')
    >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    ...     x=50, y=50, width=50, height=50)
    >>> e: ap.Event = ap.Event(this=rectangle)
    >>> _ = rectangle.bind_custom_event(
    ...     custom_event_type='my_custom_event',
    ...     handler=on_custom_event, e=e)
    >>> # Do something here and then trigger the custom event
    >>> rectangle.trigger_custom_event(
    ...     custom_event_type='my_custom_event')
    """

    _this: T

    def __init__(
            self, this: T,
            *,
            type_name: Optional[str] = None) -> None:
        """
        Basic event class.

        Parameters
        ----------
        this : VariableNameInterface
            Instance that listening event (e.g., Sprite).
        type_name : str or None, default None
            Type name to set. Only specify when inherit this class.

        Examples
        --------
        >>> import apysc as ap
        >>> def on_custom_event(
        ...         e: ap.Event[ap.Rectangle], options: dict) -> None:
        ...     rectangle: ap.Rectangle = e.this
        ...     rectangle.fill_color = ap.String('#f0a')
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> e: ap.Event = ap.Event(this=rectangle)
        >>> _ = rectangle.bind_custom_event(
        ...     custom_event_type='my_custom_event',
        ...     handler=on_custom_event, e=e)
        >>> # Do something here and then trigger the custom event
        >>> rectangle.trigger_custom_event(
        ...     custom_event_type='my_custom_event')
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=Event):
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            self._validate_type_name_and_self_type(type_name=type_name)
            self._this = this
            if type_name is None:
                type_name = var_names.EVENT
            self.variable_name = expression_variables_util.\
                get_next_variable_name(type_name=type_name)

    def _validate_type_name_and_self_type(
            self, *, type_name: Optional[str]) -> None:
        """
        Validate type_name argument is None when self instance
        is not Event subclass, and the opposite pattern is true
        as well.

        Parameters
        ----------
        type_name : str or None
            Type name to set.

        Raises
        ------
        ValueError
            - If type_name is not None and self instance is Event type.
            - If type_name is None and self instance is not Event type.
        """
        from apysc._type import type_util
        if type_name is not None:
            if type_util.is_same_class_instance(class_=Event, instance=self):
                raise ValueError(
                    'type_name argument can be set only when this instance '
                    'is subclass of Event.')
            return
        if not type_util.is_same_class_instance(class_=Event, instance=self):
            raise ValueError(
                'type_name argument can\'t be set when this instance '
                'is Event (this will be used by Event subclass).')

    @property
    def this(self) -> T:
        """
        Get an instance that listening this event.

        Returns
        -------
        this : VariableNameInterface
            Instance that listening this event.

        Examples
        --------
        >>> import apysc as ap
        >>> def on_custom_event(
        ...         e: ap.Event[ap.Rectangle], options: dict) -> None:
        ...     rectangle: ap.Rectangle = e.this
        ...     rectangle.fill_color = ap.String('#f0a')
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> e: ap.Event = ap.Event(this=rectangle)
        >>> _ = rectangle.bind_custom_event(
        ...     custom_event_type='my_custom_event',
        ...     handler=on_custom_event, e=e)
        >>> # Do something here and then trigger the custom event
        >>> rectangle.trigger_custom_event(
        ...     custom_event_type='my_custom_event')
        """
        return self._this
