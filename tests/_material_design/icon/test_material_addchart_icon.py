from apysc._material_design.icon.material_addchart_icon import MaterialaddchartIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialaddchartIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialaddchartIcon = MaterialaddchartIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
