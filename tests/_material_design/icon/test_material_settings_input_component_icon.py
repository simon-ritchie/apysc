from apysc._material_design.icon.material_settings_input_component_icon import (
    MaterialsettingsInputComponentIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsettingsInputComponentIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsettingsInputComponentIcon = MaterialsettingsInputComponentIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
