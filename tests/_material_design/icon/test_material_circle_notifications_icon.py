from apysc._material_design.icon.material_circle_notifications_icon import MaterialcircleNotificationsIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcircleNotificationsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcircleNotificationsIcon = MaterialcircleNotificationsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
