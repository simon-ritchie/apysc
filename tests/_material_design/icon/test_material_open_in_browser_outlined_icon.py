from apysc._material_design.icon.material_open_in_browser_outlined_icon import (
    MaterialOpenInBrowserOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialOpenInBrowserOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialOpenInBrowserOutlinedIcon = MaterialOpenInBrowserOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
