import apysc as ap
from apysc._chart.border_container_mixin import BorderContainerMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestBorderContainerMixIn:
    @apply_test_settings()
    def test__initialize_border_container(self) -> None:
        mixin: BorderContainerMixIn = BorderContainerMixIn()
        overall_container: ap.Sprite = ap.Sprite()
        mixin._initialize_border_container(
            overall_container=overall_container,
            variable_name_suffix="test_suffix",
        )
        assert isinstance(mixin._border_container, ap.Sprite)
        assert mixin._border_container._variable_name_suffix == "test_suffix"
        assert mixin._border_container._parent is overall_container
