from apysc._material_design.icon.material_settings_input_composite_icon import (
    MaterialsettingsInputCompositeIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsettingsInputCompositeIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsettingsInputCompositeIcon = MaterialsettingsInputCompositeIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
