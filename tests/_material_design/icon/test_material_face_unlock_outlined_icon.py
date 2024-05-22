from apysc._material_design.icon.material_face_unlock_outlined_icon import (
    MaterialFaceUnlockOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFaceUnlockOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFaceUnlockOutlinedIcon = MaterialFaceUnlockOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
