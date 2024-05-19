from apysc._material_design.icon.material_business_outlined_icon import MaterialbusinessOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialbusinessOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialbusinessOutlinedIcon = MaterialbusinessOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
