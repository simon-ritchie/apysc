from apysc._material_design.icon.material_report_icon import MaterialreportIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialreportIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialreportIcon = MaterialreportIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
