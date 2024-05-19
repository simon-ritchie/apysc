from apysc._material_design.icon.material_logout_icon import MateriallogoutIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallogoutIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallogoutIcon = MateriallogoutIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
