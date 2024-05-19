from apysc._material_design.icon.material_qr_code_outlined_icon import (
    MaterialqrCodeOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialqrCodeOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialqrCodeOutlinedIcon = MaterialqrCodeOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
