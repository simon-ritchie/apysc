from apysc._material_design.icon.material_flip_to_back_outlined_icon import (
    MaterialFlipToBackOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFlipToBackOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFlipToBackOutlinedIcon = MaterialFlipToBackOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
