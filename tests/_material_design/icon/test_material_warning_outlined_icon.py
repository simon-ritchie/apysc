from apysc._material_design.icon.material_warning_outlined_icon import (
    MaterialwarningOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialwarningOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialwarningOutlinedIcon = MaterialwarningOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
