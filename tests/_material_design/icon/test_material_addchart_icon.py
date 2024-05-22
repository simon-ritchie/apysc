from apysc._material_design.icon.material_addchart_icon import MaterialAddchartIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAddchartIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAddchartIcon = MaterialAddchartIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
