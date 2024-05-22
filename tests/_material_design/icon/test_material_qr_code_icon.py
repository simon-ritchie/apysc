from apysc._material_design.icon.material_qr_code_icon import MaterialQrCodeIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialQrCodeIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialQrCodeIcon = MaterialQrCodeIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
