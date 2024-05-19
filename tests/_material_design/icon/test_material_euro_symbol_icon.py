from apysc._material_design.icon.material_euro_symbol_icon import MaterialeuroSymbolIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialeuroSymbolIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialeuroSymbolIcon = MaterialeuroSymbolIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
