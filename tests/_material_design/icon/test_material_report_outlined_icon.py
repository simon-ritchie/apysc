from apysc._material_design.icon.material_report_outlined_icon import MaterialreportOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialreportOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialreportOutlinedIcon = MaterialreportOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
