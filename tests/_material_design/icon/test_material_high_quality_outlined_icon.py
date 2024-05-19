from apysc._material_design.icon.material_high_quality_outlined_icon import MaterialhighQualityOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialhighQualityOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialhighQualityOutlinedIcon = MaterialhighQualityOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
