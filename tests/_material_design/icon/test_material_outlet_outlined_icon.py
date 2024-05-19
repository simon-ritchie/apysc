from apysc._material_design.icon.material_outlet_outlined_icon import (
    MaterialoutletOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialoutletOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialoutletOutlinedIcon = MaterialoutletOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
