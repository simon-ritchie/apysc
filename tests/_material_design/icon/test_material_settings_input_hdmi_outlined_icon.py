from apysc._material_design.icon.material_settings_input_hdmi_outlined_icon import (
    MaterialsettingsInputHdmiOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsettingsInputHdmiOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsettingsInputHdmiOutlinedIcon = (
            MaterialsettingsInputHdmiOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
