"""Class implementation for the timer event.
"""

from apysc._event.event import Event
from apysc._time import timer


class TimerEvent(Event):
    """
    Timer event class.

    References
    ----------
    - TimerEvent class document
        - https://simon-ritchie.github.io/apysc/timer_event.html

    Examples
    --------
    >>> from typing_extensions import TypedDict
    >>> import apysc as ap
    >>> class RectOptions(TypedDict):
    ...     rectangle: ap.Rectangle
    >>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
    ...     rectangle: ap.Rectangle = options['rectangle']
    ...     rectangle.x += 1
    ...     with ap.If(rectangle.x >= 100):
    ...         timer: ap.Timer = e.this
    ...         timer.stop()
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.begin_fill(color='#0af')
    >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    ...     x=50, y=50, width=50, height=50)
    >>> options: RectOptions = {'rectangle': rectangle}
    >>> ap.Timer(
    ...     on_timer, delay=ap.FPS.FPS_60, options=options,
    ... ).start()
    """

    _this: 'timer.Timer'

    def __init__(self, this: 'timer.Timer') -> None:
        """
        Timer event class.

        Parameters
        ----------
        this : Timer
            Target timer instance.

        References
        ----------
        - TimerEvent class document
            - https://simon-ritchie.github.io/apysc/timer_event.html

        Examples
        --------
        >>> from typing_extensions import TypedDict
        >>> import apysc as ap
        >>> class RectOptions(TypedDict):
        ...     rectangle: ap.Rectangle
        >>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
        ...     rectangle: ap.Rectangle = options['rectangle']
        ...     rectangle.x += 1
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> options: RectOptions = {'rectangle': rectangle}
        >>> ap.Timer(
        ...     on_timer, delay=ap.FPS.FPS_60, options=options,
        ... ).start()
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=TimerEvent):
            from apysc._expression import var_names
            super(TimerEvent, self).__init__(
                this=this, type_name=var_names.TIMER_EVENT)

    @property
    def this(self) -> 'timer.Timer':
        """
        Get a timer instance that listening this event.

        Returns
        -------
        this : TImer
            Instance that listening this event.

        References
        ----------
        - TimerEvent class document
            - https://simon-ritchie.github.io/apysc/timer_event.html

        Examples
        --------
        >>> from typing_extensions import TypedDict
        >>> import apysc as ap
        >>> class RectOptions(TypedDict):
        ...     rectangle: ap.Rectangle
        >>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
        ...     rectangle: ap.Rectangle = options['rectangle']
        ...     rectangle.x += 1
        ...     with ap.If(rectangle.x >= 100):
        ...         timer: ap.Timer = e.this
        ...         timer.stop()
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> options: RectOptions = {'rectangle': rectangle}
        >>> ap.Timer(
        ...     on_timer, delay=ap.FPS.FPS_60, options=options,
        ... ).start()
        """
        return self._this
