from apysc._material_design.icon.material_settings_input_hdmi_outlined_icon import (
    MaterialSettingsInputHdmiOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSettingsInputHdmiOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSettingsInputHdmiOutlinedIcon = (
            MaterialSettingsInputHdmiOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
