from apysc._material_design.icon.material_notification_important_outlined_icon import (
    MaterialNotificationImportantOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialNotificationImportantOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialNotificationImportantOutlinedIcon = (
            MaterialNotificationImportantOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
