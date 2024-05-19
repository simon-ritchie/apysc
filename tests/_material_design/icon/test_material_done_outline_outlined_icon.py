from apysc._material_design.icon.material_done_outline_outlined_icon import MaterialdoneOutlineOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdoneOutlineOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdoneOutlineOutlinedIcon = MaterialdoneOutlineOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
