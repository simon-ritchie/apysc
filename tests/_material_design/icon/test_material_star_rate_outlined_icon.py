from apysc._material_design.icon.material_star_rate_outlined_icon import (
    MaterialStarRateOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialStarRateOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialStarRateOutlinedIcon = MaterialStarRateOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
