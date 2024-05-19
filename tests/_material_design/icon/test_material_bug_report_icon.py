from apysc._material_design.icon.material_bug_report_icon import MaterialbugReportIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialbugReportIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialbugReportIcon = MaterialbugReportIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
