from random import randint

from retrying import retry

import apysc as ap
from apysc._console import _trace
from apysc._expression import expression_data_util
from apysc._html.debug_mode import add_debug_info_setting


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_trace() -> None:
    stage: ap.Stage = ap.Stage()
    ap.trace(stage, 100, "Hello!")
    expression: str = expression_data_util.get_current_expression()
    expected: str = (
        f'console.log({stage.variable_name}, "100", "Hello!", "\\nCalled from: '
        "test_trace, file name: test__trace.py, line number: "
    )
    assert expected in expression
    assert '");' in expression


@add_debug_info_setting(module_name=__name__)
def _dummy_trace() -> str:
    """
    Dummy function of the `trace`.

    Returns
    -------
    func_callers_info : str
        A function caller's information.
    """
    func_callers_info: str = _trace._get_func_callers_info()
    return func_callers_info


_TOP_LEVEL_SCOPE_FUNC_CALLERS_INFO: str = _dummy_trace()


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_func_callers_info() -> None:
    print(_TOP_LEVEL_SCOPE_FUNC_CALLERS_INFO)
    assert _TOP_LEVEL_SCOPE_FUNC_CALLERS_INFO.startswith("\\nCalled from: test__trace")

    func_callers_info: str = _dummy_trace()
    assert func_callers_info.startswith(
        "\\nCalled from: test__get_func_callers_info, file name: test__trace"
    )


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_outer_frames_index() -> None:
    _trace._temporary_outer_frames_index_adjustments = 5
    outer_frame_index: int = _trace._get_outer_frames_index()
    assert outer_frame_index == 5

    _trace._temporary_outer_frames_index_adjustments = None
    outer_frame_index = _trace._get_outer_frames_index()
    assert outer_frame_index == _trace.DEFAULT_OUTER_FRAMES_INDEX



class TestTemporaryOuterFramesIndexAdjustment:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___enter__(self) -> None:
        with _trace.TemporaryOuterFramesIndexAdjustment(
                temporary_outer_frames_index_adjustments=5):
            assert _trace._temporary_outer_frames_index_adjustments == 5

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___exit__(self) -> None:
        with _trace.TemporaryOuterFramesIndexAdjustment(
                temporary_outer_frames_index_adjustments=5):
            pass
        assert _trace._temporary_outer_frames_index_adjustments is None
