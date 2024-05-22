from apysc._material_design.icon.material_desktop_access_disabled_icon import (
    MaterialDesktopAccessDisabledIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialDesktopAccessDisabledIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialDesktopAccessDisabledIcon = MaterialDesktopAccessDisabledIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
