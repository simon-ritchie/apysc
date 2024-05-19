from apysc._material_design.icon.material_face_unlock_outlined_icon import (
    MaterialfaceUnlockOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialfaceUnlockOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialfaceUnlockOutlinedIcon = MaterialfaceUnlockOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
