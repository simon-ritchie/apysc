from apysc._material_design.icon.material_text_rotate_up_outlined_icon import MaterialtextRotateUpOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialtextRotateUpOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialtextRotateUpOutlinedIcon = MaterialtextRotateUpOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
