from apysc._material_design.icon.material_visibility_off_outlined_icon import (
    MaterialVisibilityOffOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialVisibilityOffOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialVisibilityOffOutlinedIcon = MaterialVisibilityOffOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
