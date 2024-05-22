from apysc._material_design.icon.material_report_icon import MaterialReportIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialReportIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialReportIcon = MaterialReportIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
