from apysc._material_design.icon.material_outlet_icon import MaterialOutletIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialOutletIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialOutletIcon = MaterialOutletIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
