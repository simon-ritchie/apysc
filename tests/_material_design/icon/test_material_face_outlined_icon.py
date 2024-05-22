from apysc._material_design.icon.material_face_outlined_icon import (
    MaterialFaceOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFaceOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFaceOutlinedIcon = MaterialFaceOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
