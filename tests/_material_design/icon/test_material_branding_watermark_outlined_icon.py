from apysc._material_design.icon.material_branding_watermark_outlined_icon import (
    MaterialBrandingWatermarkOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialBrandingWatermarkOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialBrandingWatermarkOutlinedIcon = (
            MaterialBrandingWatermarkOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
