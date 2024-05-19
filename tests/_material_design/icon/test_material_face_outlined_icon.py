from apysc._material_design.icon.material_face_outlined_icon import (
    MaterialfaceOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialfaceOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialfaceOutlinedIcon = MaterialfaceOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
