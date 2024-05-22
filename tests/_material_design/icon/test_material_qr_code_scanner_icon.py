from apysc._material_design.icon.material_qr_code_scanner_icon import (
    MaterialQrCodeScannerIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialQrCodeScannerIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialQrCodeScannerIcon = MaterialQrCodeScannerIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
