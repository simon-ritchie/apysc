from apysc._material_design.icon.material_error_outline_outlined_icon import (
    MaterialerrorOutlineOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialerrorOutlineOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialerrorOutlineOutlinedIcon = MaterialerrorOutlineOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
