"""Class implementation for the enter frame mix-in.
"""

from typing import Callable
from typing import Dict
from typing import Optional
from typing import TypeVar

from typing_extensions import TypedDict
from typing_extensions import final

from apysc._event.enter_frame_event import EnterFrameEvent
from apysc._event.handler import HandlerData
from apysc._event.set_handler_data_mixin import SetHandlerDataMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._time.fps import FPS
from apysc._type.boolean import Boolean
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._validation import arg_validation_decos

_Options = TypeVar("_Options")
_Handlername = str


class _HandlerSettings(TypedDict):
    handler_name: str
    is_stopped: Boolean
    fps: Int
    fps_interval: Number


class EnterFrameMixIn(SetHandlerDataMixIn[EnterFrameEvent]):

    _enter_frame_handlers: Dict[str, HandlerData[EnterFrameEvent]]
    _enter_frame_handler_settings: Dict[_Handlername, _HandlerSettings]

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

        self._initialize_enter_frame_handlers_if_not_initialized()
        self._set_handler_data(
            handler=handler,
            handlers_dict=self._enter_frame_handlers,
            options=options,
        )

    def _initialize_enter_frame_handlers_if_not_initialized(self) -> None:
        """
        Initialize the `_enter_frame_handlers` attribute if this interface
        has not initialized it yet.
        """
        if hasattr(self, "_enter_frame_handlers"):
            return
        self._enter_frame_handlers = {}
