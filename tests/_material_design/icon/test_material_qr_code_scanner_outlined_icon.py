from apysc._material_design.icon.material_qr_code_scanner_outlined_icon import (
    MaterialQrCodeScannerOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialQrCodeScannerOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialQrCodeScannerOutlinedIcon = MaterialQrCodeScannerOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
