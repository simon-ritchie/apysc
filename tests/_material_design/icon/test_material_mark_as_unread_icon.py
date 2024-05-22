from apysc._material_design.icon.material_mark_as_unread_icon import (
    MaterialMarkAsUnreadIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMarkAsUnreadIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMarkAsUnreadIcon = MaterialMarkAsUnreadIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
