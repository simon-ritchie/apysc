from apysc._material_design.icon.material_schedule_icon import MaterialScheduleIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialScheduleIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialScheduleIcon = MaterialScheduleIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
