from apysc._material_design.icon.material_book_online_outlined_icon import (
    MaterialBookOnlineOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialBookOnlineOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialBookOnlineOutlinedIcon = MaterialBookOnlineOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
