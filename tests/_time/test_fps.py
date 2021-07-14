import apysc as ap
from apysc._time.fps import FPSDefinition
from tests.testing_helper import assert_attrs


class TestFPSDefinition:

    def test___init__(self) -> None:
        definition: FPSDefinition = FPSDefinition(
            fps=30,
            milisecond_intervals=33.3333)
        assert_attrs(
            expected_attrs={
                '_fps': 30,
                '_milisecond_intervals': 33.3333,
            },
            any_obj=definition)

    def test_milisecond_interval(self) -> None:
        definition: FPSDefinition = FPSDefinition(
            fps=30,
            milisecond_intervals=33.3333)
        assert definition.milisecond_intervals == 33.3333


def test_FPS() -> None:
    for fps in ap.FPS:
        fps_definition: FPSDefinition = fps.value
        one_second: float = \
            fps_definition._fps * fps_definition._milisecond_intervals
        assert one_second > 999.9
        assert one_second < 1000.1
