from apysc._material_design.icon.material_book_outlined_icon import (
    MaterialbookOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialbookOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialbookOutlinedIcon = MaterialbookOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
