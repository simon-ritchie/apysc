from apysc._material_design.icon.material_hd_outlined_icon import MaterialHdOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHdOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHdOutlinedIcon = MaterialHdOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
