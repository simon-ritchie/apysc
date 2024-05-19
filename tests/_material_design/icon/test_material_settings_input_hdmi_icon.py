from apysc._material_design.icon.material_settings_input_hdmi_icon import MaterialsettingsInputHdmiIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsettingsInputHdmiIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsettingsInputHdmiIcon = MaterialsettingsInputHdmiIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
