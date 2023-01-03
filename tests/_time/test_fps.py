import apysc as ap
from apysc._testing.testing_helper import assert_attrs
from apysc._time.fps import FPSDefinition


class TestFPSDefinition:
    def test___init__(self) -> None:
        definition: FPSDefinition = FPSDefinition(fps=30, millisecond_interval=33.3333)
        assert_attrs(
            expected_attrs={
                "_fps": 30,
                "_millisecond_interval": 33.3333,
            },
            any_obj=definition,
        )

    def test_milisecond_interval(self) -> None:
        definition: FPSDefinition = FPSDefinition(fps=30, millisecond_interval=33.3333)
        assert definition.millisecond_interval == 33.3333


def test_FPS() -> None:
    for fps in ap.FPS:
        fps_definition: FPSDefinition = fps.value
        one_second: float = fps_definition._fps * fps_definition._millisecond_interval
        assert one_second > 999.9
        assert one_second < 1000.1
