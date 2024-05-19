from apysc._material_design.icon.material_voice_over_off_outlined_icon import (
    MaterialvoiceOverOffOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialvoiceOverOffOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialvoiceOverOffOutlinedIcon = MaterialvoiceOverOffOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
