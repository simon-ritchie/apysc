from apysc._material_design.icon.material_announcement_icon import (
    MaterialAnnouncementIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAnnouncementIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAnnouncementIcon = MaterialAnnouncementIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
