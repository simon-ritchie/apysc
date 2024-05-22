from apysc._material_design.icon.material_text_rotation_none_outlined_icon import (
    MaterialTextRotationNoneOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialTextRotationNoneOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialTextRotationNoneOutlinedIcon = (
            MaterialTextRotationNoneOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
