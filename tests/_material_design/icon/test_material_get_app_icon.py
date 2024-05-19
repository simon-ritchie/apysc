from apysc._material_design.icon.material_get_app_icon import MaterialgetAppIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialgetAppIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialgetAppIcon = MaterialgetAppIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
