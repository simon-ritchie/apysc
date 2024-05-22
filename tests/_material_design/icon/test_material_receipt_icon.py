from apysc._material_design.icon.material_receipt_icon import MaterialReceiptIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialReceiptIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialReceiptIcon = MaterialReceiptIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
