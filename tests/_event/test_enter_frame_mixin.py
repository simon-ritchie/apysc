from random import randint
import re
from typing import Match, Optional, Pattern, List

from retrying import retry

from apysc._event.enter_frame_mixin import EnterFrameMixIn
import apysc as ap
from apysc._expression import expression_data_util, var_names


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
        assert mixin._is_stopped_settings == {"test": True}

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
        )
        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=rf"function {var_names.LOOP}_\d+?\(\) {{",
            string=expression,
        )
        assert match is not None

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

        match = re.search(
            pattern=rf"\n  requestAnimationFrame\({var_names.LOOP}_\d+?\);",
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

        match = re.search(
            pattern=rf"\nrequestAnimationFrame\({var_names.LOOP}_\d+?\);",
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None
