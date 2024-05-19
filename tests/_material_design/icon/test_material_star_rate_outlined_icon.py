from apysc._material_design.icon.material_star_rate_outlined_icon import (
    MaterialstarRateOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialstarRateOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialstarRateOutlinedIcon = MaterialstarRateOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
