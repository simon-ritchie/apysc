import apysc as ap
from apysc._chart.x_axis_container_mixin import XAxisContainerMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestXAxisContainerMixIn:
    @apply_test_settings()
    def test__initialize_x_axis_container(self) -> None:
        mixin: XAxisContainerMixIn = XAxisContainerMixIn()
        overall_container: ap.Sprite = ap.Sprite()
        mixin._initialize_x_axis_container(
            overall_container=overall_container,
            variable_name_suffix="test_suffix",
        )
        assert isinstance(mixin._x_axis_container, ap.Sprite)
        assert mixin._x_axis_container._variable_name_suffix == "test_suffix"
        assert mixin._x_axis_container.parent == overall_container
