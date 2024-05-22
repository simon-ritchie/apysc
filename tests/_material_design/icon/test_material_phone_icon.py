from apysc._material_design.icon.material_phone_icon import MaterialPhoneIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPhoneIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPhoneIcon = MaterialPhoneIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
