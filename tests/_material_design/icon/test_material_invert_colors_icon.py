from apysc._material_design.icon.material_invert_colors_icon import (
    MaterialInvertColorsIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialInvertColorsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialInvertColorsIcon = MaterialInvertColorsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
