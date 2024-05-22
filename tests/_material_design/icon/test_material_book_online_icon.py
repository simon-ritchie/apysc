from apysc._material_design.icon.material_book_online_icon import MaterialBookOnlineIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialBookOnlineIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialBookOnlineIcon = MaterialBookOnlineIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
