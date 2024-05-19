from apysc._material_design.icon.material_library_books_outlined_icon import (
    MateriallibraryBooksOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallibraryBooksOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallibraryBooksOutlinedIcon = MateriallibraryBooksOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
