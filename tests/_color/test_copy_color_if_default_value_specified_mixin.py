import apysc as ap
from apysc._color.copy_color_if_default_value_specified_mixin import (
    CopyColorIfDefaultValueSpecifiedMixIn,
)
from apysc._testing.testing_helper import apply_test_settings


class TestCopyColorIfDefaultValueSpecifiedMixIn:
    @apply_test_settings()
    def test__copy_color_if_default_value_specified(self) -> None:
        mixin: CopyColorIfDefaultValueSpecifiedMixIn = (
            CopyColorIfDefaultValueSpecifiedMixIn()
        )
        color: ap.Color = ap.Color("#333")
        copied_color: ap.Color = mixin._copy_color_if_default_value_specified(
            color=color, default_color=color
        )
        assert color == copied_color
        assert color._value.variable_name != copied_color._value.variable_name

        copied_color = mixin._copy_color_if_default_value_specified(
            color=color, default_color=ap.Color("#444")
        )
        assert color == ap.Color("#333")
        assert color._value.variable_name == copied_color._value.variable_name
