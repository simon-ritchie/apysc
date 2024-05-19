from apysc._material_design.icon.material_book_icon import MaterialbookIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialbookIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialbookIcon = MaterialbookIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
