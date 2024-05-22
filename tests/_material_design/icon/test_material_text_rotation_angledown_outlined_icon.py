from apysc._material_design.icon.material_text_rotation_angledown_outlined_icon import (
    MaterialTextRotationAngledownOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialTextRotationAngledownOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialTextRotationAngledownOutlinedIcon = (
            MaterialTextRotationAngledownOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
