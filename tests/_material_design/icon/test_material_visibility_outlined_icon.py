from apysc._material_design.icon.material_visibility_outlined_icon import (
    MaterialVisibilityOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialVisibilityOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialVisibilityOutlinedIcon = MaterialVisibilityOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
