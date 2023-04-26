import apysc as ap
from apysc._chart.background_container_mixin import BackgroundContainerMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestBackgroundContainerMixIn:
    @apply_test_settings()
    def test__initialize_background_container(self) -> None:
        ap.Stage()
        overall_container: ap.Sprite = ap.Sprite()
        mixin: BackgroundContainerMixIn = BackgroundContainerMixIn()
        mixin._initialize_background_container(
            overall_container=overall_container,
            variable_name_suffix="test_suffix",
        )
        assert isinstance(mixin._background_container, ap.Sprite)
        assert mixin._background_container._variable_name_suffix == "test_suffix"
        assert mixin._background_container.parent == overall_container
