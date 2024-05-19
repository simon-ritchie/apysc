from apysc._material_design.icon.material_report_off_outlined_icon import MaterialreportOffOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialreportOffOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialreportOffOutlinedIcon = MaterialreportOffOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
