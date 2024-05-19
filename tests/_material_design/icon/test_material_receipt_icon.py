from apysc._material_design.icon.material_receipt_icon import MaterialreceiptIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialreceiptIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialreceiptIcon = MaterialreceiptIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
