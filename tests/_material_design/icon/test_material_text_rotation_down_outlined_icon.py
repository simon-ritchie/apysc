from apysc._material_design.icon.material_text_rotation_down_outlined_icon import (
    MaterialtextRotationDownOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialtextRotationDownOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialtextRotationDownOutlinedIcon = (
            MaterialtextRotationDownOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
