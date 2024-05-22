from apysc._material_design.icon.material_report_gmailerrorred_outlined_icon import (
    MaterialReportGmailerrorredOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialReportGmailerrorredOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialReportGmailerrorredOutlinedIcon = (
            MaterialReportGmailerrorredOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
