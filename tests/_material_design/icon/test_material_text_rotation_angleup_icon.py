from apysc._material_design.icon.material_text_rotation_angleup_icon import MaterialtextRotationAngleupIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialtextRotationAngleupIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialtextRotationAngleupIcon = MaterialtextRotationAngleupIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
