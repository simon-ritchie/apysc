"""Class implementation for the `_set_handler_data` mix-in.
"""

from typing import Callable
from typing import Dict
from typing import Generic
from typing import Optional
from typing import TypeVar

from typing_extensions import final

from apysc._event.event import Event
from apysc._event.handler import HandlerData
from apysc._validation import arg_validation_decos

_Options = TypeVar("_Options")
_EventClass = TypeVar("_EventClass", bound=Event)


class SetHandlerDataMixIn(Generic[_EventClass]):
    @final
    @arg_validation_decos.handler_args_num(arg_position_index=1)
    @arg_validation_decos.is_builtin_dict(arg_position_index=2)
    @arg_validation_decos.handler_options_type(arg_position_index=3)
    def _set_handler_data(
        self,
        *,
        handler: Callable[[_EventClass, _Options], None],
        handlers_dict: Dict[str, HandlerData[_EventClass]],
        options: Optional[_Options],
    ) -> None:
        """
        Set a handler's data to the given dictionary.

        Parameters
        ----------
        handler : Callable[[_EventClass, _Options], None]
            Callable that this instance calls when dispatching.
        handlers_dict : Dict[str, HandlerData]
            Dictionary that this instance sets a handler's data.
        options : Optional[_Options]
            Optional arguments dictionary that this instance passes
            to a handler.
        """
        from apysc._event.handler import get_handler_name

        name: str = get_handler_name(handler=handler, instance=self)
        if options is None:
            options = {}  # type: ignore
        handler_data: HandlerData[_EventClass] = HandlerData(
            handler=handler, options=options
        )
        handlers_dict[name] = handler_data
