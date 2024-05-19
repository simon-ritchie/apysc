from apysc._material_design.icon.material_drag_indicator_icon import MaterialdragIndicatorIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdragIndicatorIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdragIndicatorIcon = MaterialdragIndicatorIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
