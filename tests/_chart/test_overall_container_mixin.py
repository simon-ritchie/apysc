import apysc as ap
from apysc._chart.overall_container_mixin import OverallContainerMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestOverallContainerMixIn:
    @apply_test_settings()
    def test__initialize_overall_container(self) -> None:
        mixin: OverallContainerMixIn = OverallContainerMixIn()
        mixin._initialize_overall_container(variable_name_suffix="test_suffix_1")
        assert isinstance(mixin._overall_container, ap.Sprite)
        assert mixin._overall_container._variable_name_suffix == "test_suffix_1"
