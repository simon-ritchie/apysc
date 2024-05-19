from apysc._material_design.icon.material_library_books_icon import (
    MateriallibraryBooksIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallibraryBooksIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallibraryBooksIcon = MateriallibraryBooksIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
