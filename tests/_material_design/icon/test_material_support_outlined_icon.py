from apysc._material_design.icon.material_support_outlined_icon import (
    MaterialSupportOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSupportOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSupportOutlinedIcon = MaterialSupportOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
