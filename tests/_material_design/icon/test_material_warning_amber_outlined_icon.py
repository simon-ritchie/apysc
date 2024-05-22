from apysc._material_design.icon.material_warning_amber_outlined_icon import (
    MaterialWarningAmberOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialWarningAmberOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialWarningAmberOutlinedIcon = MaterialWarningAmberOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
