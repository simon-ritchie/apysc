from apysc._material_design.icon.material_notification_important_icon import (
    MaterialNotificationImportantIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialNotificationImportantIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialNotificationImportantIcon = MaterialNotificationImportantIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
