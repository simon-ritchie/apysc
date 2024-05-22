from apysc._material_design.icon.material_branding_watermark_icon import (
    MaterialBrandingWatermarkIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialBrandingWatermarkIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialBrandingWatermarkIcon = MaterialBrandingWatermarkIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
