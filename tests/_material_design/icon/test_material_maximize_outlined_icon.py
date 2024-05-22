from apysc._material_design.icon.material_maximize_outlined_icon import (
    MaterialMaximizeOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMaximizeOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMaximizeOutlinedIcon = MaterialMaximizeOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
