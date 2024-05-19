from apysc._material_design.icon.material_warning_amber_outlined_icon import (
    MaterialwarningAmberOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialwarningAmberOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialwarningAmberOutlinedIcon = MaterialwarningAmberOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
