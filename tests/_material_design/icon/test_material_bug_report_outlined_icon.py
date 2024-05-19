from apysc._material_design.icon.material_bug_report_outlined_icon import (
    MaterialbugReportOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialbugReportOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialbugReportOutlinedIcon = MaterialbugReportOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
