import apysc as ap
from apysc._chart.y_axis_container_mixin import YAxisContainerMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestYAxisContainerMixIn:
    @apply_test_settings()
    def test__initialize_y_axis_container(self) -> None:
        ap.Stage()
        mixin: YAxisContainerMixIn = YAxisContainerMixIn()
        overall_container: ap.Sprite = ap.Sprite()
        mixin._initialize_y_axis_container(
            overall_container=overall_container,
            variable_name_suffix="test_suffix",
        )
        assert isinstance(mixin._y_axis_container, ap.Sprite)
        assert mixin._y_axis_container._variable_name_suffix == "test_suffix"
        assert mixin._y_axis_container.parent == overall_container
