from apysc._material_design.icon.material_filter_alt_icon import MaterialfilterAltIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialfilterAltIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialfilterAltIcon = MaterialfilterAltIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
