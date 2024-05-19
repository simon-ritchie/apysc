from apysc._material_design.icon.material_home_outlined_icon import MaterialhomeOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialhomeOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialhomeOutlinedIcon = MaterialhomeOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
