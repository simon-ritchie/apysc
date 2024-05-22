from apysc._material_design.icon.material_minimize_outlined_icon import (
    MaterialMinimizeOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMinimizeOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMinimizeOutlinedIcon = MaterialMinimizeOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
