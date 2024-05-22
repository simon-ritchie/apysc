from apysc._material_design.icon.material_report_off_icon import MaterialReportOffIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialReportOffIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialReportOffIcon = MaterialReportOffIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
