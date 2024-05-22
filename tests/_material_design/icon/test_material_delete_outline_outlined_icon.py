from apysc._material_design.icon.material_delete_outline_outlined_icon import (
    MaterialDeleteOutlineOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialDeleteOutlineOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialDeleteOutlineOutlinedIcon = MaterialDeleteOutlineOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
