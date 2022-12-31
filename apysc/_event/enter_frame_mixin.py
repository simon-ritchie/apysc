"""Class implementation for the enter frame mix-in.
"""

from typing import Callable
from typing import Dict
from typing import Generic
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
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._validation import arg_validation_decos

_Options = TypeVar("_Options")
_HandlerName = str
_Target = TypeVar("_Target")


class _HandlerSettings(TypedDict):
    handler_name: str
    is_stopped: Boolean
    fps: Int
    fps_interval: Number


class EnterFrameMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    SetHandlerDataMixIn[EnterFrameEvent],
    Generic[_Target],
    VariableNameMixIn,
):

    _enter_frame_handlers: Dict[str, HandlerData[EnterFrameEvent]]
    _is_stopped_settings: Dict[_HandlerName, Boolean]

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
            A handler function to handle the enter frame event.
        fps : FPS, default FPS.FPS_60
            Frame per second to set.
        options : Optional[_Options], optional
            Optional arguments to pass to a handler function.
        """
        import apysc as ap
        from apysc._event.handler import append_handler_expression
        from apysc._event.handler import get_handler_name

        self._initialize_enter_frame_handlers_if_not_initialized()
        self._initialize_is_stopped_settings_if_not_initialized()

        handler_name: str = get_handler_name(handler=handler, instance=self)
        if handler_name in self._is_stopped_settings:
            self._is_stopped_settings[handler_name].value = False
            return

        self._set_handler_data(
            handler=handler,
            handlers_dict=self._enter_frame_handlers,
            options=options,
        )
        is_stopped: Boolean = Boolean(
            False,
            variable_name_suffix=self._get_attr_or_variable_name_suffix(
                value_identifier="is_stopped",
            ),
        )
        event: ap.EnterFrameEvent = ap.EnterFrameEvent(this=self)
        self._append_enter_frame_expression(
            handler_name=handler_name,
            fps=fps,
            is_stopped=is_stopped,
        )
        append_handler_expression(
            handler_data=self._enter_frame_handlers[handler_name],
            handler_name=handler_name,
            e=event,
        )
        self._is_stopped_settings[handler_name] = is_stopped

    def _append_enter_frame_expression(
        self,
        *,
        handler_name: str,
        fps: FPS,
        is_stopped: Boolean,
    ) -> None:
        """
        Append an enter frame expression string.

        Parameters
        ----------
        handler_name : str
            Target handler's name.
        fps : FPS
            Frame per second to set.
        is_stopped : Boolean
            A boolean to control an animation loop.
        """
        import apysc as ap
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names
        from apysc._expression.indent_num import Indent

        LOOP_FUNC_NAME: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.LOOP
        )
        MILISECOND_INTERVALS: float = fps.value.milisecond_intervals
        prev_time: ap.DateTime = ap.DateTime.now(
            variable_name_suffix=self._get_attr_or_variable_name_suffix(
                value_identifier="prev_time",
            ),
        )
        expression: str = (
            f"function {LOOP_FUNC_NAME}() {{"
            f"\n  if ({is_stopped.variable_name}) {{"
            "\n    return;"
            "\n  }"
        )
        ap.append_js_expression(expression=expression)
        with Indent():
            current_time: ap.DateTime = ap.DateTime.now(
                variable_name_suffix=self._get_attr_or_variable_name_suffix(
                    value_identifier="current_time",
                )
            )
            count: Int = Int(
                0,
                variable_name_suffix=self._get_attr_or_variable_name_suffix(
                    value_identifier="count",
                ),
            )
            timedelta_: ap.TimeDelta = current_time - prev_time
            total_milliseconds: Number = timedelta_.total_seconds() * 1000
            count.value = ap.Math.trunc(total_milliseconds / MILISECOND_INTERVALS)
            ap.append_js_expression(
                expression=(
                    f"for (var i = 0; i < {count.variable_name}; i++) {{"
                    f"\n  {handler_name}();"
                    "\n}"
                )
            )
            ap.append_js_expression(
                expression=f"requestAnimationFrame({LOOP_FUNC_NAME});"
            )
            prev_time.millisecond += count * MILISECOND_INTERVALS
        ap.append_js_expression(expression="}")
        ap.append_js_expression(expression=f"requestAnimationFrame({LOOP_FUNC_NAME});")

    def _initialize_enter_frame_handlers_if_not_initialized(self) -> None:
        """
        Initialize the `_enter_frame_handlers`'s attribute if this interface
        has not initialized it yet.
        """
        if hasattr(self, "_enter_frame_handlers"):
            return
        self._enter_frame_handlers = {}

    def _initialize_is_stopped_settings_if_not_initialized(self) -> None:
        """
        Initialize the `_is_stopped_settings`'s attribute if this interface
        has not initialized it yet.
        """
        if hasattr(self, "_is_stopped_settings"):
            return
        self._is_stopped_settings = {}
