from apysc._material_design.icon.material_view_day_icon import MaterialviewDayIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialviewDayIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialviewDayIcon = MaterialviewDayIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
