from apysc._material_design.icon.material_date_range_icon import MaterialdateRangeIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdateRangeIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdateRangeIcon = MaterialdateRangeIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
