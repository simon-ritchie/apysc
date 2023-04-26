import apysc as ap
from apysc._chart.chart_container_mixin import ChartContainerMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestChartContainerMixIn:
    @apply_test_settings()
    def test__initialize_chart_container(self) -> None:
        ap.Stage()
        mixin: ChartContainerMixIn = ChartContainerMixIn()
        overall_container: ap.Sprite = ap.Sprite()
        mixin._initialize_chart_container(
            overall_container=overall_container,
            variable_name_suffix="test_suffix",
        )
        assert isinstance(mixin._chart_container, ap.Sprite)
        assert mixin._chart_container._variable_name_suffix == "test_suffix"
        assert mixin._chart_container.parent == overall_container
