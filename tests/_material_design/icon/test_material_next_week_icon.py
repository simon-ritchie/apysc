from apysc._material_design.icon.material_next_week_icon import MaterialnextWeekIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialnextWeekIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialnextWeekIcon = MaterialnextWeekIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
