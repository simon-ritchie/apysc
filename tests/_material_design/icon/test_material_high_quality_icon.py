from apysc._material_design.icon.material_high_quality_icon import MaterialhighQualityIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialhighQualityIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialhighQualityIcon = MaterialhighQualityIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
