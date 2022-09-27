"""Class implementation for the enter frame interface.
"""

from typing import Callable
from typing import Dict
from typing import Optional
from typing import TypeVar

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._event.handler import HandlerData
from apysc._validation import arg_validation_decos
from apysc._event.enter_frame_event import EnterFrameEvent
from apysc._time.fps import FPS


_Options = TypeVar("_Options")


class EnterFrameInterface:

    _enter_frame_handlers: Dict[str, HandlerData[EnterFrameEvent]]

    @final
    @arg_validation_decos.handler_args_num(arg_position_index=1)
    @arg_validation_decos.is_fps(arg_position_index=2)
    @arg_validation_decos.handler_options_type(arg_position_index=3)
    @add_debug_info_setting(module_name=__name__)
    def enter_frame(
            self,
            handler: Callable[[EnterFrameEvent, _Options], None],
            *,
            fps: FPS = FPS.FPS_60,
            options: Optional[_Options] = None,
        ) -> None:
        """
        Add an enter frame event listener setting.

        Parameters
        ----------
        handler : Callable[[EnterFrameEvent, _Options], None]
            An handler function to handle the enter frame event.
        fps : FPS, default FPS.FPS_60
            Frame per second to set.
        options : Optional[_Options], optional
            Optional arguments to pass to a handler function.
        """
        from apysc._event.handler import get_handler_name

        self._initialize_enter_frame_handlers_if_not_initialized()
        name: str = get_handler_name(handler=handler, instance=self)
        pass

    def _initialize_enter_frame_handlers_if_not_initialized(self) -> None:
        """
        Initialize the `_enter_frame_handlers` attribute if this interface
        has not initialized it yet.
        """
        if hasattr(self, "_enter_frame_handlers"):
            return
        self._enter_frame_handlers = {}
