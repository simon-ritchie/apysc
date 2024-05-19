from apysc._material_design.icon.material_qr_code_scanner_outlined_icon import MaterialqrCodeScannerOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialqrCodeScannerOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialqrCodeScannerOutlinedIcon = MaterialqrCodeScannerOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
