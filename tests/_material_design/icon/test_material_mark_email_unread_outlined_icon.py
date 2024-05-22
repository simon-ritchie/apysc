from apysc._material_design.icon.material_mark_email_unread_outlined_icon import (
    MaterialMarkEmailUnreadOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMarkEmailUnreadOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMarkEmailUnreadOutlinedIcon = (
            MaterialMarkEmailUnreadOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
