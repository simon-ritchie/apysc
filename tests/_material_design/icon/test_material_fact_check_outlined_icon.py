from apysc._material_design.icon.material_fact_check_outlined_icon import (
    MaterialfactCheckOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialfactCheckOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialfactCheckOutlinedIcon = MaterialfactCheckOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
