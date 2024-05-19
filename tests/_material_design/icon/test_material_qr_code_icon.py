from apysc._material_design.icon.material_qr_code_icon import MaterialqrCodeIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialqrCodeIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialqrCodeIcon = MaterialqrCodeIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
