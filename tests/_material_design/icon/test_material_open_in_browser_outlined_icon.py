from apysc._material_design.icon.material_open_in_browser_outlined_icon import MaterialopenInBrowserOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialopenInBrowserOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialopenInBrowserOutlinedIcon = MaterialopenInBrowserOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
