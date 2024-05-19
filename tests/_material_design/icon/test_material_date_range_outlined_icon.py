from apysc._material_design.icon.material_date_range_outlined_icon import MaterialdateRangeOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdateRangeOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdateRangeOutlinedIcon = MaterialdateRangeOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
