from apysc._material_design.icon.material_next_week_icon import MaterialNextWeekIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialNextWeekIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialNextWeekIcon = MaterialNextWeekIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
