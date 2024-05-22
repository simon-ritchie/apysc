from apysc._material_design.icon.material_https_icon import MaterialHttpsIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHttpsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHttpsIcon = MaterialHttpsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
