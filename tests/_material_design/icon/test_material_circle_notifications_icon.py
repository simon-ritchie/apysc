from apysc._material_design.icon.material_circle_notifications_icon import (
    MaterialCircleNotificationsIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCircleNotificationsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCircleNotificationsIcon = MaterialCircleNotificationsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
