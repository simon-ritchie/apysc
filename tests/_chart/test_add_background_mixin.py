import apysc as ap
from apysc._chart.add_background_mixin import AddBackgroundMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestAddBackgroundMixIn:
    @apply_test_settings()
    def test__add_background(self) -> None:
        mixin: AddBackgroundMixIn = AddBackgroundMixIn()
        background_container: ap.Sprite = ap.Sprite()
        mixin._add_background(
            background_container=background_container,
            width=ap.Int(300),
            height=ap.Int(200),
            background_fill_color=ap.Color("#333333"),
            background_fill_alpha=ap.Number(0.5),
            variable_name_suffix="test_suffix",
        )
        assert isinstance(mixin._background, ap.Rectangle)
        assert mixin._background._variable_name_suffix == "test_suffix"
        assert mixin._background.width == ap.Int(300)
        assert mixin._background.height == ap.Int(200)
        assert mixin._background.fill_color == ap.Color("#333333")
        assert mixin._background.fill_alpha == ap.Number(0.5)
        assert mixin._background.parent == background_container
