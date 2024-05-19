from apysc._material_design.icon.material_https_icon import MaterialhttpsIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialhttpsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialhttpsIcon = MaterialhttpsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
