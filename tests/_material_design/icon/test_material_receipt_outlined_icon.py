from apysc._material_design.icon.material_receipt_outlined_icon import (
    MaterialReceiptOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialReceiptOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialReceiptOutlinedIcon = MaterialReceiptOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
