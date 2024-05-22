from apysc._material_design.icon.material_filter_alt_icon import MaterialFilterAltIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFilterAltIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFilterAltIcon = MaterialFilterAltIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
