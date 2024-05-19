from apysc._material_design.icon.material_smart_button_outlined_icon import (
    MaterialsmartButtonOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsmartButtonOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsmartButtonOutlinedIcon = MaterialsmartButtonOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
