from apysc._material_design.icon.material_warning_outlined_icon import (
    MaterialWarningOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialWarningOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialWarningOutlinedIcon = MaterialWarningOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
