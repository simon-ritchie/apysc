from apysc._material_design.icon.material_phone_outlined_icon import MaterialphoneOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialphoneOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialphoneOutlinedIcon = MaterialphoneOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
