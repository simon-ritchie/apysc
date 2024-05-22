from apysc._material_design.icon.material_book_outlined_icon import (
    MaterialBookOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialBookOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialBookOutlinedIcon = MaterialBookOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
