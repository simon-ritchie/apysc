from apysc._material_design.icon.material_print_disabled_icon import (
    MaterialPrintDisabledIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPrintDisabledIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPrintDisabledIcon = MaterialPrintDisabledIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
