from apysc._material_design.icon.material_open_in_browser_icon import (
    MaterialOpenInBrowserIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialOpenInBrowserIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialOpenInBrowserIcon = MaterialOpenInBrowserIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
