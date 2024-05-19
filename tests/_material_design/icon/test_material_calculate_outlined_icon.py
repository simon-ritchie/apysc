from apysc._material_design.icon.material_calculate_outlined_icon import (
    MaterialcalculateOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcalculateOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcalculateOutlinedIcon = MaterialcalculateOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
