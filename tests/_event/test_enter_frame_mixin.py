import re
from random import randint
from typing import Match
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._event.enter_frame_mixin import EnterFrameMixIn
from apysc._event.handler import get_handler_name
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._event.enter_frame_mixin import _EnterFrameEventNotRegistered
from apysc._testing.testing_helper import assert_raises


class TestEnterFrameMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_enter_frame_handlers_if_not_initialized(self) -> None:
        mixin: EnterFrameMixIn = EnterFrameMixIn()
        mixin._initialize_enter_frame_handlers_if_not_initialized()
        assert mixin._enter_frame_handlers == {}

        prev_id: int = id(mixin._enter_frame_handlers)
        mixin._initialize_enter_frame_handlers_if_not_initialized()
        assert prev_id == id(mixin._enter_frame_handlers)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_is_stopped_settings_if_not_initialized(self) -> None:
        mixin: EnterFrameMixIn = EnterFrameMixIn()
        mixin._initialize_is_stopped_settings_if_not_initialized()
        assert mixin._is_stopped_settings == {}

        mixin._is_stopped_settings["test"] = ap.Boolean(True)
        mixin._initialize_is_stopped_settings_if_not_initialized()
        assert mixin._is_stopped_settings == {"test": ap.Boolean(True)}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_enter_frame_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: EnterFrameMixIn = EnterFrameMixIn()
        mixin.variable_name = "test_mixin"
        is_stopped: ap.Boolean = ap.Boolean(False)
        mixin._append_enter_frame_expression(
            handler_name="test_handler",
            fps=ap.FPS.FPS_60,
            is_stopped=is_stopped,
            loop_func_name="test_loop_1",
        )
        expression: str = expression_data_util.get_current_expression()
        assert "function test_loop_1() {" in expression

        match = re.search(
            pattern=rf"\n  if \({is_stopped.variable_name}\) {{\n    return;\n  }}",
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

        match = re.search(
            pattern=rf"\n  for \(var i = 0; i \< {var_names.INT}_\d+?\; i\+\+\) {{"
            r"\n    test_handler\(\);\n  }",
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None
        assert "\n  requestAnimationFrame(test_loop_1);" in expression
        assert "\nrequestAnimationFrame(test_loop_1);" in expression

    def on_enter_frame_1(self, e: ap.EnterFrameEvent, options: dict) -> None:
        """
        The handler for enter-frame event.

        Parameters
        ----------
        e : ap.EnterFrameEvent
            Event instance.
        options : dict
            Optional arguments dictionary.
        """
        ap.trace(100)

    def on_enter_frame_2(self, e: ap.EnterFrameEvent, options: dict) -> None:
        """
        The handler for enter-frame event.

        Parameters
        ----------
        e : ap.EnterFrameEvent
            Event instance.
        options : dict
            Optional arguments dictionary.
        """
        ap.trace(200)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_enter_frame(self) -> None:
        expression_data_util.empty_expression()
        mixin: EnterFrameMixIn = EnterFrameMixIn()
        mixin.variable_name = "test_mixin"
        mixin.enter_frame(
            handler=self.on_enter_frame_1,
            fps=ap.FPS.FPS_30,
        )
        handler_name: str = get_handler_name(
            handler=self.on_enter_frame_1,
            instance=mixin,
        )
        assert handler_name in mixin._enter_frame_handlers
        assert not mixin._is_stopped_settings[handler_name]
        assert handler_name in mixin._loop_func_name_settings
        assert mixin._loop_func_name_settings[handler_name].startswith(var_names.LOOP)

        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=rf"function {var_names.LOOP}_\d+?\(\) {{",
            string=expression,
        )
        assert match is not None

        expression = expression_data_util.get_current_event_handler_scope_expression()
        assert f"function {handler_name}" in expression

        expression_data_util.empty_expression()
        mixin.unbind_enter_frame(handler=self.on_enter_frame_1)
        mixin.enter_frame(
            handler=self.on_enter_frame_1,
            fps=ap.FPS.FPS_30,
        )
        assert mixin._is_stopped_settings[handler_name].value == False
        expression = expression_data_util.get_current_expression()
        assert "function" not in expression
        assert "requestAnimationFrame" in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_unbind_enter_frame(self) -> None:
        mixin: EnterFrameMixIn = EnterFrameMixIn()
        assert_raises(
            expected_error_class=_EnterFrameEventNotRegistered,
            callable_=mixin.unbind_enter_frame,
            match="There is no unbinding target of a specified handler.",
            handler=self.on_enter_frame_1,
        )

        mixin.enter_frame(handler=self.on_enter_frame_1)
        mixin.unbind_enter_frame(handler=self.on_enter_frame_1)
        handler_name: str = get_handler_name(
            handler=self.on_enter_frame_1,
            instance=mixin,
        )
        assert mixin._is_stopped_settings[handler_name].value

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_unbind_enter_frame_all(self) -> None:
        mixin: EnterFrameMixIn = EnterFrameMixIn()
        mixin.enter_frame(handler=self.on_enter_frame_1)
        mixin.enter_frame(handler=self.on_enter_frame_2)
        mixin.unbind_enter_frame_all()
        handler_name: str = get_handler_name(
            handler=self.on_enter_frame_1,
            instance=mixin,
        )
        assert mixin._is_stopped_settings[handler_name].value
        handler_name = get_handler_name(
            handler=self.on_enter_frame_2,
            instance=mixin,
        )
        assert mixin._is_stopped_settings[handler_name].value

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_fps_milisecond_intervals_settings_if_not_initialized(
        self
    ) -> None:
        mixin: EnterFrameMixIn = EnterFrameMixIn()
        mixin._initialize_fps_milisecond_intervals_settings_if_not_initialized()
        assert mixin._fps_milisecond_intervals_settings == {}

        mixin._fps_milisecond_intervals_settings["test"] = ap.Number(33.3)
        mixin._initialize_fps_milisecond_intervals_settings_if_not_initialized()
        assert mixin._fps_milisecond_intervals_settings == {
            "test": ap.Number(33.3),
        }

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_loop_func_name_settings_if_not_initialized(self) -> None:
        mixin: EnterFrameMixIn = EnterFrameMixIn()
        mixin._initialize_loop_func_name_settings_if_not_initialized()
        assert mixin._loop_func_name_settings == {}

        mixin._loop_func_name_settings["test_handler"] = "test_loop"
        assert mixin._loop_func_name_settings == {"test_handler": "test_loop"}
