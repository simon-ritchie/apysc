from apysc._material_design.icon.material_login_outlined_icon import MaterialloginOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialloginOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialloginOutlinedIcon = MaterialloginOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
