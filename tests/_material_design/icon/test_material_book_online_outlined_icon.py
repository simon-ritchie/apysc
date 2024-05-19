from apysc._material_design.icon.material_book_online_outlined_icon import MaterialbookOnlineOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialbookOnlineOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialbookOnlineOutlinedIcon = MaterialbookOnlineOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
