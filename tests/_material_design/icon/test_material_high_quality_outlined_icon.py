from apysc._material_design.icon.material_high_quality_outlined_icon import (
    MaterialHighQualityOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHighQualityOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHighQualityOutlinedIcon = MaterialHighQualityOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
