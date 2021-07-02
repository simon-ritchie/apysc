from apysc._time.fps import _FPSDefinition
from apysc import FPS
from tests.testing_helper import assert_attrs


class Test_FPSDefinition:

    def test___init__(self) -> None:
        definition: _FPSDefinition = _FPSDefinition(
            fps=30,
            milisecond_intervals=33.3333)
        assert_attrs(
            expected_attrs={
                '_fps': 30,
                '_milisecond_interval': 33.3333,
            },
            any_obj=definition)


def test_FPS() -> None:
    for fps in FPS:
        fps_definition: _FPSDefinition = fps.value
        one_second: float = \
            fps_definition._fps * fps_definition._milisecond_interval
        assert one_second > 999.9
        assert one_second < 1000.1
