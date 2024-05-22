from apysc._material_design.icon.material_outlined_flag_icon import (
    MaterialOutlinedFlagIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialOutlinedFlagIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialOutlinedFlagIcon = MaterialOutlinedFlagIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
