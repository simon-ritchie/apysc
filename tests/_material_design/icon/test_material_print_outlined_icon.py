from apysc._material_design.icon.material_print_outlined_icon import (
    MaterialPrintOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPrintOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPrintOutlinedIcon = MaterialPrintOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
