from apysc._material_design.icon.material_report_off_icon import MaterialreportOffIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialreportOffIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialreportOffIcon = MaterialreportOffIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
