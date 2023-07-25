import apysc as ap
from apysc._testing.testing_helper import apply_test_settings


class TestColorless:
    @apply_test_settings(retrying_max_attempts_num=0)
    def test___init__(self) -> None:
        assert isinstance(ap.COLORLESS, ap.Color)
        assert ap.COLORLESS._value == ap.String("")
        assert "colorless" in ap.COLORLESS._value.variable_name
