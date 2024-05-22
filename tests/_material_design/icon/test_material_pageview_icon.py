from apysc._material_design.icon.material_pageview_icon import MaterialPageviewIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPageviewIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPageviewIcon = MaterialPageviewIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
