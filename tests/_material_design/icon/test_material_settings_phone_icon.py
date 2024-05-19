from apysc._material_design.icon.material_settings_phone_icon import MaterialsettingsPhoneIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsettingsPhoneIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsettingsPhoneIcon = MaterialsettingsPhoneIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
