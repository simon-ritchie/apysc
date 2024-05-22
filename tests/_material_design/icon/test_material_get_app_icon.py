from apysc._material_design.icon.material_get_app_icon import MaterialGetAppIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialGetAppIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialGetAppIcon = MaterialGetAppIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
