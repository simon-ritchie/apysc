from apysc._material_design.icon.material_text_rotation_angleup_outlined_icon import (
    MaterialtextRotationAngleupOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialtextRotationAngleupOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialtextRotationAngleupOutlinedIcon = (
            MaterialtextRotationAngleupOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
