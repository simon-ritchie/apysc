from apysc._time.fps import _FPSDefinition
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
