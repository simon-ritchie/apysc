from apysc._material_design.icon.material_settings_input_antenna_icon import (
    MaterialsettingsInputAntennaIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsettingsInputAntennaIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsettingsInputAntennaIcon = MaterialsettingsInputAntennaIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
