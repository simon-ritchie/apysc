import apysc as ap
from apysc._chart.background_container_mixin import BackgroundContainerMixIn
from apysc._chart.chart_container_mixin import ChartContainerMixIn
from apysc._chart.initialize_each_container_mixin import InitializeEachContainerMixIn
from apysc._chart.overall_container_mixin import OverallContainerMixIn
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises


class _TestMixIn(
    OverallContainerMixIn,
    BackgroundContainerMixIn,
    ChartContainerMixIn,
    InitializeEachContainerMixIn,
):
    pass


class TestInitializeEachContainerMixIn:
    @apply_test_settings()
    def test__initialize_each_container(self) -> None:
        ap.Stage()
        mixin_1: InitializeEachContainerMixIn = InitializeEachContainerMixIn()
        assert_raises(
            expected_error_class=TypeError,
            callable_=mixin_1._initialize_each_container,
            variable_name_suffix="test_suffix_1",
        )

        mixin_2: _TestMixIn = _TestMixIn()
        mixin_2._initialize_each_container(variable_name_suffix="test_suffix_2")
        assert isinstance(mixin_2._overall_container, ap.Sprite)

        assert isinstance(mixin_2._background_container, ap.Sprite)
        assert mixin_2._background_container.parent == mixin_2._overall_container

        assert isinstance(mixin_2._chart_container, ap.Sprite)
        assert mixin_2._chart_container.parent == mixin_2._overall_container
