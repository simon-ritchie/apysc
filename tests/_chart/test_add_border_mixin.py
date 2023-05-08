import apysc as ap
from apysc._chart.add_border_mixin import AddBorderMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestAddBorderMixIn:
    @apply_test_settings()
    def test__add_border(self) -> None:
        ap.Stage()
        mixin: AddBorderMixIn = AddBorderMixIn()
        border_container: ap.Sprite = ap.Sprite()
        mixin._add_border(
            border_container=border_container,
            width=ap.Int(500),
            height=ap.Int(300),
            border_color=ap.String("#aaaaaa"),
            border_alpha=ap.Number(0.5),
            border_thickness=ap.Int(2),
            variable_name_suffix="test_suffix",
        )
        assert isinstance(mixin._border, ap.Rectangle)
        assert mixin._border._variable_name_suffix == "test_suffix"
        assert mixin._border.width == ap.Int(500)
        assert mixin._border.height == ap.Int(300)
        assert mixin._border.line_color == ap.String("#aaaaaa")
        assert mixin._border.line_alpha == ap.Number(0.5)
        assert mixin._border.line_thickness == ap.Int(2)
        assert mixin._border.parent == border_container
