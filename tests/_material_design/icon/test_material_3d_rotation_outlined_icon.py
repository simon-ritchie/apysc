from apysc._material_design.icon.material_3d_rotation_outlined_icon import (
    Material3DRotationOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterial3DRotationOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: Material3DRotationOutlinedIcon = Material3DRotationOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
