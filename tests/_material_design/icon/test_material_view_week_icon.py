from apysc._material_design.icon.material_view_week_icon import MaterialviewWeekIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialviewWeekIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialviewWeekIcon = MaterialviewWeekIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
