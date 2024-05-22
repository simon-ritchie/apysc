from apysc._material_design.icon.material_bug_report_outlined_icon import (
    MaterialBugReportOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialBugReportOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialBugReportOutlinedIcon = MaterialBugReportOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
