from apysc._material_design.icon.material_text_rotation_none_outlined_icon import MaterialtextRotationNoneOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialtextRotationNoneOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialtextRotationNoneOutlinedIcon = MaterialtextRotationNoneOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
