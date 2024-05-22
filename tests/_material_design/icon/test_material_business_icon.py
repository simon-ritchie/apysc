from apysc._material_design.icon.material_business_icon import MaterialBusinessIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialBusinessIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialBusinessIcon = MaterialBusinessIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
