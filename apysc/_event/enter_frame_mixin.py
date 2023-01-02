"""Class implementation for the enter frame mix-in.
"""

from typing import Callable
from typing import Dict
from typing import Generic
from typing import Optional
from typing import TypeVar

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


class _EnterFrameEventNotRegistered(Exception):
    pass


class EnterFrameMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    SetHandlerDataMixIn[EnterFrameEvent],
    Generic[_Target, _Options],
    VariableNameMixIn,
):

    _enter_frame_handlers: Dict[str, HandlerData[EnterFrameEvent]]
    _is_stopped_settings: Dict[_HandlerName, Boolean]
    _fps_milisecond_intervals_settings: Dict[_HandlerName, Number]
    _loop_func_name_settings: Dict[_HandlerName, str]

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

        Notes
        -----
        If this is the second call of this interface, this interface
        ignores `options` argument (it changes the only running status
        and `fps` setting).

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
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        self._initialize_enter_frame_handlers_if_not_initialized()
        self._initialize_is_stopped_settings_if_not_initialized()
        self._initialize_fps_milisecond_intervals_settings_if_not_initialized()
        self._initialize_loop_func_name_settings()

        handler_name: str = get_handler_name(handler=handler, instance=self)
        if handler_name in self._is_stopped_settings:
            with ap.If(self._is_stopped_settings[handler_name]):
                self._is_stopped_settings[handler_name].value = False
                ap.append_js_expression(
                    expression=(
                        "requestAnimationFrame("
                        f"{self._loop_func_name_settings[handler_name]});"
                    ),
                )
            return

        LOOP_FUNC_NAME: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.LOOP
        )
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
            loop_func_name=LOOP_FUNC_NAME,
        )
        append_handler_expression(
            handler_data=self._enter_frame_handlers[handler_name],
            handler_name=handler_name,
            e=event,
        )
        self._is_stopped_settings[handler_name] = is_stopped
        self._loop_func_name_settings[handler_name] = LOOP_FUNC_NAME

    def _initialize_loop_func_name_settings(self) -> None:
        """
        Initialize the `_loop_func_name_settings`'s attribute
        if this instance has not initialized it yet.
        """
        if hasattr(self, "_loop_func_name_settings"):
            return
        self._loop_func_name_settings = {}

    def _initialize_fps_milisecond_intervals_settings_if_not_initialized(self) -> None:
        """
        Initialize the `_fps_milisecond_intervals_settings`'s
        attribute if this instance has not initialized it yet.
        """
        if hasattr(self, "_fps_milisecond_intervals_settings"):
            return
        self._fps_milisecond_intervals_settings = {}

    def _append_enter_frame_expression(
        self,
        *,
        handler_name: str,
        fps: FPS,
        is_stopped: Boolean,
        loop_func_name: str,
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
        loop_func_name : str
            A loop function name to set.
        """
        import apysc as ap
        from apysc._expression.indent_num import Indent

        MILISECOND_INTERVALS: float = fps.value.milisecond_intervals
        prev_time: ap.DateTime = ap.DateTime.now(
            variable_name_suffix=self._get_attr_or_variable_name_suffix(
                value_identifier="prev_time",
            ),
        )
        expression: str = (
            f"function {loop_func_name}() {{"
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
                expression=f"requestAnimationFrame({loop_func_name});"
            )
            prev_time.millisecond += count * MILISECOND_INTERVALS
        ap.append_js_expression(expression="}")
        ap.append_js_expression(expression=f"requestAnimationFrame({loop_func_name});")

    def _initialize_enter_frame_handlers_if_not_initialized(self) -> None:
        """
        Initialize the `_enter_frame_handlers`'s attribute if this instance
        has not initialized it yet.
        """
        if hasattr(self, "_enter_frame_handlers"):
            return
        self._enter_frame_handlers = {}

    def _initialize_is_stopped_settings_if_not_initialized(self) -> None:
        """
        Initialize the `_is_stopped_settings`'s attribute if this instance
        has not initialized it yet.
        """
        if hasattr(self, "_is_stopped_settings"):
            return
        self._is_stopped_settings = {}

    @final
    @arg_validation_decos.handler_args_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def unbind_enter_frame(
        self,
        handler: Callable[[EnterFrameEvent, _Options], None],
    ) -> None:
        """
        Unbind a specified handler's enter-frame event.

        Parameters
        ----------
        handler : Callable[[EnterFrameEvent, _Options], None]
            Unbinding target callable.

        Raises
        ------
        _EnterFrameEventNotRegistered
            If there is no unbinding target of a specified handler.
        """
        from apysc._event.handler import get_handler_name

        self._initialize_is_stopped_settings_if_not_initialized()
        handler_name: str = get_handler_name(handler=handler, instance=self)
        if handler_name not in self._is_stopped_settings:
            raise _EnterFrameEventNotRegistered(
                "There is no unbinding target of a specified handler."
                "\nPlease call `enter_frame` interframe before call this method."
            )
        self._is_stopped_settings[handler_name].value = True

    @final
    @add_debug_info_setting(module_name=__name__)
    def unbind_enter_frame_all(self) -> None:
        """
        Unbind all enter-frame events.
        """
        self._initialize_is_stopped_settings_if_not_initialized()
        for is_stopped in self._is_stopped_settings.values():
            is_stopped.value = True
