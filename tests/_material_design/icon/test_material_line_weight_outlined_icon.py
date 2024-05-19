from apysc._material_design.icon.material_line_weight_outlined_icon import (
    MateriallineWeightOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallineWeightOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallineWeightOutlinedIcon = MateriallineWeightOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
