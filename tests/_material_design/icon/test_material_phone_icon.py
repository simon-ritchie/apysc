from apysc._material_design.icon.material_phone_icon import MaterialphoneIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialphoneIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialphoneIcon = MaterialphoneIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
