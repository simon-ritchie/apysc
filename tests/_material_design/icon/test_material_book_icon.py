from apysc._material_design.icon.material_book_icon import MaterialBookIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialBookIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialBookIcon = MaterialBookIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
