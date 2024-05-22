from apysc._material_design.icon.material_hd_icon import MaterialHdIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHdIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHdIcon = MaterialHdIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
